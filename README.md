# Molecular Docking & Molecular Dynamics of Protein Systems

A portfolio project documenting two structural-bioinformatics workflows: (1) HIV-1 protease–ligand docking preparation and inspection, and (2) molecular-dynamics (MD) analysis of a glycosylated EGFR–Cetuximab system using GROMACS.

> **Reproducibility note:** This repository is a curated project record. It does not claim that all workflows are fully reproducible from the files currently included. Add the actual input structures, configuration files, scripts, plots, and output summaries you retained before describing this as a complete reproducible workflow.

## Project 1 — HIV-1 Protease Docking

- **Target structure:** HIV-1 protease, PDB ID **1HSG**
- **Ligand noted during the workflow:** MK-1
- **Tools used:** AutoDock Vina, Meeko, PyMOL
- **Activities documented:** receptor/ligand inspection, receptor preparation, binding-pocket inspection, and docking workflow exploration.

### Add the actual project artifacts
Place retained scripts, preparation settings, and small text outputs in `hiv1_protease_docking/`. If available, document the exact Vina version, search-box center and dimensions, exhaustiveness, scoring output, and preparation commands. Do not invent docking scores or binding-affinity values.

## Project 2 — EGFR–Cetuximab Molecular Dynamics

- **System:** glycosylated EGFR–Cetuximab complex
- **Simulation software:** GROMACS 2025.4
- **Analysis:** backbone RMSD, residue-level RMSF, and radius of gyration
- **Recorded simulation setup:** 50,000 steps / 100 ps for the run described in the project notes.
- **Tools mentioned:** GROMACS, CHARMM36 glycan-related force-field files, PyMOL, Python/Matplotlib for plotting.

The recorded analysis commands included:

```bash
gmx rms -s md.tpr -f md.xtc -o rmsd_backbone.xvg
gmx rmsf -s md.tpr -f md.xtc -o rmsf_backbone.xvg -res
```

For radius of gyration, include the exact command and group selection from your own terminal history if you still have it. The original `.xvg` files and plots should be copied into `figures/` when available.

### Interpretation caution
A 100 ps simulation is a short exploratory run. RMSD, RMSF, and radius of gyration can describe the sampled trajectory, but this duration alone does not establish long-timescale stability, binding affinity, or biological efficacy.

## Repository structure

```text
.
├── README.md
├── DATA_AND_REPRODUCIBILITY.md
├── .gitignore
├── hiv1_protease_docking/
│   └── README.md
├── egfr_cetuximab_md/
│   ├── README.md
│   └── scripts/
│       └── plot_gromacs_xvg.py
└── figures/
    └── README.md
```

## How to reproduce / extend

1. Add the exact PDB/structure inputs and document their source and any modifications.
2. Add the retained docking preparation commands, Vina configuration, and result logs.
3. Add the actual GROMACS `.mdp` files and topology-generation notes.
4. Add the small `.xvg` analysis outputs and plots.
5. Record software versions and commands in `DATA_AND_REPRODUCIBILITY.md`.
6. Re-run commands in a suitable environment before claiming end-to-end reproducibility.

## Limitations

- Raw simulation trajectories and checkpoint files are not included in this starter package.
- Exact docking scores, box settings, force-field parameters, and trajectory-derived numerical results are not stated here because they must be verified from the original output files.
- This repository documents a learning/research workflow and should not be interpreted as clinical or therapeutic evidence.
