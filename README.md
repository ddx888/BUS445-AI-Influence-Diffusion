# Influencer Identification & Diffusion Simulation for AI Product Adoption

**BUS 445 Advanced Business Analytics** · Farmingdale State College · Fall 2026

**Instructor:** Professor Bruno G. Kamdem

**Group:** Luigi Scolieri, Daniel Pineda, Ben Nosovitch, Mickaela Wright

## Overview

When a business launches a new AI product, who should hear about it first? This project tests whether choosing three starting participants by their network position (degree, betweenness, or eigenvector centrality) spreads information to more students than choosing three at random.

- **Data:** an original survey of 18 Farmingdale State College students (AI use, sharing habits, and which other participants they talk with about AI). Participants are identified by codes only.
- **Networks:** two undirected, unweighted networks built from the 40 contact nominations: a *mutual report* baseline (both students name each other, 11 connections) and an *either report* comparison (at least one student names the other, 29 connections).
- **Simulation:** an Independent Cascade model at assumed transmission probabilities of 10%, 25%, and 50%, with 10,000 runs per network, strategy, and probability.

The full write-up is in `Final_Report.docx`.

## Files in this repository

| File | What it does |
|---|---|
| `environment.yml` | Conda environment (Python 3.12.14 and all required packages) |
| `form.xlsx` | Survey data. **Required by all three scripts** |
| `project.py` | Builds the directed nomination network and writes a per-participant summary (nominations made and received) to `AI_Network_Summary.xlsx` |
| `project2.py` | Builds the mutual and either-report networks and prints their characteristics (density, average degree, components, isolates) |
| `project3.py` | Centrality analysis, seed selection, Independent Cascade simulation, paired comparisons against random selection, tables, and figures |
| `Final_Report.docx` | Final written report (placeholder until the finalized version is uploaded) |
| `results/` | Output files created by `project3.py` |

## Setup

1. **Put everything in one folder.** Download or clone this repository so that `form.xlsx`, `environment.yml`, and the three `.py` scripts sit together in the same folder (for example, a folder named `BUS445_Project`). The scripts look for `form.xlsx` next to themselves, so it must stay in the same folder as the scripts. It does not matter where on your computer the folder lives.

2. **Open Anaconda Prompt.**

3. **Create the environment** from the provided file:
   ```
   conda env create -f environment.yml
   ```

4. **Activate it:**
   ```
   conda activate bus445_project
   ```

If an environment named `bus445_project` already exists on your machine, either remove it first (`conda env remove -n bus445_project`) and repeat step 3, or update it with `conda env update -f environment.yml --prune`.

**Software versions used:** Python 3.12.14, NumPy 2.3.5, NetworkX 3.5, Matplotlib 3.10.8, pandas 3.1.1, openpyxl 3.1.5, IPython 9.18.1, ipykernel 7.4.0.

## Running the code

The scripts are independent of each other, so they can be run in any order. In VS Code, open the folder and select the `bus445_project` interpreter (Ctrl+Shift+P, then "Python: Select Interpreter") before running.

### What a correct run looks like

`project2.py` should print 40 total nominations and:

| | Mutual report | Either report |
|---|---|---|
| Connections | 11 | 29 |
| Density | 0.0719 | 0.1895 |
| Average degree | 1.2222 | 3.2222 |
| Connected components | 8 | 3 |
| Largest component | 10 | 16 |
| Isolated participants | 6 | 2 |

`project3.py` should begin with:

```
either_report participants: 18 connections: 29
mutual_report participants: 18 connections: 11
Directed nominations: 40
Simulation checks passed
```

and finish with `All model checks passed.` Mean reach at a 50% transmission probability should be:

| Network | Degree | Betweenness | Eigenvector | Random |
|---|---|---|---|---|
| Either report | 11.2582 | 11.3450 | 11.2348 | 12.3593 |
| Mutual report | 5.8663 | 5.9705 | 4.9315 | 5.6742 |

Reach includes the three starting participants.

## Outputs

`project.py` saves `AI_Network_Summary.xlsx` in the project folder. `project3.py` creates a `results/` folder in the project folder containing:

| File | Contents |
|---|---|
| `mutual_report_edges.csv`, `either_report_edges.csv` | Edge lists for each network |
| `centrality.csv` | Degree, betweenness, and eigenvector scores for every participant in both networks |
| `simulation_summary.csv` | Mean reach, standard deviation, and 95% interval for each network, probability, and strategy |
| `paired_comparisons.csv` | Each centrality strategy's difference from random selection, with paired 95% intervals |
| `simulation_runs.csv` | Every individual simulation run (about 13 MB; regenerated each time `project3.py` runs, so it is not tracked in git) |
| `metadata.json` | Random seed, run counts, network statistics, seed sets, and software versions |
| `*_network.png` | Network drawings (one per network definition) |
| `*_reach.png` | Average reach by strategy and transmission probability (one per network definition) |

## Reproducibility notes

- Random seed: **4452026**. Runs per configuration: **10,000**. Transmission probabilities: **0.10, 0.25, 0.50**.
- These settings are defined inside `project3.py`. Command-line flags are not used.
- Random seed streams are fixed, so rerunning with the same package versions reproduces the numbers above.
- The `display(...)` image lines at the end of `project3.py` show nothing when run from a terminal. The same figures are saved as PNG files in `results/`, so open them from there.
- Transmission probabilities are assumptions, not values estimated from the survey. Reach is a simulated outcome, not observed adoption.

## AI use disclosure

Per the course guidelines, AI assistance used for the items below is listed here. Claude (Anthropic) was used as follows:

| Area | How AI was used |
|---|---|
| Environment | Guidance on creating, checking, and sharing the conda environment (`environment.yml`). |
| This README | Drafted with Claude and reviewed by the group. |