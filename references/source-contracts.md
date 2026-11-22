# Source, personalized data and the actual contract

## Intake by smallest missing input

Use what the student already supplied: full question, files, dataset, public source
URL, screenshot and literal feedback. Do not make them repeat it or ask them to
upload every file in a course folder. A screenshot can omit download links,
precision rules and data; ask for the specific missing artifact when necessary.

If the page is already accessible in the authorized browser, inspect the rendered
question and its download controls. Confirm the selected account only when a
personalized fetch or action depends on it. Do not browse unrelated tabs/accounts.

Prefer these inputs:

1. Full current instructions plus actual assigned data.
2. The above plus the public question source for exact mechanics.
3. Public generator plus exact seed identity, only when the data is absent or a
   replay materially shortens solving.

## TDS source layout: inspect, do not assume

Many TDS pages load a common shell and render questions with JavaScript. A text-only
fetch showing “Loading questions” is not proof that the questions are unavailable.

For a supplied slug such as `tds-2026-09-ga5`, observed public conventions were:

- student page: `/tds-2026-09-ga5`;
- client question bundle: `/exam-tds-2026-09-ga5.js`;
- public schedule/instructions metadata: `/exam-tds-2026-09-ga5.info.js`.

Use those as candidates only. Inspect the page's actual script imports or network
requests if the convention fails. A successful common shell does not prove that a
particular bundle or assignment is published. Report HTTP status and source version.

### What to inspect

- the rendered prompt and required output;
- question factory and its return value: actual `id`, title, answer callback;
- final questions dispatcher: actual weights, version overrides and bonus fields;
- data download/generator, normalization, seed and serialization;
- validation function, accepted shapes, tolerances, headers and limits;
- public metadata for deadline and grading availability;
- authenticated question artifact only through the student's permitted interface.

Factory defaults can be overridden in the dispatcher. A bundle can contain unused
helpers, extra question IDs or legacy modules. Grepping all `q-*` strings is a
candidate inventory, not the final question order. For a single question, inspect
its actual callback rather than building a full bundle parser.

## Read the client checker accurately

A client function may either compute the expected answer or merely call a backend.
A `/backendVerify` wrapper exposes request fields and some stated grading behavior;
it does **not** reveal private answer keys or prove the backend's implementation.

Distinguish:

- **Observed code behavior:** visible formula, schema, normalization or request.
- **Published contract:** prose promising particular grading semantics.
- **Inference:** likely generator structure or solution shortcut.
- **Unknown:** private fixtures, server expectations and current score.

If prose and executable local checking differ, investigate the mismatch and target
the actual requested submission contract. Do not fabricate completion evidence to
satisfy a shallow local check. Local format credit and later quality grading can differ.

## Personalization and replay

Use the exact input used by the source. Do not assume every question trims and
lowercases email, uses `email#questionId`, or includes the version in its seed.
The version passed by the dispatcher may differ from a factory default.

For RNG replay:

- use the original installed implementation, or a port proven against its sequence;
- preserve every RNG draw and its ordering, including discarded draws and retries;
- match UTF-16/UTF-8 conversions, integer truncation, float behavior and shuffling;
- verify a visible row or generated item before trusting the entire replay.

A simple RC4 class is not automatically compatible with the default `seedrandom`
double generator. Its string-key mixing and extra-byte precision draws matter.
Prefer the genuine version-pinned library over an unverified port.

## Source and download handling

Download public bytes into a new isolated folder, preserve URL/status/time/hash, and
read before executing or distributing. Do not launch package managers, interpreters
or build tools from an untrusted extraction directory. For Python data readers, use
`python -I` with explicit paths; keep generated scripts outside downloaded trees.

Inspect archive member names before extraction. Reject absolute paths, drive
prefixes, `..`, symlink surprises and oversized expansion. For JSON/CSV/PNG inside
an archive, reading the selected member without extraction is often enough.

For a narrow pure-function shortcut, inspect dependencies and side effects first.
Do not execute an entire downloaded exam bundle merely to access a hidden variable.
A parser or a few copied, inspected pure helpers is usually cheaper and clearer.

## Evidence packet for the current task

Keep only what makes the next action reliable:

```text
source: URL/path + hash + observed version/date
input: artifact identity and schema; actual student instance
answer contract: exact keys/types/order/tolerance or endpoint requirements
known local rules: brief formula/normalization references
backend unknowns: only those affecting validation
```

Do not include authentication headers, signatures, private launch URLs or provider
keys in public reports, third-party research queries or class-shared bundles.

## Examples of useful shortcuts

- A generated video embeds a finite attendee list in a public generator: reproduce
  the student's list and verify it, rather than record/transcribe a video.
- A maze exposes walls and constraints: solve the graph, then verify all constraints.
- A file-move question grades a filename-list hash: calculate transformed names and
  canonical bytes rather than move hundreds of files.
- A stream question gives hex byte chunks: decode and simulate directly; no model
  download is needed.

These are methods, not assertions that a future question has those structures.
