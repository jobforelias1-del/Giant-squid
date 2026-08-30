---
name: update-dossier
description: Run the Operation Architeuthis dossier update — sweep new Architeuthis dux literature, verify sources, extend the evidence ledger, refresh the deliverables and the compiled book, and open a draft PR. Use whenever asked to update the kraken / giant squid dossier, on a schedule or on demand.
---

# Operation Architeuthis — Dossier Update Procedure

You are updating a **source-grounded evidence audit** of the giant squid (*Architeuthis dux*). The repository root holds nine deliverables (`README.md`, `executive-summary.md`, `full-dossier.md`, `evidence-ledger.csv`, `observation-timeline.md`, `unresolved-questions.md`, `myths-and-evidence.md`, `annotated-bibliography.md`, `source-quality-audit.md`) plus a compiled book in `book/`. This is a literature review — propose no original biological theory.

## 1. Absorb the standards (non-negotiable)

Read `README.md` (methodology), `source-quality-audit.md` (verification discipline and §5's deliberately withheld numbers), `unresolved-questions.md`, and skim `evidence-ledger.csv`. The rules you inherit:

- Every substantive claim gets an evidence category — **A** direct observation of living animals · **B** physical specimen · **C** indirect · **D** informed inference · **E** speculation/anecdote — plus confidence, limitations, and an identifier.
- Verify every new source independently (existence, authorship, year, venue, topical match) before admitting it; record how you verified it. Never invent citations, DOIs, measurements, or quotations.
- Preserve disagreements between credible sources as disagreements; never average conflicting measurements; never state estimates as facts; distinguish first-claimed from first-well-verified.
- The colossal squid (*Mesonychoteuthis hamiltoni*) appears only as a clearly labeled comparison species.
- Never weaken an existing hedge, verdict, or disputed-status without new verified evidence. Never assert the numbers withheld in `source-quality-audit.md` §5 without sighting the original sources.

## 2. Sweep for new evidence

Search the peer-reviewed literature, museum and agency announcements (NOAA, NIWA, Te Papa, NHM, Smithsonian, Schmidt Ocean), and reputable news for anything on *Architeuthis dux* newer than the ledger's latest entries: new papers, specimens, strandings, live observations or footage, eDNA and genomic work, formal rebuttals in the size or lifespan debates, and any movement on the twelve items in `unresolved-questions.md`. Trace press claims back to primary sources.

## 3. Decide honestly

**If nothing substantive is new: stop.** Report exactly that. Do not pad the dossier, do not open a PR. (Deep-sea teuthology moves slowly; an empty quarter is the normal result.)

## 4. Apply real additions

1. Append new rows to `evidence-ledger.csv`, continuing the existing claim-ID sequences (LIV/SPE/TAX/DEP/DIE/REP/SWH/MYT).
2. Update the affected deliverables and `observation-timeline.md` (mark each new event well-verified / first-claimed / disputed); keep the executive summary under ~2,000 words; keep the "What Would We Know If All Inferences Were Removed?" section strictly A/B evidence.
3. Log the update — sources admitted, sources checked-but-excluded, verification outcomes, anything unresolved — in `source-quality-audit.md`.
4. Regenerate the book: `python3 book/build_book.py` (deps: `pip install weasyprint markdown`; LibreOffice with Writer for the `.docx` — fall back to `--format pdf` if Writer is unavailable).

## 5. Ship

Commit on a fresh branch cut from `origin/main` (e.g. `claude/dossier-update-<year>Q<quarter>`, unless your session designates a branch), push, and open a **draft** pull request titled `Dossier update: <year> Q<quarter>` summarizing what changed, what was checked but excluded, and any citation problems reported honestly.
