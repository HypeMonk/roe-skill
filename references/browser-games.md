# Browser automation and visual games

## Inspect the actual mechanism first

A task that looks manual may expose a simpler representation:

| Visible task | Inspect for |
|---|---|
| Video tracking/transcription | Original frames, structured motion data, subtitle/text source, generator |
| Geometric puzzle | Piece poses, polygons, snap grid, constraints, target shape and official validator |
| Interactive game | State API, permitted actions, scoring formula, saved-plan state, session timing |
| Hidden question | DOM including hidden text, source/checker and the intended inspectable clue |
| Data download | Actual JSON/CSV/binary artifact rather than a screenshot of its preview |

Use the page and APIs authorized for the student's own task. An available API does
not grant permission to impersonate peers, access another account or mutate an
unrelated service. Check code and effects before using any third-party console solver.

## Readiness before timed actions

Opening a page can be read-only; pressing Start/Join may create or consume a timed
attempt. Inspect instructions and known session state first. Ask for Start/Join
approval unless the student already explicitly authorized that exact attempt.

Before starting, prepare input access, required scripts/models, output validation,
manual fallback and the save/receipt step. Do not pull a large model after a short
game clock starts. If an interface automatically starts a timer on navigation,
treat navigation to it as the timed action, not as a harmless preview.

## Tool choice

Use available browser tools directly. Inspect snapshots for text/controls and
screenshots for visuals; do not infer image content from filenames alone.
Prefer permitted structured API/WebMCP actions when their schema is known. Otherwise
use DOM interactions or mouse/keyboard automation with a verified target element.

Consult the tool's actual schema. Do not assume `document.modelContext`, a particular
MCP server, Playwright, Chrome DevTools or a shell/browser exists in every client.
If a tool is missing, give the student one precise manual action or short inspected
console snippet that obtains the required evidence.

## Console routines

Write short task-scoped code. It should:

- verify the official origin/path and actual question element;
- use the current student instance, not an email guessed from a filename;
- read only the required account fields and keep auth on the official origin;
- validate input/dataset/version before computing;
- preserve unrelated work and avoid overwriting a different answer silently;
- dispatch the actual input/change events needed by the page;
- provide cancellation/retry where work can be long;
- visibly distinguish prepared, filled, locally validated, checked and saved.

Do not auto-click Check, Save, paid evaluation or game Start. Put such actions behind
explicit authorized steps. A console import can execute arbitrary code in the
student's signed-in page; do not recommend an uninspected remote script or include
private tokens in its URL.

A read-only snapshot can capture text/metadata, but it is not a data download.
Same-origin iframe access can work; cross-origin frames may be inaccessible.
If an artifact contains assigned private codes, keep the snapshot local/private.

## Geometry and exact games

Read the original collision, boundary, snap, orientation/reflection and silhouette
rules. Use geometric search or structured placements instead of manual dragging
when possible. Verify against the official exact geometry/hash, not a visually
similar silhouette. A finite solution cache is valid only for the actual supported
target and configuration.

Translation invariance, allowed rotations and discretization can reduce search.
Use them only when published or observed in the validator. Ask for official
attestation after a verified solution and permitted game actions; never fabricate a
signed completion token.

## Tracking/perception

When original frames are available, process those rather than ask the student to
record a rendered video again. Maintain object identity through time, not merely
nearest detection in the final frame. Validate frame indexing and coordinate origin.

A renderer-specific font/shape template may outperform a general model. It is
appropriate only when the actual pixels match. Distinguish “glyph recognized exactly”
from “track identity proven”: exact OCR alone cannot prove which ball is the target.
Ambiguous detections, occlusion or multiple valid matches need another method or
student review, not a made-up answer.

## Strategic games

Inspect scoring and legal choices before optimizing. Team and individual incentives
may conflict; include both and respect real room membership, saved state and peer
communication rules. A recommended plan is not a saved plan. Verify the game's
readback after an authorized save.

Do not invent payoff coefficients, hidden peer strategies or likely scores. If the
rules are unavailable, explain the known incentive structure and make bounded,
clearly labeled recommendations while continuing other questions.

## Final gate

Give the requested answer or official receipt with its verification status. For
manual confirmation, ask one specific choice and say what it changes. No outcome
is “saved” until the official system confirms it. If the game has ended or the
published deadline passed, finish practice/analysis work but do not claim a new
attempt can earn retroactive marks.
