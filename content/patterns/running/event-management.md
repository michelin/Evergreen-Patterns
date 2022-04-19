---
title: "Event Management"
date: 2022-04-12T16:11:58+02:00
draft: true
family: running
---


# MAIN PURPOSE

In order to always anticipate and solve situations before they disturb the users, event management is essential.

To be clear : an event is simply a change to the state of a service, a threshold is breached, or configuration item (CI) that is significant to its management.



# GOAL



The objective is simple: to have the information as soon as possible to provide a solution as quickly as possible. It also avoids mobilizing teams to scan the monitoring screens.



It is simple but requires :

 * knowledge of the system to identify what is the subject of an event.

 * Knowledge of the cases and actions to be taken (Run Book)



It is the starting point of a self-remediation chain (pattern Self-healing) by triggering an automated scenario following an event (Pattern Event Management & Time is precious).



# WHAT NEED TO BE DONE

The implementation starts by identifying the situations we want to monitor (The implementation is based on the observability pattern).

For each cases, the team identify:

* The thresholds (static or dynamic).

* Which team is the most appropriate

The procedure to apply

All informations is regrouped in a document : Run Book

After setting implemented, it is necessary to monitor the evolution over time and to ensure:

* That the thresholds are still consistent with reality.

* hat the applicable procedures are still compatible with the system in place.



This mechanism is particularly adapted for the management of flows.



All event must be tracked in an ITSM tool to ensure traceability, reporting and analysis.

The implementation can be based on AI/machine learning tools for the determination of thresholds in a dynamic way.

Note that a use case treated as part of a automation, knowledge,.. approach is eligible for problem management to eradicate the situation.


# EXAMPLES

All the flows allowing a planning application are monitored. In case of absence at a specific time, a volume of inconsistent data or an integration error are all situations that can give rise to an event. The rapid treatment before the users notice the disturbance allows to maintain a high level of Quality of Service.

# REAL MICHELIN WORLD

Ex:  
