# The Unofficial Guide

Yashasvini Kattelu, city_guides

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none, because the grader can't
> read it.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Week 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->


This project is a retrieval-augmented generation (RAG) system built around a
collection of regional travel guides. It retrieves the most relevant chunks
from the guides based on a user's question and uses those chunks to generate
an answer. The system also uses a relevance cutoff to refuse questions that
are outside the information covered by the guides. The corpus covers topics
such as accessibility, transportation, food, accommodations, seasons, and
individual towns in the region.

## Chunking Strategy

**Chunk size:** 500 characters 
**Overlap:** 75 characters

I chose a chunk size of 500 characters because my corpus contains regional
travel guides made up of relatively short paragraphs and sections, with each
paragraph usually covering a specific topic. When I looked at several
documents, I noticed that useful information was often contained within
individual paragraphs, so I wanted to keep those ideas together instead of
cutting them at arbitrary character boundaries.

I chose an overlap of 75 characters because some information may fall near a
chunk boundary. The overlap keeps some context between neighbouring chunks
without creating too much duplicated text.

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `guide_accessibility.md#0` — produced by: `chunker.py::split_documents`

> # Getting around the region with limited mobility
>
> An honest assessment rather than a promotional one. Some of these places are
> difficult and it is better to know in advance.
>
> ## Straightforward
>
> **Thornby Wells** is the easiest town in the region. It is flat, compact, and
> everything is within three minutes of everything else. Parking is free for two
> hours anywhere in town and the station is central. The pump room and gardens are
> level throughout.

**Chunk 2** — source: `guide_corry_vale.md#5` — produced by: `chunker.py::split_documents`

> n the second village is 12th century and always unlocked.
>
> ## Where to stay
>
> Perhaps thirty beds in the entire valley, spread across two pubs and a handful of farmhouse rooms. In summer these are booked months ahead. Camping is permitted on two marked fields and nowhere else.
>
> ## When to go

**Chunk 3** — source: `guide_givens_mill.md#3` — produced by: `chunker.py::split_documents`

> , food served lunchtimes and Thursday to Saturday evenings.
>
> ## What to see
>
> The mill runs tours on the hour from 11 to 3 and the machinery is operating during them, which is loud and much more impressive than a static exhibit. The church has a Saxon doorway. The river walk downstream reaches Brightwater in about three hours.
>
> ## Where to stay

**Chunk 4** — source: `guide_marchwood.md#1` — produced by: `chunker.py::split_documents`

> ne, since almost nothing of interest is near the station.
>
> ## Getting there
>
> Every railway line in the region meets here, which is the city's defining feature. Trains to Brightwater run every 40 minutes until 11pm. The airport is 20 minutes out by a dedicated bus that runs every 15 minutes and costs more than the equivalent taxi shared between three people.
>
> ## Getting around

**Chunk 5** — source: `guide_regional_transport.md#5` — produced by: `chunker.py::split_documents`

> den Bay coast road is cut into the cliff
> and is slow rather than difficult.
>
> Parking is the constraint rather than driving. Both Halden Bay lots fill by
> 10am on summer weekends. Kestrelford's lower car park is free and involves a
> steep walk up.
>
> ## Walking and cycling
```
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**

Which town is the easiest in the region for someone with limited mobility, and what specific features make it accessible?

**Answer:**

Thornby Wells is the easiest town in the region for someone with limited mobility. It is accessible because it is flat, compact, everything is within three minutes of everything else, parking is free for two hours anywhere in town, the station is central, and the pump room and gardens are level throughout.

**Source:** 

guide_accessibility.md, guide_corry_vale.md, guide_kestrelford.md

```
```

**My relevance cutoff:**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

I set my relevance cutoff to **0.6**. The five in-corpus questions had best distances ranging from **0.3181 to 0.6076**, while the five out-of-scope questions ranged from **0.8293 to 0.9026**. There is a clear gap between the in-corpus and out-of-scope questions, although two in-corpus questions were slightly above 0.6. I kept 0.6 as the cutoff because it accepts most relevant questions while rejecting all five clearly out-of-scope questions.

| Question | In corpus? | Best distance |
|---|---|---|
| 1 | Yes | 0.4406 |
| 2 | Yes | 0.3181 |
| 3 | Yes | 0.4491 |
| 4 | Yes | 0.5961 |
| 5 | Yes | 0.6076 |
| 6 | No | 0.8874 |
| 7 | No | 0.8969 |
| 8 | No | 0.9026 |
| 9 | No | 0.8293 |
| 10 | No | 0.8529 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.** 

I used AI to help choose a chunking strategy for my travel-guide
corpus. I explained that the documents contain relatively short paragraphs
and topic-based sections, and AI recommended paragraph-aware chunking with a
500-character chunk size and 75-character overlap. I implemented and tested
the strategy myself and used `python app.py chunks` to inspect the resulting
chunks.

**2.**

I used AI to help evaluate my retrieval results and choose a relevance
cutoff. I provided the distances from my five in-scope and five out-of-scope
questions, and AI helped me compare the two groups. I kept the cutoff at 0.6
because it rejected all five out-of-scope questions, although one in-scope
question was slightly above the cutoff.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Week 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     week 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->


| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 3/5 | 3/5 | 3/5 | MISSED |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunk completeness | 4 of 5 | 1/5 | 1/5 | 1/5 | MISSED |
| 5. Correct source attribution | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     week — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->


| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer (4 of 5) | MISSED | 3/5 in all three runs. Q3 (food/hours) and Q4 (wheelchair) both failed — the correct sentence exists in the source doc but wasn't in the retrieved chunk used for generation. |
| 2 | Every answer names a source (5 of 5) | MET | All 5 questions cited a source document in every run, including Q4, which named `guide_accessibility.md` even though it couldn't answer. |
| 3 | Gate stops out-of-corpus questions (4 of 5) | MET | 5/5 refused, well above target. Measured once since the gate is deterministic. |
| 4 | Chunk completeness (4 of 5) | MISSED | 1/5 sample chunks start on a clean sentence boundary. Chunks 2–5 all begin mid-word or mid-sentence (e.g. "n the second village," "ne, since almost nothing"), showing the chunker splits on a fixed character count with no boundary awareness. |
| 5 | Correct source attribution (4 of 5) | MET | 4/5 — Q1, Q2, Q3, Q5 named the document that actually matches the question topic. Q4 didn't attribute anything since it never answered. |


## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

**Criterion 1 — Retrieved chunk contains the answer (MISSED)**

Stage: retrieval.

Confirmed by inspecting chunk boundaries directly (`python app.py chunks`):
in both failing cases, the answer-bearing content exists as its own
separate, cleanly-split chunk — the chunker isn't at fault, and retrieval
simply didn't select the right chunk out of the ones available.

- Q4 ("which places are challenging for a wheelchair user"): the answer
  lives in `guide_accessibility.md#4` ("Difficult" section — Kestrelford,
  Halden Bay: "hard going with luggage or a pushchair, let alone a
  wheelchair", Corry Vale). This is a distinct chunk from
  `guide_accessibility.md#0` ("Straightforward" section, Thornby Wells),
  which is the chunk that was actually retrieved and used in all 3 runs.
- Q3 (Brightwater food/opening hours): the answer lives in
  `guide_eating.md#3` ("Opening hours" section — "kitchens across the
  region stop serving at 9pm and often earlier"). This is a distinct chunk
  from `guide_eating.md#1` ("The pattern worth knowing", pricing), which is
  what was retrieved and used instead.

Pattern: in both cases, embedding similarity favored a chunk that matches
the question's general topic (accessibility, eating) over the chunk that
actually contains the answer, because the answer chunk's distinguishing
vocabulary (wheelchair, pushchair, opening hours, 9pm) carries less weight
in semantic similarity than broad topical overlap. A keyword-matching
method (BM25) would catch these exact terms directly.

**Criterion 4 — Chunk completeness (MISSED)**

Stage: chunking.

4 of 5 sample chunks begin mid-word or mid-sentence (e.g. Chunk 2 of the
original sample: "n the second village," Chunk 4: "ne, since almost
nothing"). The chunker (`chunker.py::split_documents`) splits every 500
characters with a fixed overlap and no check for sentence or word
boundaries. This is a separate problem from Criterion 1 — the accessibility
and eating chunks inspected above happened to split cleanly at section
headers, but that's not guaranteed generally, as the original 5-chunk
sample shows.

**Pattern across both misses:** Criterion 1's failures are a retrieval
problem (wrong chunk selected from otherwise well-formed chunks); Criterion
4's failure is a chunking problem (chunks not reliably starting/ending on
clean boundaries). They're independent issues at different pipeline stages,
not the same root cause — worth noting since fixing one won't fix the
other.

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
