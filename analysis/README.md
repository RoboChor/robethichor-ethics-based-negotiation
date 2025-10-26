# RobEthiChor: automated context-aware ethics-based negotiation for autonomous robots

This folder contains the files for the analysis (and its results) of the collected logs from the running of the experiments.

## Experiment data analysis

> [!NOTE]
> Outputs are attached within the files: it is no needed to run them to read the analysis results.
>
> To run again analysis files (even though not required), the following dependencies are required (Conda environment management is recommended):
> - Python 3
> - Jupyter
> - Pandas
> - Numpy
> - Matplotlib
> - Seaborn
> - Sklearn

### Deployment comparison
`deployment-comparison.ipynb` contains a comparative analysis of the negotiation times measured for the scalability experiments in the _on-robot_ and _off-robot_ with profiles containing up to 100 dispositions. The analysis is performed in the context of _EQ3_

**Result logs analysed:** `scalability-offrobot.log`, `scalability-onrobot.log`.

Paper reference: Section 7.2, description of Table 2.

### Log comparison
`log_comparison.ipynb` compares the logs obtained in the simulated scenarios for results consistency. The analysis is performed in the context of _EQ2_.

**Result logs analysed:** `simulation-airport-offrobot.log`, `simulation-airport-onrobot.log`, `simulation-hospital-offrobot.log`, `simulation-hospital-onrobot.log`.

**Paper reference:** Section 7.1, comments on negotiation results.

### Ping analysis
`ping_analysis.py` extracts overall stats for the network latency. The analysis is performed in the context of _EQ2_ and _EQ3_.

**Result logs analysed:** `ping_results.txt`.

**Paper reference:** Section 7, experimentation setting description.

### Scalability analysis
`scalability-offrobot-analysis.ipynb` and `scalability-onrobot-analysis.ipynb` contain the analysis on the performance scalability of the negotiation approach. The analysis is performed in the context of _EQ3_.

**Result logs analysed:** `scalability-offrobot.log` and `scalability-onrobot.log`.

**Paper reference:** Section 7.2, Figures 8, 9, 10, and 11, regression analysis commentary.

### Simulation analysis
`simulation_analysis.ipynb` contains the analysis of the results of the negotiation scenarios. The analysis is performed in the context of _EQ1_ and _EQ2_.

**Result logs analysed:** `simulation-airport-offrobot.log`, `simulation-airport-onrobot.log`, `simulation-hospital-offrobot.log`, `simulation-hospital-onrobot.log`.

**Paper reference:** Section 7.1, Figures 6 and 7.