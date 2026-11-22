# Job-listings facet coding, round 2: code the lines on your own

**What this is.** You are one of several coders, AI models and people, coding the same 208 lines from 12 job postings **independently**, so Nik Bear Brown can compare the coders afterwards. [README.md](README.md) says which way in fits your coder; this page is the task itself. You code every line under the guide below, check your codes, and hand in one folder.

**First written 2026-11-22.** Two Claude models coded round 2 first, under these same rules. Their codes stay private until every coder has handed in.

## 1. Independence rules (read first)

- **Work alone.** Don't contact, message or coordinate with any other coder, agent, session or person doing this task. That means no shared files, no shared chats, no shared memory and no agent-to-agent messages. Don't ask another AI or person to code, check or discuss any line.
- **One coder per hand-in.** One model, or one person, makes every code in your hand-in: no ensembles, no voting across models, no second opinions.
- **Don't look at anyone else's codes or comments.** Don't open `hand-ins/` (your copy shouldn't have it) or any file you didn't write named `codes*.tsv`, `replies*`, `comparison*`, `agreement*` or `disagreements*`. Don't read the kit's GitHub issues or pull requests between starting and handing in, because other coders may discuss lines there. If your copy sits inside a larger project, stay inside your copy.
- **Don't look the postings up.** No web search, no opening the links in `postings.tsv`, no reading the employer's other ads. Code only from the lines you are given.
- **One posting at a time, fresh each time.** Agents: a new conversation or headless call for each posting. People: work through the postings in order. You may fix a mistake, but don't recode earlier lines to match later ones.
- **Don't change the guide or the messages.** When a rule doesn't settle a line, make your best call, mark it L, and say why in the note.
- **Keep the text private.** The lines are job-ad text. Don't publish, post or push them, your codes, or your notes.

## 2. The postings

All 12 were live on public company job boards on 2026-11-11. Each is the only posting in the sample from its employer, and no employer appears in round 1. `postings.tsv` has the source ids and links for the record; don't open them while coding.

| Posting | Title | Company | Lines |
|---|---|---|---|
| F01 | Software Engineer, Manufacturing Automation & Test | Intuitive Surgical | 12 |
| F02 | Digital Nurse Practitioner (Remote, NY License) | Galileo | 24 |
| F03 | Enterprise Account Executive, Privy | Stripe | 19 |
| F04 | IT Support Specialist II | Trace3 | 21 |
| F05 | Commercial Counsel | FullStory | 17 |
| F06 | Senior Intercompany Accountant | Lambda | 23 |
| F07 | GTM Recruiter | Databricks | 10 |
| F08 | Senior Product Designer | CoStar | 11 |
| F09 | Senior Data Scientist, RBQM Analytics | AbbVie | 17 |
| F10 | MES Technician (Night Shift) | Form Energy | 21 |
| F11 | Senior Product Manager II - Identity & Access Management | Appian | 19 |
| F12 | Licensed Marriage and Family Therapist- Remote | BetterHelp | 14 |

A script kept only the lines between a duties or requirements heading and a stop heading (benefits, pay, EEO and the like). A few perks and legal lines got through; code them OUT. Line ids run `F01-01`, `F01-02` and so on.

## 3. The coding guide

[CODER-GUIDE.md](CODER-GUIDE.md) is the instrument, word for word. It covers the five modes, the seven facets plus "no clean home", the unit of coding, and ten decision rules. Read all of it before you start. The same text is inside every message (ways A to C) and in the coding sheet's Codebook tab (way D).

## 4. The messages (agents)

For each posting the model gets:

- **System prompt:** `prompts/system.txt`.
- **Message:** `prompts/task_template.txt`, with `{codebook}` set to CODER-GUIDE.md and the posting's title, company, section headings and numbered lines filled in. `scripts/render_prompts.py` does this exactly. `handout-private/messages/` holds the same messages with reply instructions added for chat.
- **Reply:** one JSON object matching `schema/reply.schema.json`: `{"codes": [...]}`, with one entry per line in order, each with `item`, `mode`, `facet`, `facet2` (`""` for none), `conf`, `cue` (the deciding words, copied from the line) and `note` (a short reason).

Use your model's normal settings, and record any reasoning or effort setting in RUN.md. Don't add examples, extra rules or your own system prompt.

## 5. Checks

`scripts/check_handin.py <hand-in folder>` checks that:

- every one of the 208 lines is coded exactly once, with no extra items;
- mode is DO, KNOW, BE, SIT or OUT; facet is a facet code or "-"; facet2 is blank or a facet code; conf is H, M or L;
- an OUT line has facet "-"; "-" appears only on OUT or SIT lines; facet2 is blank when facet is "-" and never repeats facet.

It writes `codes.tsv` and `report.json`. If a posting's reply fails, it gets **one** retry, sent with the list of errors. If the retry fails too, keep it and record the errors. Low-confidence lines without a note and a missing RUN.md show as warnings.

## 6. What to hand in

One folder named `facets-r2-<coder>-<the date you started, YYYYMMDD>`, for example `facets-r2-gpt-5-codex-20261122` or `facets-r2-ta1-20261124`. Name a model coder by the model that actually answered. People use a coder code, never a full name. The folder holds:

- `replies/F01.json` to `replies/F12.json` (agents), or `coding-sheet.xlsx` or `coding-sheet.csv` (people);
- `codes.tsv` and `report.json` from `check_handin.py` (Bear can run it if you can't);
- `RUN.md`, containing:
  - the way in (A, B, C or D);
  - agents: the model and version you asked for, **the model that served the replies** (from the provider's response, if it reports one), and any reasoning or effort setting;
  - the date and time you started and finished;
  - anything you did differently from this page, and why.

Hand the folder in privately. On the Explorer cluster, make it inside the drop box `/projects/aiskunks/irreducibly-human-facets/hand-ins/` with `mkdir`, then copy your files into it with plain `cp -R`. README.md, Contributing, step 4 has the commands. Anywhere else, send it to Bear or to whoever gave you the kit. Don't push it to any repository, don't attach it to an issue or pull request, and don't open anyone else's hand-in.
