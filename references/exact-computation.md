# Exact computation

## Start from the smallest executable contract

Write the data schema, formula, filter, order and output shape before computing.
Use a short script with the existing runtime. Avoid asking an LLM to add long lists,
produce hashes, track every revision, or invent a numerical answer from a screenshot.
If data is missing, preserve unknowns instead of silently substituting zeros.

Do not optimize an unrelated general algorithm. Solve the supplied instance and keep
just enough structure to verify it or rerun after a correction.

## Numerical and ordering discipline

| Risk | Correct handling |
|---|---|
| Money or huge integer minor units | Use integer minor units, Python integers, JS BigInt or decimal arithmetic. Never pass values above JS safe-integer range through Number. |
| Nearest-integer/decimal rounding | Match the source: JS Math.round, ties-to-even and decimal half-up differ, especially for negative ties. |
| Exact ties | Apply the stated ID/index ordering, not a default unstable sort. |
| Unicode normalization | Match specified Unicode version and ordered transforms. NFKC, casefold and lowercase are not interchangeable. |
| Missing fields | Distinguish absent, null, empty string and zero; preserve types. |
| Dates/windows | Preserve timezone and inclusive/exclusive endpoints. Equal-to-expiry can be stale or invalid. |
| Unit vectors | A dot product equals cosine only after the required normalization. Reject zero/nonfinite vectors. |
| Hashes | Hash the specified bytes, not a pretty-printed approximation. |

## JSON and hashing

Parse strictly. Duplicate JSON keys are not harmless: many parsers silently retain
the last one. Inspect them when a certificate or digest requires unambiguous data.
Preserve large numeric spelling before a parser converts it to an imprecise float.

Before hashing, determine:

1. What is the exact object/array/text being hashed?
2. Is key order prescribed, recursively sorted, or irrelevant?
3. What encoding, escaping, separators and newline convention apply?
4. Are strings normalized before hashing?
5. Is the output full SHA-256, truncated hex, FNV-1a prefix, or another format?

`JSON.stringify`, Python `json.dumps` and a language's default encoder need not
produce identical bytes. ASCII-only compact JSON is easier to reproduce, but use
that fact only when the contract actually guarantees ASCII.

FNV-1a-32 over UTF-8 bytes starts at 2166136261. For each byte:
`h = ((h XOR byte) * 16777619) mod 2^32`.
In JavaScript use `Math.imul`; float multiplication can lose required low bits.
Output `fnv1a32:` plus eight lowercase hex digits only when the task specifies it.

For filename hashes, settle slash conversion, category source, leading `./`, ASCII
sorting and the final LF. Simulate transformed names if only those bytes are graded;
do not mutate the student's source archive unnecessarily.

The bundled `scripts/evidence.py` can hash bytes or inspect strict JSON. It deliberately
does not guess the task's canonicalization.

## CSV, tables and aggregation

- Identify delimiter, quoting, header names, encoding/BOM and missing-value behavior.
- Filter with every required condition, including exact city/case/date/unit matching.
- Parse quantities and prices losslessly; compute the actual requested measure.
- Check matching-row count, a hand-computed example and the total's magnitude.
- Do not mistake a sum of unit prices for sum(quantity × price).
- Respect full-data vs participant-only denominators and weighted vs unweighted rows.

## Rankings and correlations

For top-k embeddings, map the student's displayed document order to the underlying
vectors/scores. Return relative indices or document IDs as requested, not indices
from a global cache. Validate result cardinality and uniqueness.

Spearman correlation compares ranks for the **same documents**. If search returns
scores sorted by rank, first align each score vector back to document identity.
Use average ranks for ties and handle constant vectors explicitly. Do not correlate
only top-three lists when the question requests all corpus documents.

A verified finite cache can eliminate repeated model work, but only if the actual
input texts/models/options match. Unknown texts or changed model versions require
recomputation; do not invent missing vectors or claim cached data came from a new run.

## Encodings and stream reconstruction

- Inspect candidate encoding forms before trying transforms.
- For a small known transform set, enumerate legal inverse orders and verify the
  result against the actual plaintext/schema, rather than guess one order.
- For byte streams, preserve chunk order and use incremental UTF-8 decoding.
- Buffer NDJSON until a complete newline-terminated record exists; a network chunk
  is not necessarily a JSON record or full Unicode character.
- Apply the given stop rules: include text from the terminal done record if required,
  stop on the first error/done, ignore later records and incomplete trailing JSON.
- Preserve spaces, escaped newlines and Unicode; ignore fields such as `thinking`
  only if the question tells you to.

## Unicode ledgers and revision pipelines

Treat the specified procedure as a state machine, not a bag of interchangeable
filters. A typical pipeline may require normalization, replay removal, revision
selection/tie-break, eligibility, business-key deduplication, signed net and digest.
Its order changes the result.

Maintain intermediate counts and excluded IDs/reasons privately so a failure can
be isolated. Apply a confusable map once unless specified otherwise. Remove only
listed invisible scalars, not every character that looks ignorable. Verify runtime
Unicode data version before claiming compatibility with a pinned normalization spec.

## Cache/protocol simulations

Implement only the supplied machine. Do not add real-world HTTP rules omitted by
an exam-defined subset. Keep the trace serial or concurrent exactly as specified.
Use small fixtures for:

- age equal to freshness lifetime;
- schedule change at the same timestamp as a request;
- matching and nonmatching Vary values, including missing headers;
- no-cache vs no-store vs private;
- 304 retaining body but updating required metadata;
- unsafe-method invalidation;
- final state ordering and digest.

Emit requested probe results in the specified order, independently of internal maps.

## Low-cost validation

For one task, choose checks that can change confidence: shape/type assertions,
small independent recalculation, invariant totals, boundary fixtures and a canonical
digest comparison. A hundred self-derived cases do not prove a hidden grader's
expectations. If the local contract is unclear, obtain the actual artifact or exact
feedback rather than multiplying tests around an assumption.
