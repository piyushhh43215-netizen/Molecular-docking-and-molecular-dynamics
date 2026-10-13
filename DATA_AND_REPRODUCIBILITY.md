# Data and Reproducibility

This document records known workflow details and lists what should be recovered from the original working directory before the project is considered fully reproducible.

## HIV-1 protease docking

Known from the project notes:
- Target PDB: `1HSG` (HIV-1 protease)
- Ligand label used in the workflow: `MK-1`
- Tools: AutoDock Vina 1.2.7, Meeko 0.8.0, PyMOL
- Receptor preparation was explored using Meeko utilities.

To complete this record, add:
- Original structure source and exact input filename
- Any chain/residue selections and treatment of waters/heteroatoms
- Receptor and ligand preparation commands
- Vina search-box center and dimensions
- Vina options such as exhaustiveness and number of modes
- Exact output score(s) copied from the Vina log
- Software versions and operating system

Do not report docking scores from memory; use the saved Vina output/log.

## EGFR–Cetuximab molecular dynamics

Known from the project notes:
- GROMACS version: `2025.4-Ubuntu_2025.4_1`
- A recorded MD run used 50,000 steps and a nominal total time of 100 ps.
- Files previously produced included `md.tpr`, `md.xtc`, `md.edr`, `md.log`, `md.gro`, and `md.cpt`.
- Analysis was performed for backbone RMSD, residue-level RMSF, and radius of gyration.
- The glycosylated system used CHARMM36-related glycan force-field files.

Commands recorded:
```bash
gmx mdrun -deffnm md -v -ntmpi 1 -ntomp 12
gmx rms -s md.tpr -f md.xtc -o rmsd_backbone.xvg
gmx rmsf -s md.tpr -f md.xtc -o rmsf_backbone.xvg -res
```

To complete this record, add:
- Exact topology and `.mdp` files used
- System preparation steps, box/solvation/ionization settings
- Equilibration protocol and restraints
- Exact group selections for analysis
- The exact radius-of-gyration command
- `.xvg` files and plots, with axes/units
- Any warnings/errors from the GROMACS log that affect interpretation

## Files recommended for GitHub

Good candidates:
- `*.mdp`, small text scripts, `.xvg` outputs, `*.pdb` inputs where redistribution is permitted, plots (`.png`), and README documentation.

Usually exclude:
- Large trajectories (`*.xtc`, `*.trr`), checkpoint files (`*.cpt`), temporary structures, generated caches, environment folders, credentials, and private files.

If large data files are necessary, document how to obtain them or use a suitable large-file/data repository rather than committing them directly.

## Scientific interpretation

The recorded 100 ps MD run is an exploratory short simulation. Do not claim the system is equilibrated or stable based only on this short run. Report the actual observed plots and numeric summaries, including limitations.
