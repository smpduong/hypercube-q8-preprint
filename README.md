# Local identifying codes in the 8-cube

Companion material to Steven Minh Phat Duong, **A Share-Deficit Bound and a
40-Word Local Identifying Code in the 8-Cube** (2026).
Published preprint: https://doi.org/10.5281/zenodo.24335625

## Result and limits
The paper gives **36 ≤ Mᴸ(8) ≤ 40**, not an exact value. Here a local
identifying code dominates all vertices and distinguishes adjacent vertices;
it need not distinguish every pair. The explicit 40-word witness establishes
the upper bound. The lower bound is the paper's mathematical share-deficit
argument, not a consequence of running this verifier. AI-assisted preprint;
not independently human-reviewed or formally verified.

## Reproduce the witness check
Python 3, standard library only; no downloads, solvers, credentials or network:
```sh
python3 check_witness.py
python3 -m unittest discover -s tests -v
python3 -O -m unittest discover -s tests -v
```
Expected: 40 codewords, 256 covered vertices, 1024 separated edges, PASS.
The witness SHA-256 must match the checked-in witness-check.json.
The checker uses explicit exceptions, so validation remains active with -O.

The PDF and TeX are unchanged copies of the corrected preprint.
To build the TeX, use pdfLaTeX twice with the standard geometry, amsmath,
amssymb, amsthm, booktabs, hyperref and listings packages. The checked-in PDF
is the authoritative published-version artifact; byte-identical rebuilding
is not promised.

## Scope
This is a curated, history-free Q8 companion snapshot. It deliberately excludes
the larger research repository's Q6/Q7/Q9/Q10 experiments, SAT certificates,
private review material, solver logs and bundled third-party archives.
It is not a complete reproduction of those separate projects.

Code is MIT-licensed; the preprint and text/data retain CC BY 4.0.
See LICENSE, PROVENANCE.md, RIGHTS.md and SHA256SUMS.txt.
The wider original research repository remains separate and private.
