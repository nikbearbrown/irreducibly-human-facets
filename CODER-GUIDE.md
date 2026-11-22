# Coding guide: job-posting lines and the Irreducibly Human facets

## What you are doing

You will read lines from real job postings and give each line a few short codes. The **mode** says what kind
of statement the line is. The **facet** says which of seven human capacities the work in that line rests on.
You may add a second facet, and you say how sure you are. There are no answers to match: the point is to see
whether different coders reading this same guide land in the same place. Work on your own, do not discuss lines
with anyone else who is coding them, and do not look the postings up.

For each line, record:
- **mode**: DO, KNOW, BE, SIT or OUT
- **facet**: the primary facet code (PA, ES, SP, MS, CC, CD, EW, NH). Use "-" only for OUT lines, or for a SIT
  line whose setting points to no facet.
- **facet 2**: an optional second facet code, or blank for none. Leave it blank whenever facet is "-", and never
  repeat the primary facet.
- **confidence**: H, M or L, your confidence in the facet code
- **note**: a short reason (a few words). Always write one when your confidence is L.

When the rules below do not settle a line, make your best call, mark it L, and say why in the note.

## Mode (what kind of statement)

| Mode | Use when | Example shape | Strength as evidence |
|---|---|---|---|
| DO | The line names work the job does, including "ability to [concrete act]" | "Investigate and resolve...", "Ability to lift 25 lbs" | Strong |
| KNOW | Knowledge, tools, degrees, licences, years of experience | "5+ years...", "Unrestricted state license" | Medium (licences: see rule 6) |
| BE | A quality or trait of the person, with no act named | "Strong communicator", "integrity", "empathetic" | Weak |
| SIT | The setting or stakes, not the act | "business-critical customers", "regulated domains", shifts | Context only (this is what O*NET Work Context measures) |
| OUT | Not about the job: pay, benefits, perks, EEO, privacy, fraud notices, work authorisation, remote or onsite policy, duplicate lines | | Excluded |

## Facets, in listing terms

| Code | Facet | Code a line here when its load-bearing act is... | Typical listing verbs |
|---|---|---|---|
| PA | Pattern & Association | producing, classifying, summarising, translating, building to a known method; holding knowledge of tools, rules, domains | build, implement, write, analyse, report, maintain, follow instructions; tool lists; degrees |
| ES | Embodied & Sensorimotor | using the body or senses on the physical world, or being physically present where the work needs it | lift, stand, assemble, inspect parts, operate equipment, see clients in person |
| SP | Social & Personal | working through a relationship with particular people, where trust or history carries the work | mentor, coach, care for, trusted advisor, protect the relationship, build relationships with clients |
| MS | Metacognitive & Supervisory | checking whether output (own, others', a machine's) is right; noticing something is wrong; knowing when a rule does not apply; framing the problem | review before it ships, audit, validate, know when to make an exception, identify off-nominal issues, frame the problem |
| CC | Causal & Counterfactual | finding why something happens, or estimating what would happen under a change | root cause, troubleshoot, replicate the issue, diagnose, run experiments, off-policy evaluation, risk assessment |
| CD | Collective & Distributed | working within and through teams and institutions: alignment, coalitions, governance, norms | partner across teams, align stakeholders, resolve cross-functional tensions, build governance, influence without authority |
| EW | Existential & Wisdom | owning a consequential decision and its outcome; weighing values against each other; ethics; what is worth doing | be accountable for results, balance risk against objectives, make calls under ambiguity, define strategy or success, licences |
| NH | No clean home | capacity limits rather than capacities: juggling, sustained attention, workload | manage multiple priorities under deadlines |

## Unit

One line of a posting's duties or requirements section: one bullet, or one paragraph when the posting has no bullets. The parser in `scripts/listing_sections.py` keeps the lines between a duty heading ("What you'll do", "Requirements", ...) and a stop heading ("Benefits", "Compensation", "EEO", ...). It lets through some perks and legal lines; those are coded OUT.

## Decision rules

1. **Code the act, not the adjective.** "Strategic thinker" is BE; "decide scope, sequencing, and trade-offs" is DO.
2. **Load-bearing facet first.** Ask which capacity the line would fail without. Most lines involve Pattern & Association somewhere; code PA first only when nothing else carries the line.
3. **Customer contact is not automatically Social & Personal.** The book places transactional service in Tier 1. Support tickets and status updates go to the act they serve (often CC for troubleshooting). SP needs a particular person and a relationship that matters.
4. **Teamwork verbs are Collective & Distributed, but weakly.** "Collaborate with Product and Engineering" is CD at medium confidence. It is teamwork, not collective knowledge production, the same gap the O*NET crosswalk found.
5. **Ownership language is Existential & Wisdom at low confidence.** Postings use "own" loosely. It gets high confidence only when an outcome and its stakes are named ("be accountable for improving those results").
6. **A licence is an accountability marker.** State licences, bar membership, DEA registration: KNOW + EW. A vendor certification is KNOW + PA.
7. **Presence is Embodied only when the work needs it.** "See clients in person" is SIT + ES. An onsite-only policy for desk work is OUT.
8. **Strategy and objectives go to Existential & Wisdom**, following the crosswalk's placement of Developing Objectives and Strategies. Strategy that names a causal claim ("what will move this audience") would be CC.
9. **Data analysis is Pattern & Association** unless the line names a cause, an experiment, or a counterfactual ("assess effectiveness" alone is PA + CC at low confidence).
10. **Confidence** H / M / L is the coder's own. Low-confidence lines are the ones a second coder should see first.
