# Operation Architeuthis — Giant Squid Research Dossier

## Purpose

This repository contains a bounded, source-grounded research investigation into
the giant squid, *Architeuthis dux*. It is a **literature review and evidence
audit**: a synthesis of what humanity currently knows about giant squid, how we
know it, and which major questions remain unresolved. It proposes no original
biological theory and makes no novelty claims.

The review is organized around twelve core questions, covering direct
observations of living animals, the physical specimen record, size and mass
estimates, geographic and depth distribution, ecology (movement, hunting, diet,
predators), reproduction and life history, interactions with sperm whales, the
history of imaging live animals, exaggerated or disputed claims, and the
observational obstacles that keep key questions open.

## Methodology

1. **Research plan first.** The twelve core questions were partitioned into
   eight evidence domains (live observation and imaging milestones; specimens
   and size; taxonomy, genetics and distribution; depth and habitat; diet and
   predators; reproduction and lifespan; sperm-whale interactions; myths and
   history).
2. **Parallel evidence sweep.** Each domain was researched independently
   against the open literature: peer-reviewed journals, museum records,
   government science agencies (e.g. NOAA, NIWA), university and expedition
   reports, with press coverage used only as a pointer back to primary sources.
3. **Evidence categorization.** Every substantive claim was assigned one of
   five evidence categories:
   - **A** — direct observation of living giant squid;
   - **B** — physical specimen evidence (captured, stranded, bycaught,
     preserved, or predator-stomach material);
   - **C** — indirect evidence (scars, predator stomach contents implying
     behavior, environmental correlations);
   - **D** — informed inference (allometry, statolith interpretation, isotope
     ecology, statistical modeling);
   - **E** — speculation, anecdote, or unverifiable claim.
4. **Independent citation verification.** Each domain's source list was passed
   to a separate adversarial verification pass that checked identifiers (DOIs
   via Crossref, stable URLs, institutional pages) and confirmed authorship,
   year, venue, and topical match before sources were admitted to the ledger.
5. **Ledger before prose.** The evidence ledger (`evidence-ledger.csv`) was
   compiled before the narrative documents were drafted; the dossier and
   summary documents were then written against the ledger, not the other way
   around.
6. **Audit pass.** Drafts were audited against the ledger for uncited claims,
   estimate-stated-as-fact errors, and internal inconsistencies; unresolved
   citation problems are reported honestly in `source-quality-audit.md`
   rather than papered over.

Widely repeated claims were traced toward their earliest reliable source where
feasible. Disagreements between credible sources are recorded as disagreements.
Where evidence is too weak for a firm conclusion, the documents say so.

## Directory Guide

| File | Contents |
| --- | --- |
| `README.md` | This file: purpose, methodology, directory guide. |
| `executive-summary.md` | Readable overview of the strongest established findings (≤ ~2,000 words). |
| `full-dossier.md` | Detailed report organized by the twelve core questions, with inline citations and explicit evidence/inference separation. Includes the special section **"What Would We Know If All Inferences Were Removed?"** |
| `evidence-ledger.csv` | Machine-readable ledger of substantive claims: claim ID, claim, evidence category, source, year, source type, direct/inferred, confidence, limitations, citation or identifier. |
| `observation-timeline.md` | Chronological timeline of major specimens, photographs, recordings, expeditions, and live observations, distinguishing first *claimed* from first *well-verified* events. |
| `unresolved-questions.md` | Ranked list of major unknowns, the evidence available for each, and why each remains unresolved. |
| `myths-and-evidence.md` | Recurring claims (extraordinary size, ship attacks, sea monsters, whale battles) rated as supported / plausible but unconfirmed / disputed / unsupported. |
| `annotated-bibliography.md` | Key sources with concise notes on why each matters; primary vs. secondary identified. |
| `source-quality-audit.md` | Search methods, inclusion/exclusion decisions, missing or inaccessible sources, conflicting measurements, and limitations of this review. |

## Book Edition

The entire dossier is also compiled into a single typeset volume in `book/`:
`Operation-Architeuthis-Dossier.pdf` (94-page A4 book with linked contents) and
`Operation-Architeuthis-Dossier.docx` (editable Word edition). Both are generated
from the files above by `book/build_book.py` (deps: `pip install weasyprint markdown`,
plus LibreOffice for the .docx) — rerun it after editing any deliverable.

## Scope Note

The subject is *Architeuthis dux* only. The colossal squid
(*Mesonychoteuthis hamiltoni*) and sperm whale (*Physeter macrocephalus*)
appear strictly as clearly labeled comparison or interaction species.
