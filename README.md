# CIKR Design Basis Examples

A public site showing one worked design basis example for each critical infrastructure sector: the sector framework, one facility class, one use case (summary card only) and one real reference event. Owned by Project 0 (Cross-Project Alignment) of Tim Roxey's *Design Basis for AI Governance in Critical Infrastructure* (Eclectic Technologies).

Every document the site links to is frozen in *CIKR Design Basis Examples, Edition 1 (November 2026)*, version DOI 10.5281/zenodo.23863986, concept DOI 10.5281/zenodo.23863985. The PDFs are served from the publications mirror at `scubanuke.github.io/publications/cikr/edition-1/`. No use case is published; use cases are available to defenders and regulators on request.

## How the site is built

The HTML at the repository root is generated. Edit the sources in `content/` and run `python3 tools/build.py` from the repository root.

`content/cards/` holds the public text of the sector cards, copied from Project 0's card drafts with the checker notes removed. `content/facility_classes.json` holds each sector's other facility classes, titles only, generated from the DBA Facility Class Register; it is not part of the frozen edition. `content/readers.json`, `content/pages.json` and `content/glossary.json` hold the reader pages, the fixed pages and the glossary. `assets/figures/` holds the two figures; `tools/make_layers_figure.py` draws the simplified design basis layers figure.

Two switches at the top of `tools/build.py` matter. `DRAFT_BANNER` shows the review banner and is turned off at launch. `MASTER_DRAFT_LIVE` adds the master draft page and its links once Project 2 deposits the master draft; fill `MASTER_DRAFT_DOI` and `MASTER_DRAFT_CHAPTERS` at the same time.

Text and documents are licensed CC BY 4.0.
