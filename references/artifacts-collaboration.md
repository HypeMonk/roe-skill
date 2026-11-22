# Artifacts, real recordings and peer collaboration

## Replace repeated manual steps with one verified pipeline

For a single student's artifact, automate:

```text
assigned input → transformation/generation → quality review → size/type validation
→ authorized hosting → direct URL/readback → explicit official Check/Save
```

Do not turn this into a website-building project. Use an existing suitable tool or
short local script and give the student one output file or exact URL.

## Files and media

Read the current format, byte limit, dimensions/duration, direct-URL, CORS and
retention requirements. “100 KB” can mean 100,000 bytes, not 102,400. Verify what the
actual checker uses. Compression that damages the graded content is not success.

- For JSON, serve raw JSON media type and exact schema, not a viewer wrapper.
- For models, validate real container structure and dependencies; a filename ending
  in `.glb` is not proof of a valid model.
- For video/audio, inspect codec, duration, playback and MIME. A share page or private
  drive page is not necessarily a directly fetchable file URL.
- Test the published URL from the grader's expected perspective after upload approval.
- Keep the resource available for the specified evaluation period.

Immediate format marks and later quality/peer marks are distinct. A playable video
or valid model can pass the first check while poorly matching the assigned subject.
Say which stage has been verified.

## Genuine audio or personal evidence

If the task requests the student's own voice, experience, initiative or collaborator
reasons, ask for the smallest genuine input. Draft concise, specific wording from
facts the student supplies; do not invent an experience, collaborator relationship,
recording or public proof.

Give a target duration/word budget and a one-command conversion/hosting pipeline
where useful. Obtain the student's approval before publishing their voice, image,
identity or third-party personal details. If the task permits synthetic media,
label its nature as required; do not present it as a real recording of someone.

## Signed terminal recordings

First establish the actual recorder and receipt contract. A task may inspect a real
account-signed cast, command order, output markers, actual command results and exit.
A fabricated JSONL file is not a substitute for a required genuine recording.

Reduce effort by preparing:

1. prerequisites outside the recording where permitted;
2. exact personalized commands, quoted for the student's shell;
3. output/capture markers and command ordering;
4. real fetch/decode/create/show steps inside the recording;
5. archive and file-size checks;
6. an authorized public upload and exact direct URL.

Do not record secrets. Use dummy tokens only where the task supplies them. Check
whether the challenge rotates and must be fetched in the same recorded session.
Inspect both cast and receipt before packaging; only the official recorder/service
can issue its signature.

## Peer tasks

Separate automation from the ingredient that must come from people.

| Task | Automate | Student/peer input |
|---|---|---|
| Token exchange | Compute own challenge, format rows, deduplicate, track missing replies | Legitimate peers produce their own responses |
| Peer review | Preload media, keyboard navigation, valid-count progress | Informed judgement; broken media is not an arbitrary vote |
| Team game | Explain incentives, compute plans, track saved state | Real room membership and each participant's authorized choices |
| Poster/team artifact | Prepare data, candidate findings, charts and role-specific drafts | Actual idea vote, review and matching-version approval |

Do not create accounts or act as peers to manufacture collaboration. Keep private
launch links, keys and receipts out of group chats. Share code or public findings
when permitted; personalized answers need their own verification.

Send peer messages only after the student approves recipients and content or grants
a bounded messaging instruction. While replies/rendering/upload are pending,
continue independent questions when the participation rules allow it.

## Team posters and evidence

Compute findings from the actual dataset with correct units, weights, denominators,
comparison groups and source references. Preserve a reproducible query/calculation.
Do not invent an interesting statistic or imply model agreement verifies it.

If distinctness is graded, seek a defensible different finding, not paraphrases of
one generic class-wide result. Match text/chart to the chosen team idea. The team
must approve the same version. Respect roles, unanimity and any live attendance
requirement; an automation helper cannot shorten a server-enforced 45-minute session.

Use a suitable available chart/design skill when creating a chart; if none is
available, follow basic readable scales, labels, units and nonmisleading encodings.
Do not install a dashboard framework just to make one static plot.

## When human work blocks progress

Ask for a concrete action, not “do it manually”:

> Record these supplied facts in your own voice for about 60 seconds and upload the
> file here. I will validate, compress and prepare the direct submission URL.

or:

> Choose A/B/equal after inspecting this pair. Broken media should be skipped.
> I can prepare the next pair while you decide.

State whether the action starts a timer or consumes quota. Finish computational
parts first, and hand over a clear minimum valid submission if partial credit exists.
