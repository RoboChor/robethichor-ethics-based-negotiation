# RobEthiChor: automated context-aware ethics-based negotiation for autonomous robots
Replication package for the paper **RobEthiChor: automated context-aware ethics-based negotiation for autonomous robots**

## Authors
This study has been designed, developed, and reported by the following investigators:
- Mashal Afzal Memon (University of L'Aquila, Italy)
- Gianluca Filippone (Gran Sasso Science Institute, Italy)
- Gian Luca Scoccia (Gran Sasso Science Institute, Italy)
- Marco Autili (University of L'Aquila, Italy)
- Paola Inverardi (Gran Sasso Science Institute, Italy)

## Repository Structure
```
towards-uncertainty-aware-bts
|   README.md                               # This file
|   LICENSE                                 # License file
├---analysis                                # Jupyter Notebook files for the results analyis
├---results                                 # Raw log files from the experimentation
└---ros_ws                                  # ROS 2 workspace with RobEthiChor
|   └---src
|       ├---robethichor                     # RobEthiChor ROS 2 package
|       └---robethichor_interfaces          # ROS 2 package for RobEthiChor services interfaces
└---run                                     # Experimental settings and experiment running facilities
    ├---scalability_experiments
    |   |   run_experiment.bash             # Script for running scalability experiments
    |   |   generate_test_cases.py          # Test cases generation script
    |   └---test_cases                      # Test cases used in the paper
    └---simulation
        |   disposition_activation.json     # Scenario-related disposition activation configuration
        |   echical_implications.json       # Scenario-related task ethical implication model
        |   run_usecase.bash                # Script for running airport negotiation scenarios
        ├---airport
        ├---hospital
        └---personas
            |   personas.pdf                # Personas description
            |   ground_truth.xlsx           # Ground thruth expected data and negotiations outcome observation
            └---[A-J]                       # Personas profiles and status implementation
```

## Study Results & Analysis

### Collected data
Raw data obtained from experiments are contained in the `results/` folder as a set of log files:
- `ping_results.txt` contains the results of ping messages sent during the experimentation to monitor the network latency for robot-to-robot messaging
- `scalability-offrobot.log` contains the logged negotiation results for the scalability experiments in the _off-robot_ setting
- `scalability-onrobot.log` contains the logged negotiation results for the scalability experiments in the _on-robot_ setting
- `simulation-[airport/hospital]-offrobot.log` contains the logged negotiation results for the negotiation scenarios in the airport and hospital context in the _off-robot_ setting
- `simulation-[airport/hospital]-onrobot.log` contains the logged negotiation results for the negotiation scenarios in the airport and hospital context in the _on-robot_ setting

### Data analysis
Log analysis and results are contained in the `analysis/` folder as a set of Jupyter Notebook files.

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

#### Deployment comparison
`deployment-comparison.ipynb` contains a comparative analysis of the negotiation times measured for the scalability experiments in the _on-robot_ and _off-robot_ with profiles containing up to 100 dispositions.

**Result logs analysed:** `scalability-offrobot.log`, `scalability-onrobot.log`.

Paper reference: Section 7.2, description of Table 2.

#### Log comparison
`log_comparison.ipynb` compares the logs obtained in the simulated scenarios for results consistency.

**Result logs analysed:** `simulation-airport-offrobot.log`, `simulation-airport-onrobot.log`, `simulation-hospital-offrobot.log`, `simulation-hospital-onrobot.log`.

**Paper reference:** Section 7.1, comments on negotiation results.

#### Ping analysis
`ping_analysis.py` extracts overall stats for the network latency.

**Result logs analysed:** `ping_results.txt`.

**Paper reference:** Section 7, experimentation setting description.

#### Scalability analysis
`scalability-offrobot-analysis.ipynb` and `scalability-onrobot-analysis.ipynb` contain the analysis on the performance scalability of the negotiation approach.

**Result logs analysed:** `scalability-offrobot.log` and `scalability-onrobot.log`.

**Paper reference:** Section 7.2, Figure 7, 8, 9, and 10, regression analysis commentary.

#### Simulation analysis
`simulation_analysis.ipynb` contains the analysis of the results of the negotiation scenarios.

**Result logs analysed:** `simulation-airport-offrobot.log`, `simulation-airport-onrobot.log`, `simulation-hospital-offrobot.log`, `simulation-hospital-onrobot.log`.

**Paper reference:** Section 7.1, Figure 5 and 6.


## Experiment replication

### Requirements
- Ubuntu 22.04
- ROS 2 Humble
- ROS dev-tools
- Rosdep

### Download and installation
Download the repository:
```
git clone https://github.com/RoboChor/robethichor-ethics-based-negotiation.git
```

Build the ROS package:

> [!NOTE]
> Rosdep must be installed and initialized before building the ROS package.
> Install Rosdep:
> ```
> sudo apt-get update
> sudo apt-get install python3-rosdep
> ```
>
> Initialize Rosdep:
> ```
> sudo rosdep init
> rosdep update
> ```

```
cd robethichor-ethics-based-negotiation/ros_ws
rosdep install --from-paths src -y --ignore-src
colcon build
```

> [!IMPORTANT]
> RobEthiChor must be deployed on the machine that will execute it. To test the _on-robot_ deployment, clone the repository or move the `ros_ws/` folder on the robot before installing dependencies and building the ROS packages.
>
> Alternatively, RobEthiChor can be built locally and then moved on the target machine (e.g., if dev-tools are not available). In this case, move the whole workspace folder after running `colcon build` locally:
> ```
> scp . user@host:/path/to/ros_ws
> ```
> Then, `cd` into the moved `ros_ws/` folder in the target machine and reinstall the dependencies using Rosdep (install and init if required as shown above):
> ```
> sudo apt-get update
> rosdep install --from-paths src -y --ignore-src
> ```

### Running experiments

The `run/` folder contains the experimental settings and the scripts required to run them. They must be run outside of the robots despite of the chosen deployment setting.

The files `run_usecase.bash` and `run_experiment.bash` provides support for launching the experiments. Documentation on the parameters can be found within them.

#### Negotiation Scenarios
Configuration and running facilities can be found in the `simulation/` folder.

##### *off-robot* scenario:
```
cd ../run/simulation
chmod +x run_usecase.bash
./run_usecase.bash --launch true --context <airport/hospital>
```
Two terminals will open, each for one of the two robots. Log files will be stored inside the newly created `simulation/results/` folder.

##### *on-robot* scenario:

Deploy RobEthiChor on the two negotiating robots as explained above, and copy the `usecases/disposition_activation.json` and `usecases/ethical_implications.json` files inside the robot's `ros_ws/` folder:
```
cd ../run/simulation
scp disposition_activation.json user@host:/path/to/ros_ws
scp ethical_implications.json user@host:/path/to/ros_ws
```

Then, from the robot's `ros_ws/` folder, run:
```
. install/setup.bash
ros2 launch robethichor robethichor_launch.py ns:=[ROBOT_NAME] port:=[ROBOT_PORT] ethical_implication_file:=/path/to/ros_ws/ethical_implications.json disposition_activation_file:=/path/to/ros_ws/disposition_activation.json log_output_file:=/path/to/ros_ws/negotiation_results.log
```

> [!IMPORTANT]
> Substitute `ROBOT_NAME` and `ROBOT_PORT` with the name of each of the robots (e.g., _robassistant_1_ and _robassistant_2_) and the robot's connector port (e.g., _5000_ and _5001_)

Finally, run the scenarios from the computer:
```
chmod +x run_usecase.bash
./run_usecase.bash --names <robot1_name> <robot2_name> --hosts <robot1_host> <robot2_host> --ports <robot1_port> <robot2_port>
```
> [!IMPORTANT]
> Substitute parameters according to the configurations provided to the launched robots. `robot1_host` and `robot2_host` must contain the IP addresses of the two robots.

Log files will be stored inside the newly created `results/` folder within the robot's `ros_ws/` folder.

#### Scalability Experiments
Configuration and running facilities can be found in the `scalability_experiments/` folder.

> [!NOTE]
> Test cases used for running experiments are already contained into the repository.
> To generate new test cases, use the `generate_test_cases.py` python script:
> ```
> python3 generate_test_cases --n <N> --p <P> --c <NUMBER_OF_CASES>
> ```

##### *off-robot* scenario:
```
cd ../run/scalability_experiments
chmod +x run_experiment.bash
./run_experiment.bash --launch true
```
Two terminals will open, each for one of the two robots. Log files will be stored inside the newly created `scalability_experiments/results/` folder.

> [!NOTE]
> The script `run_experiment.bash` will prompt, before running each configuration, the wait times between each negotiation so to avoid overlapping different negotiations.

##### *on-robot* scenario:

Deploy RobEthiChor on the two negotiating robots as explained above, and copy the `test_cases/disposition_activation.json` and `test_cases/ethical_implications.json` files inside the robot's `ros_ws/` folder:
```
cd ../run/simulation
scp scalability_experiments/test_cases/disposition_activation.json user@host:/path/to/ros_ws
scp scalability_experiments/test_cases/ethical_implications.json user@host:/path/to/ros_ws
```

Then, from the robot's `ros_ws/` folder, run:
```
. install/setup.bash
ros2 launch robethichor robethichor_launch.py ns:=[ROBOT_NAME] port:=[ROBOT_PORT] ethical_implication_file:=/path/to/ros_ws/ethical_implications.json disposition_activation_file:=/path/to/ros_ws/disposition_activation.json log_output_file:=/path/to/ros_ws/negotiation_results.log
```

> [!IMPORTANT]
> Substitute `ROBOT_NAME` and `ROBOT_PORT` with the name of each of the robots (e.g., _robassistant_1_ and _robassistant_2_) and the robot's connector port (e.g., _5000_ and _5001_)

Finally, run the scenarios from the computer:
```
chmod +x run_experiment.bash
./run_experiment.bash --names <robot1_name> <robot2_name> --hosts <robot1_host> <robot2_host> --ports <robot1_port> <robot2_port>
```
> [!IMPORTANT]
> Substitute parameters according to the configurations provided to the launched robots. `robot1_host` and `robot2_host` must contain the IP addresses of the two robots.

Log files will be stored inside the newly created `results/` folder within the robot's `ros_ws/` folder.