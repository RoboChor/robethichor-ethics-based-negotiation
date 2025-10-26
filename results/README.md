# RobEthiChor: automated context-aware ethics-based negotiation for autonomous robots

This folder contains the raw data obtained from experiments as a set of log files.

## Experiment results data

### Ping reults
The file `ping_results.txt` contains the results of ping messages sent during the experimentation to monitor the network latency for robot-to-robot messaging
These data where collected during the execution of simulation and scalability tests.

### Scalability tests
The files `scalability-offrobot.log` and `scalability-onrobot.log` contain the logged negotiation results for the scalability experiments in the _off-robot_ and _on-robot_ setting, respectively. The files are collected in the context of the experiments for _EQ3_.

Each log line has the form:

`/robassistant_XX: negotiation completed. Configuration: {"goal": "<N> dispositions, <P> activated conditions, ethicprofile no. <i>. Test counter: <j>"}. Negotiation time: <T> seconds. Rounds: <R>. Result: winner/loser/no-agreement`

### Simulation
The files `simulation-[airport/hospital]-offrobot.log` and `simulation-[airport/hospital]-onrobot.log` contains the logged negotiation results for the negotiation scenarios in the airport and hospital context in the _off-robot_ and _on-robot_ setting, respectively. The files are collected in the context of the experiments for _EQ1_ and _EQ2_

Each log line has the form:
`/robassistant_XX: negotiation completed. Configuration: {"goal": "navigate_to_gate (User: <X>, Negotiating against: <Y>)"}. Negotiation time: <T> seconds. Rounds: <R>. Result: winner/loser/no-agreement`

The log reports the result of the negotiation of between the personas `<X>` and `<Y>`, seen from the point of view of `robotassistant_<XX>`, which is acting on the behalf of `<X>`.