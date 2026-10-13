# Glycosylated EGFR–Cetuximab Molecular Dynamics

This folder documents the GROMACS workflow for a glycosylated EGFR–Cetuximab complex.

## Recorded analysis
- GROMACS 2025.4
- A recorded run: 50,000 steps / 100 ps
- Backbone RMSD, residue-level RMSF, and radius of gyration were analyzed.

## Analysis commands recorded
```bash
gmx rms -s md.tpr -f md.xtc -o rmsd_backbone.xvg
gmx rmsf -s md.tpr -f md.xtc -o rmsf_backbone.xvg -res
```

Copy the actual `.xvg` outputs and plot images into `../figures/` when available. Add the exact radius-of-gyration command and the group selections from the original terminal history. A 100 ps trajectory is short and supports only exploratory interpretation.
