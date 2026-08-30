# Source Quality Audit

An honest account of how this review was conducted, what its sources can and cannot support, which citations could not be fully verified, and where credible sources disagree. Companion to `README.md` (methodology overview) and `evidence-ledger.csv`.

## 1. Search methods

1. **Decomposition.** The twelve core questions were partitioned into eight evidence domains (live observation & imaging; specimens & size; taxonomy/genetics/distribution; depth & habitat; diet & predators; reproduction & lifespan; sperm-whale interactions; myths & history). Each was researched by an independent pass with its own search trail, so that no single narrative could smooth over inter-domain contradictions.
2. **Search channels.** (a) General web search (used until the session's search budget was exhausted); (b) the Consensus scholarly search service, backed by the Semantic Scholar/Scopus/PubMed index, which returned full bibliographic records and abstracts for peer-reviewed items; (c) targeted retrieval attempts against publisher sites, Crossref, museum collection databases, and government agency pages.
3. **Query strategy.** Each domain combined topic queries ("Architeuthis statolith age", "sperm whale stomach contents Architeuthis"), known-item queries for load-bearing papers, and trace-back queries aimed at finding the *earliest* reliable source of widely repeated claims (e.g., the "300–1,000 m" depth range → Roper & Boss 1982; the "18 m" maximum → 19th-century Newfoundland/NZ reports; the albatross scavenging fractions → Xavier et al. 2003).
4. **Independent verification pass.** Every domain's source list was then handed to a separate adversarial verification pass instructed to assume errors until proven otherwise: confirm each source exists, and that authorship, year, venue, and topical content match the use being made of it.

## 2. Verification results

196 source-checks were performed across the eight domains:

| Outcome | Count | Meaning |
|---|---|---|
| **Verified** | 142 | Title, first author, year, venue (where indexed), and abstract-level content independently confirmed; in most cases the *specific quantitative claims* used by the dossier (e.g., 12.1% Azores diet share, 43 mitogenomes, 2,153–3,060 mm beak-estimate spread, 411–674-day beak ages, 6.4→15 °C oxygen-affinity collapse) were confirmed verbatim in indexed abstracts |
| **Corrected** | 9 | Source real; a bibliographic detail was wrong and was fixed (see §4) |
| **Wrong attribution** | 2 | The cited fact/paper belongs to a different author or paper; re-attributed (see §4) |
| **Could not verify** | 43 | No online confirmation possible from this environment — overwhelmingly network-policy failures, not negative findings (see §3); nearly all retain indirect corroboration; two carry residual flags — a possible wrong attribution on a 2013 Slate byline (treated as reportage, not testimony) and the December 2025 feeding video, which has no independent trace beyond its primary post |
| **Fabricated / not found** | **0** | No invented sources were detected |

## 3. The network constraint (material limitation)

The execution environment's egress proxy **blocked essentially all direct web fetches** — Crossref's API, doi.org, publisher sites (Springer, Wiley, Elsevier, Cambridge, Royal Society, Nature), PubMed Central, archive.org, Wikipedia, museum collection pages (NHM, NHMD, Te Papa, Smithsonian), and agency sites (NOAA, NIWA) — and the general web-search budget was exhausted partway through the project. Consequences, stated plainly:

- **No DOI was dereferenced live.** DOIs given in the deliverables were confirmed against the scholarly index's bibliographic records and standard citation patterns, and are marked in `annotated-bibliography.md` (✱) as format-checked but not resolved end-to-end.
- **Peer-reviewed sources were verified at abstract level**, not by full-text reading. Facts that live only in paper bodies (e.g., the 5.5-m tentacle figure in Kubodera & Mori 2005; the ~4,943-g pilot-whale squid; the ~220-cm sleeper-shark mantle estimate) rest on the research pass's search-snippet evidence and are flagged in the research notes (and, where applicable, in the ledger's limitations column).
- **Web-only sources (agency pages, museum pages, press) are the bulk of the 43 unverifiable items.** For nearly all, the underlying events are well-documented history corroborated by verified peer-reviewed companions (e.g., the NOAA 2019 expedition pages vs the verified Robinson et al. 2021).

## 4. Corrections made during verification

Errors caught by the adversarial pass and **fixed throughout the deliverables**:

1. **Mediterranean record (wrong attribution).** "First record of the giant squid *Architeuthis* sp. in the Mediterranean Sea" (JMBA 2000) is by **María C. González and colleagues**, not the Á.F. González/Guerra (Vigo) group whose byline had been grafted onto it.
2. **Albatross scavenging fractions (wrong attribution).** The "~30% by number / ~85% by mass scavenged" estimate belongs to **Xavier, Croxall & Reid (2003, *Marine Biology* 142:611–622)**, not Rodhouse et al. (1987), which contains no such figures.
3. **Clarke & MacLeod (1982) venue.** Published in ***Memoirs of the National Museum of Victoria* 43:25–42**, not JMBA.
4. **Sea of Japan influx paper.** Indexed with **Kubodera as first author, print year 2018** (online 2016); co-author lists circulating as "Wada et al. 2016" and even "Kubodera, Koyama & Mori" could not be itemized — cited as "Kubodera et al. (2018)".
5. **Author-list completions:** O'Shea confirmed as first author of the 2022 paralarva description; T. Wada of the 2020 eDNA paper; G. Nester of the 2026 canyon-eDNA paper; M.A.C. Roeleveld of the 2002 tentacle-morphology paper; G. Pérez-Gándaras & Guerra's 1978 diet paper resolved to *Investigación Pesquera* 42(2):401–414.
6. **Spelling/venue details:** Solé et al. 2017 co-author is Fortuño (not "Fontuno"); Hoving et al. 2006 title includes "…from the Fladen Ground in the northern North Sea"; Leite et al. 2016 first author is Luciana Leite (initials "T.S." doubtful).
7. **Priority framing.** "First film in natural habitat" is credited in broadcasts to the 2012 submersible; the record shows the remote Medusa platform obtained deep footage days earlier on the same expedition. The dossier states both.

## 5. Numbers deliberately NOT asserted

Flagged as possibly garbled in indexed copies, or resting on unverifiable prior knowledge, and therefore *withheld* from the deliverables pending sight of the originals:

- The exact statolith **day-range in Lordan et al. (1998)** (garbled in indexed copies — a nonsensical descending range in every retrieval); the qualitative conclusion (sub-annual ages, 2.96–4.25%/day growth) is confirmed.
- The exact **model-age range in Landman et al. (2004)** beyond the "≤14 years" upper bound (itself from an abstract rendering, corroborated by independent secondary discussions).
- The widely repeated mitogenome diversity value **π = 0.00035** and the "44× lower than *Dosidicus*" comparison (the verified abstract says only "exceptionally low"; the number's visible trail runs partly through AI-generated tertiary sources).
- The commonly quoted **~10.5 m / 184 kg** measurements of R. Clarke's 1955 whale-stomach squid.
- **Heuvelmans' specific size claims** ("60–90 ft") — his books could not be paged; the claims are characterized generically.
- The exact record count of **Sweeney & Roper (2001)** (often quoted as ~292 through 1999).
- The **Pliny Carteia dimensions** and exact wording of several pre-1900 texts.

## 6. Inclusion and exclusion decisions

- **Included:** peer-reviewed papers (any date); museum and agency records; expedition reports; monographs; widely cited expert gray literature (the TONMO/O'Shea–Bolstad fact sheets) *with its status declared*; press reports **only** where they are the sole documentation of a real event (2006 video, 2012 depths, coastal live encounters) and always flagged as press-sourced.
- **Excluded from evidentiary use:** Wikipedia and tertiary compilations (retained in exactly two places as the only traceable carrier of a widely repeated detail — the 10 July 2012 dive date and the 15 January 2002 Kyoto photograph — both flagged); cryptozoological syntheses (Heuvelmans) except as objects of study; the 2026 Bari "systematic review" (pay-to-publish venue, 0 citations, recycled claims — verified to exist, used only to document disagreement over specimen counts); social-media video (December 2025 feeding clip) except as an explicitly unvetted event.
- **Comparison species** (colossal squid, sperm whale) appear only in clearly labeled comparison/interaction roles, per the project brief.

## 7. Conflicting measurements and how they were handled

Recorded as disagreements, never averaged (full detail in the dossier and ledger):

| Quantity | Competing values | Status |
|---|---|---|
| Maximum total length | 12 m verified (McClain 2015) · ~13 m expert (O'Shea/Bolstad; ALCES) · ~15 m O'Shea's outer bound · 20 m plausible (Paxton 2016) · 16.8–17.4 m historical claims | disputed above ~13 m |
| Maximum mantle length | 2.25 m · ~2.75 m · 2.79 m · 2.4 m (different reliability filters) | unresolved |
| Maximum mass | ~220 kg weighed · 275 kg · 300 kg estimates · "nearly a ton" (institutional web page, echoing discredited estimates) | >300 kg unsupported |
| Lifespan | <1 y · ~1 y · 1.1–3 y · 3–6 y · ≤14 y | unresolved; increment periodicity never validated |
| Depth | 630–900 m and 759 m directly observed (platform squid encounters 557–950 m, not all *Architeuthis*-specific) · 400–600 m trawled · 125–250 m isotope average · "300–1,000 m" textbook envelope | unresolved; no telemetry |
| Sperm whale diet share | 0% → 12.1% → 26.5% → 82.2% by region/individual and metric | genuinely heterogeneous |
| Global specimen count | ~339 (implied 2004) · 677 (2011) · "nearly 500 since 1547" (attributed to Sweeney & Roper) · 836 (2026, weak venue) | order of magnitude: hundreds |
| NE Atlantic share | 115 specimens = 33.9% (Guerra & González 2004) vs regional tallies in Guerra et al. 2011 (e.g., 152 for N Spain alone) | likely different dates/definitions; not forced into consensus |
| 2006 animal size | 3.5 m/50 kg (most outlets) vs "24 ft/7 m" (some outlets) | press-only; both reported |
| Nominal species count | 18 (Roeleveld & Lipinski 1991) vs ~21 (Winkelmann 2013 press) vs "8 commonly cited" (untraceable to a primary authority) | stated as 18–21 |

## 8. Known gaps and inaccessible sources

Sources this review could not reach at all, whose absence limits precision: Steenstrup's original 1857 Danish text and his posthumous papers; Verrill's monograph tables; Kirk (1888) in the original; Förch (1998) beyond citations; Clarke (1980, *Discovery Reports* 37); R. Clarke (1955); the *Comptes Rendus* (1861) *Alecton* communication; Bullen (1898), Lee (1883), Heuvelmans, and Pontoppidan at page level; primary US Navy documentation of the USS *Stein* incident (existence itself unestablished); the full texts of essentially all modern papers (abstract-level verification only); and current-state museum pages (NHM, Smithsonian, Te Papa, NHMD accession details). The open bibliographic questions arising from these gaps are listed in `unresolved-questions.md` §12.

## 9. Residual limitations of the completed review

1. **Abstract-level verification ceiling.** A claim confirmed "verbatim in the abstract" is strong; body-text facts inherit one layer of unverifiability. The ledger's confidence column reflects this.
2. **Press dependence at two milestones.** The 2006 and 2012 events — including all quantitative details of the first deep-habitat video — rest on journalism because no peer-reviewed account exists. This is a deficiency of the scientific record itself, but it means those numbers could not be hardened here.
3. **Search-language bias.** Searching was conducted in English (with incidental Spanish/Danish items). Japanese-language primary documentation — likely substantial for the 2002 Kyoto event, the 2006/2012 expeditions, and Sea of Japan records — was not directly accessed; some "unlocated primary record" flags may reflect this rather than true absence.
4. **Recency horizon.** Events after mid-2026 are outside this review; the December 2025 feeding video and the 2026 eDNA and parasitology papers were the newest items assessed.
5. **Single-index dependence for verification.** With Crossref and publishers unreachable, verification leaned on one scholarly index (Consensus/Semantic Scholar). Its coverage gaps (pre-digital monographs, museum gray literature, press) map directly onto the 43 "could not verify" outcomes, and its occasional metadata corruption (OCR-garbled author fields for two old papers) had to be detected and worked around by content-matching.
6. **No original measurements or reanalysis.** This is a literature audit; it adjudicates provenance and consistency, not biology. Where the field disagrees (lifespan, depth, maximum size, hunting mode, kraken origins, seismic strandings), this review preserves the disagreement — its contribution is the map of what is known, at what strength, from which sources.
