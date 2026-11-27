# Irreducibly Human facets: reading job postings line by line

**The coding kit for the paper *Reading Work Through Seven Facets*.**

[The paper's working draft](https://github.com/nikbearbrown/reading-work-through-seven-facets/blob/main/paper/manuscript.md) · [The coder guide](CODER-GUIDE.md) · [Contributing](#contributing) · [How to code round 2](#how-to-code-round-2)

**We're inviting coders.** Round 2 needs independent readers, people and AI models alike, to code 208 lines from 12 job postings with the same written guide. You don't need to know the project to help. You need about two hours, or a model you can run. See [Contributing](#contributing).

> **Coding in round 2?** Read this page, then [INSTRUCTIONS.md](INSTRUCTIONS.md), then code. Leave the paper, its issues and this repository's issues until you have handed in. The paper's draft reports interim results, and reading them first would make your coding no longer independent.

## What this is about

AI is changing which parts of work people do. The [Irreducibly Human framework](https://github.com/nikbearbrown/Irreducibly-Human/blob/aa9f9ff65bf710519be6496486a04f3197a6d22e/README.md#the-taxonomy) describes seven facets of human capacity, and how well machines handle each. At one end is Pattern & Association, where AI is already stronger than people. The others include judging whether work is right, finding out why something happens, working through relationships and institutions, and owning decisions about what is worth doing. This project uses the facets as labels for kinds of work, not as a ranking.

To ask what jobs need from people in these terms, you need a description of jobs that can show all seven. The standard US source, the [O\*NET database](https://www.onetcenter.org/content.html), describes jobs partly through a list of 52 abilities. When we mapped that list onto the facets, almost all of it fell in the first two, Pattern & Association and Embodied & Sensorimotor. That tells us how the abilities list was built. It doesn't tell us whether jobs need the other facets.

Job postings are a second source. Employers describe the work line by line, in their own words: "investigate why the failure recurs", "review the output before it ships", "be accountable for the result". This project reads those lines. Each duty or requirement line is coded for **what kind of statement it is** (something the job does, something the worker must know or be, the setting, or nothing to do with the job) and **which facet it rests on**: the capacity the act would fail without.

The question is whether this can be done reliably: whether independent readers, people and models, who apply the same written guide to the same lines land on the same codes. If they do, the guide can profile postings by facet, and the paper extends it to course syllabi, so that what courses grade can be set beside what jobs ask for. If they don't, the lines where they split show where the facet definitions need work.

**What it can't show.** A coded line says what a posting states. It doesn't say what the job really involves, how much of the time it takes, or whether a machine could do it.

## The seven facets

Each line gets one primary facet and, if the line supports it, a second. The full definitions and the ten decision rules are in [CODER-GUIDE.md](CODER-GUIDE.md).

| Code | Facet | A line belongs here when the act it names rests on... | Typical words in a posting |
|---|---|---|---|
| PA | Pattern & Association | producing, classifying, summarising, translating or building to a known method; knowing tools, rules and domains | build, implement, write, analyse, report; tool lists; degrees |
| ES | Embodied & Sensorimotor | using the body or senses on the physical world, or being present where the work needs it | lift, assemble, inspect parts, operate equipment, see clients in person |
| SP | Social & Personal | a relationship with particular people, where trust or history carries the work | mentor, coach, care for, trusted advisor |
| MS | Metacognitive & Supervisory | checking whether output is right (one's own, others', a machine's), noticing something is wrong, knowing when a rule doesn't apply, framing the problem | review before it ships, audit, validate, identify off-nominal issues |
| CC | Causal & Counterfactual | finding why something happens, or estimating what would happen under a change | root cause, troubleshoot, diagnose, run experiments |
| CD | Collective & Distributed | working within and through teams and institutions: alignment, coalitions, governance, norms | partner across teams, align stakeholders, build governance |
| EW | Existential & Wisdom | owning a consequential decision and its outcome, weighing values against each other, deciding what is worth doing | be accountable for results, balance risk against objectives, define strategy |
| NH | No clean home | a limit on capacity rather than a capacity | manage many priorities under deadlines |

The kind of statement, the **mode**, matters as much as the facet. A line that names an act (DO) is stronger evidence than one that names knowledge (KNOW), a trait such as "strong communicator" (BE), or the setting (SIT). Lines about pay, benefits and legal notices are OUT and get no facet.

## What we're doing

| Round | Postings | Lines | Status |
|---|---|---|---|
| 1, development | 12, one from each of 12 job families, from a November 2026 snapshot of company job boards | 240 | Done. The guide was written while coding these lines, then frozen. |
| 2, replication (this kit) | 12 fresh postings from 12 other employers, one per family again | 208 | **Open.** Many independent coders, compared once all have handed in. |

Two Claude models, Sonnet 5.5 and Opus 5.5, coded round 2 first, as the kit's test. Their codes stay private until round 2 closes. The paper reports their agreement as interim results. What's missing is people, and models from other providers.

The same seven facets are also being applied to course syllabi, with a separate guide for evidence such as what a course grades. That work is described in the paper. It isn't part of this kit.

## The paper

***Reading Work Through Seven Facets: a coding protocol for job postings and syllabi***, led by Nik Bear Brown, is part of [Humanitarians AI's research](https://github.com/nikbearbrown/hai-research). Its working draft lives in its own repository, [reading-work-through-seven-facets](https://github.com/nikbearbrown/reading-work-through-seven-facets), which has the paper's own contributor guide and task list. Its draft covers the whole study, with interim results from the Claude coders. If you are coding, read it only after you hand in.

## What needs to be done

- **Independent coders** for round 2: the most useful help now. People, and models outside the Claude family.
- **A runner for another model**, and tests that use made-up lines (see [Improve the scripts](#improve-the-scripts)).
- **A better sample of hands-on work** for a later round. The current postings are mostly desk jobs.
- **Help with the paper itself:** see the [paper's task list](https://github.com/nikbearbrown/reading-work-through-seven-facets#what-needs-to-be-done).

## Contributing

Round 2 is open. The most useful thing you can give it is another independent coder. So far two Claude models, Sonnet 5.5 and Opus 5.5, have coded it. What's missing is people, and models from other providers, including open-weights models run on your own machine or on Explorer. Fixes to the scripts and ideas for later rounds are welcome too. For how coders and authors are credited, see [Credit and what we expect from authors](#credit-and-what-we-expect-from-authors).

### Code round 2

1. **Say you're coding.** Open an issue titled `Round 2 coder: <coder>`. Name the model as it will be served, or, for a person, give a coder code such as `ta2` rather than a name. The issue stops two people running the same coder, and it is how you ask for the lines.
2. **Get the lines.** Members of the AI Skunks group on the Explorer cluster have the whole kit, lines included, at `/projects/aiskunks/irreducibly-human-facets/`. Everyone else gets `handout-private/` from Bear in reply to the issue. Never paste the lines into an issue or pull request.
3. **Make your own copy and code it.** Run `scripts/make_agent_copy.sh <coder> <parent folder>`, then use the way in that fits ([Pick your way in](#pick-your-way-in)). From then until you hand in, follow [INSTRUCTIONS.md](INSTRUCTIONS.md) section 1: don't read this repository's issues or pull requests, and don't look at anyone else's hand-in.
4. **Hand it in privately.** On Explorer, make your folder inside the drop box with `mkdir`, then copy your files into it:

   ```bash
   H=/projects/aiskunks/irreducibly-human-facets/hand-ins
   mkdir $H/facets-r2-<coder>-<YYYYMMDD>
   cp -R my-hand-in/facets-r2-<coder>-<YYYYMMDD>/. $H/facets-r2-<coder>-<YYYYMMDD>/
   ```

   Nobody can list the drop box, and a folder made there is closed to everyone except you and Bear. Use plain `cp -R`, not `cp -a` or `rsync -a`, which would carry your own permissions over. Anywhere else, comment "done" on your issue and Bear will tell you where to send the folder. Don't attach a hand-in to an issue or pull request: it quotes the postings, and other coders would see your codes.

### Improve the scripts

Pull requests are welcome, for example:

- a runner for another model, like `run_claude.py` but for another provider's command-line tool or an OpenAI-compatible server such as vLLM or Ollama, which would make way B easier on Explorer;
- tests for `check_handin.py` and `compare_coders.py` that run on made-up lines, since the real lines aren't in the repository;
- bug fixes and clearer instructions.

A few rules:

- While round 2 is open, don't change `CODER-GUIDE.md`, `prompts/`, `schema/` or `postings.tsv`. Every coder in a round must get the same task. Propose a change in an issue instead.
- Keep posting text out of pull requests entirely: code, tests, fixtures and examples. Make lines up.
- Keep the scripts to the Python standard library, apart from `openpyxl` for reading `.xlsx`.
- Say in the pull request what it changes and how you checked it.
- By opening a pull request you agree to release your contribution under the [MIT licence](LICENSE).

### Suggest changes to the guide or the sample

- **While round 2 is open,** a comment on how to code a particular line goes in your own hand-in (that line's note, or RUN.md), not in an issue, so that later coders don't see it.
- **Anything else goes in an issue:** a rule that is unclear or clashes with another, a facet definition that seems wrong, or an idea for round 3. One gap is already known. Round 2's 12 postings are mostly desk jobs, so a sample with more hands-on work, such as trades, warehouse or field care, would test Embodied & Sensorimotor better.
- The guide changes only between rounds, and each change gets a new version, so that every coder in a round works to the same rules.

### Credit and what we expect from authors

Any paper that reports these rounds follows [Yale's guidance on authorship](https://provost.yale.edu/policies/academic-integrity/guidance-authorship-scholarly-or-scientific-publications). Under it, an author has done **all four** of these:

1. **Contributed to a component of the work:** its conception, design, conduct, analysis, or interpretation of at least part of the results.
2. **Helped write the paper:** drafted part of it, or revised it for substance, not just copy edits.
3. **Approved the final version** before submission.
4. **Agreed to be accountable** for the work, including helping answer questions about its accuracy or integrity.

**Coding a round is acknowledged, but it doesn't by itself make you an author.** Yale's guidance puts helping collect or assemble data, and reviewing a finished draft, in the acknowledgments. Every person who codes is thanked by name there, unless they ask not to be; only your coder code appears in the data. To be an author, combine coding with a component, such as analysing where coders split and why once you've handed in, proposing and testing a guide revision for the next round, or drawing a sample with more hands-on work, and then do the writing, approval and accountability steps too.

**Model coders are reported in the methods** by the model that served the replies. A model can't be an author, since it can't approve the paper or answer for it. The person who ran it is acknowledged for running it.

**If you code as a person, the codes must be your own judgment, made without AI tools:** not ChatGPT, Claude or anything else. The study compares models with people, and AI-assisted codes would quietly compare models with models. [INSTRUCTIONS.md](INSTRUCTIONS.md) section 1 already rules out asking another AI or person to code, check or discuss a line.

If you want to be an author, we expect you to:

- **Read the whole paper,** not just your section. You're putting your name on all of it.
- **Think about it, then give feedback.** Does the method answer the question? Are the comparisons fair? Do the figures show what the text claims, and would a different figure show it better? Do the kappas and counts in the text match `comparison.md` and the tables?
- **Suggest changes when they matter.** Don't make a suggestion just to have made one. If you find nothing to change, say so; that's a useful answer. A real problem, raised clearly with a proposed fix, is the most valuable thing you can give.
- **Disclose AI assistance** everywhere except coding, where a person doesn't use it at all. AI tools are fine for scripts, analysis and drafting, but say where you used them. You stay accountable for everything you contribute.
- **Keep a record of what you did:** what, when, and where it lives (issue, pull request, commit, figure). The paper's contribution statement is drawn from it and lists each author's [CRediT roles](https://credit.niso.org/).
- **Sign off only when you can stand behind it.** Before submission, every author confirms in writing that they have read the full paper, agree with it, and accept accountability for it. If something is wrong or unclear, say so before approval, not after publication.

Raise authorship early, and we'll revisit it as roles change. Author order follows contribution. If you think your work merits authorship and it isn't reflected, say so before the final draft. An issue, a pull request or a hand-in does not by itself settle authorship.

## How to code round 2

Everything one coder needs is in this repository, except the posting lines, which are job-ad text and are handed out privately ([Contributing](#contributing), step 2). Each coder works in its own copy of the kit, codes alone, and hands in one folder. **Coders never talk to one another, never see one another's codes, and never see the first round's codes.** Pick the way in that fits your coder, then follow [INSTRUCTIONS.md](INSTRUCTIONS.md). The lines in `handout-private/` stay private: never push, post or share them.

### Pick your way in

| Your coder can... | Way | What it does |
|---|---|---|
| run Claude Code on a Claude plan | **A. Headless Claude** | `scripts/run_claude.py` makes one blind call per posting, checks the replies and writes the hand-in. |
| run code with any other model | **B. Any model, scripted** | `scripts/render_prompts.py` writes the 12 exact messages. You send each one in a fresh conversation, save the replies, then run `scripts/check_handin.py`. |
| only chat | **C. Hand-out messages** | The 12 files in `handout-private/messages/`, one per fresh chat. Each one is complete and says what to send back. |
| is a person | **D. Coding sheet** | `handout-private/coding-sheet.xlsx`, with dropdowns, the codebook and the postings inside. It takes about 1.5 to 2 hours. |

All four ways give every coder the same text: the guide, the same instructions, and the same lines. Ways A to C send the identical message that the Claude coders got.

### Keep coders apart

- **One copy per coder.** Run `scripts/make_agent_copy.sh <coder-name> <parent folder>`. It makes `facets-r2-kit-<coder-name>/` with an empty hand-in folder inside and leaves `hand-ins/` out. Put the parent folder outside the project that holds this kit, so an agent can't wander into earlier codes.
- **No channel between coders.** Run each agent as its own session. Don't give it messaging tools, a shared folder, a shared chat, or another coder's name or path. If one program launches several agents, it must never pass one agent's output or notes to another.
- **One fresh context per posting.** A new conversation or headless call for each of the 12 postings, so no decision carries over.
- **Collect, then compare.** Coders hand their folders in privately ([Contributing](#contributing), step 4), and only once they have finished. On Explorer, `hand-ins/` is a drop box: coders can hand in to it but can't list it or read anyone else's folder. Nothing is compared until everyone is done.

### What's here

| Path | What it is |
|---|---|
| [INSTRUCTIONS.md](INSTRUCTIONS.md) | The task: independence rules, the postings, the guide, the messages, the checks, and what to hand in. |
| [CODER-GUIDE.md](CODER-GUIDE.md) | The instrument: modes, facets, unit and decision rules. Do not edit it. |
| `prompts/system.txt`, `prompts/task_template.txt` | The system prompt and per-posting message, exactly as the Claude coders got them. The template's `{codebook}` is CODER-GUIDE.md. |
| `schema/reply.schema.json` | The shape of a reply: `{"codes": [{item, mode, facet, facet2, conf, cue, note}, ...]}`. |
| `postings.tsv` | Posting id, title, company, source id, link, line count. Facts only, no ad text. Don't open the links while coding. |
| `handout-private/` | **Private.** `lines.json` (the 208 lines), `messages/F01.md` to `F12.md` (way C), `coding-sheet.xlsx` (way D). |
| `scripts/` | `run_claude.py` (A), `render_prompts.py` (B), `check_handin.py` (all), `compare_coders.py` (after everyone), `make_agent_copy.sh`, and `kitlib.py`, which they share. |
| `hand-ins/` | Where finished hand-ins are collected. Coders never get this folder. |
| [DATA-NOTICES.md](DATA-NOTICES.md) | Where the posting text comes from and what may be done with it. |
| [LICENSE](LICENSE) | MIT, for the guide, prompts, schema and scripts. Not for the posting text. |

The scripts need Python 3.9 or later. Only `check_handin.py`, when it reads a person's `.xlsx`, needs `openpyxl`.

### Way A: headless Claude

```bash
scripts/make_agent_copy.sh sonnet-5-5 ~/facets-coders
cd ~/facets-coders/facets-r2-kit-sonnet-5-5
python3 scripts/run_claude.py my-hand-in/facets-r2-sonnet-5-5-YYYYMMDD --model claude-sonnet-5-5
```

The script runs on your own Claude plan, not an API key. Each call has no tools, settings, MCP servers or memory, and runs from an empty temporary folder. A reply that fails the checks gets one retry with its errors. Finished postings are skipped, so a rerun resumes after a usage limit. **Check the served model** that the script prints: on some plans a request for one model is served by another, and the hand-in should be labelled by the model that actually answered.

### Way B: any model, scripted

```bash
python3 scripts/render_prompts.py prompts.jsonl
```

Each line has `posting`, `items`, `system` and `user`. Send `user`, with `system` as the system prompt, in a fresh conversation. Ask for JSON that matches `schema/reply.schema.json` if your model supports structured output. Save each reply as `replies/<posting>.json` in your hand-in folder, adding a `_meta` object with `model`, `served_models` (if your provider reports them), `effort` and `attempts`. Then run:

```bash
python3 scripts/check_handin.py <hand-in folder>
```

A posting whose reply fails the check gets one retry. Resend the same message with the error list added under the heading `# Your previous reply had these problems; fix them`.

### Way C: hand-out messages

Send `handout-private/messages/F01.md` through `F12.md`, one per fresh chat, by pasting or attaching each. Each message asks for a single `json` block. Save each reply as `replies/F01.json` and so on in the hand-in folder, then write `RUN.md` (INSTRUCTIONS.md, section 6). If you can run Python, `check_handin.py` checks the folder; if not, Bear runs it.

### Way D: a person

Give the coder `handout-private/coding-sheet.xlsx` and `CODER-GUIDE.md`, and nothing else from this project. Use a coder code such as `ta1` in the folder name, not a full name. The coder fills in the Codes tab and hands the file back. It goes into the hand-in folder as `coding-sheet.xlsx` (or `coding-sheet.csv`), and `check_handin.py` reads it.

### Hand in

One folder, `facets-r2-<coder>-<YYYYMMDD>`, laid out as INSTRUCTIONS.md section 6 describes, handed in privately ([Contributing](#contributing), step 4). Never push it, and never attach it to an issue or pull request. All codes stay private until every coder has handed in.

### Compare (once everyone has handed in)

```bash
for d in hand-ins/facets-r2-*; do python3 scripts/check_handin.py "$d"; done
python3 scripts/compare_coders.py comparison.md hand-ins/facets-r2-*
```

`comparison.md` has Fleiss' kappa across all coders (the line label, mode, and each facet's presence), a pairwise kappa table, each coder's facet counts, and upper facets per posting. `disagreements.tsv` lists every line the coders split on, with their notes and the line text, so it stays private.
