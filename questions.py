"""
Your test questions.

Milestone 2 asks you to write five questions your system should be able to
answer from your corpus, specific enough to have a right answer.

  ✗ "What are good dining halls?"          — no right answer
  ✓ "What do students say about wait times at Commons during lunch?"

Fill in `QUESTIONS` below. `expects` is a word or short phrase you'd expect a
correct answer to contain — you'll use it in week 2 when you build a scorer,
and having written it now means you decided what "correct" meant before you saw
any results.

`OUT_OF_SCOPE` holds five questions your documents clearly don't cover. You
need these in Milestone 4 to find where your relevance cutoff belongs, and
again in week 2, where `run_eval.py` runs them through the gate and writes what
happened into your run log — that's the evidence for criterion 3.

Swap them for your own if you like. Keep five of them either way: criterion 3
names a target of "4 of 5", and four of three is not a thing.
"""

QUESTIONS = [
    # {"question": "...", "expects": "..."},
    {"question": "Which town is the easiest in the region for someone with limited mobility, and what specific features make it accessible?", "expects": "Thornby Wells is the easiest town for someone with limited mobility. It is flat and compact, everything is within three minutes of everything else, parking is free for two hours anywhere in town, the station is central, and both the pump room and gardens are level throughout."},
    {"question": "A visitor with limited mobility wants to visit Brightwater. How can they get from the train station to campus, and what accessibility options are available in town?", "expects": "The station is a 15-minute walk from campus on flat ground, and a shuttle meets the four busiest train arrivals. Brightwater is generally level along the river and through the centre, and the mill museum is step-free."},
    {"question": "If a visitor wants good food in Brightwater without paying tourist prices, where should they eat and what should they know about opening hours?", "expects": "They should look on Corry Lane, two streets back from the riverside, where comparable food costs about a third less. Most kitchens in Brightwater stop serving at 9pm, and many restaurants close entirely on Sundays."},
    {"question": "Which places in the region would be particularly challenging for someone using a wheelchair, and why?", "expects": "Kestrelford, Halden Bay, and Corry Vale would be particularly challenging. Kestrelford is built on a slope with a steep walk from the lower car park and has no local transport. Halden Bay has three levels connected by stepped lanes, with only the harbour front being level. Corry Vale has no public transport, villages are two to four miles apart, and many routes are footpaths rather than paved sidewalks."},
    {"question": "A visitor wants to travel around the region without a car. What are the main transportation limitations they should plan for?", "expects": "Rail service is limited to the Brightwater area, with 11 weekday services and 6 Sunday services. Beyond Brightwater, visitors mainly depend on buses or cars. The three regional bus operators do not accept each other's tickets, services are concentrated on weekday daytime hours, and Sunday service is minimal or nonexistent outside Brightwater. Kestrelford has no Sunday bus service, while the Halden Bay coast service runs four times daily year-round."},
]

# Questions from a different world entirely. Your gate should refuse all five.
#
# There are five of these because criterion 3 in criteria.md names a target of
# "at least 4 of 5" — you need five things to try before you can report 4 of 5.
# `run_eval.py` runs these through retrieval and the gate on every eval and
# records what happened, so criterion 3 has evidence in the run log alongside
# the others. They cost no model calls: a refusal never reaches the model.
OUT_OF_SCOPE = [
    "What is the capital of Mongolia?",
    "How do I change the oil in a diesel engine?",
    "Who won the 1994 World Cup?",
    "What is the recommended dosage of ibuprofen for a headache?",
    "How do I write a for loop in Rust?",
]


def answered() -> list[dict]:
    """The questions you've actually filled in."""
    return [q for q in QUESTIONS if q.get("question", "").strip()]
