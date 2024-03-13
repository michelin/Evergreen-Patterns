---
title: "Continuous Operability"
date: 2022-04-12T16:12:21+02:00
draft: false
categories:
- running
tags:
- running
description: "My team continually improves its operations based on system health, root cause analysis, and knowledge"
interact_with: "toil_routine, normal_errors, snowball_effect, everything_works_all_the_time"
---


# MAIN PURPOSE

Like every pattern it is key. But it has the particularity of ensuring that the approach and effort remains consistent & constant over time (duration being the key point)

Systems are living. They evolve with the changes implemented, the users usage changes, the businesses evolve....

It is a continuous loop that needs to be put in place



# GOAL

The effort of operability is a continuous work (not only during the building of a solution). The business evolves, the usage evolves, the systems evolve, the data evolve : all these changes require ensuring the right level of satisfaction.

Take a step back at regular frequencies (each month ideally or at least every year).

Take the time to understand the situations encountered, the difficulties faced. Continue to identify the levers that can be activated to

And above all, take the time to prepare, to anticipate the future by making sure that new or missing drivers are available in time.



Without this regular work, performance can deteriorate, components can become obsolete, maintenance more important,...



# WHAT NEED TO BE DONE

The practice is to organize regular meetings with all the stakeholders to enable them to take a step back.

In order to achieve this, the team must have:

* The events of the period, how they were handled (RCA reviews)

* The capacity plan for the coming period.

* The challenges of the teams

* Feedback from users

* Operation figures

* Additional ad hoc studies can be added



All of these elements should make it possible to establish an action plan to improve the operability of the solutions. This may concern the solution itself or the way the support is implemented. The whole pattern set can be used


# EXAMPLES

During a moment of step back, the team analyzes the various incidents identified through the implementation of the observability pattern. Several distinct cases are then isolated as:



A cluster concerning flows with errors when sending data to the EDI system => The team decide to implement the Circuit Breaker pattern



A cluster concerning data errors => the Event and Time is Precious pattern is then set up for the treatment of this case until the problem is implemented.


# REAL MICHELIN WORLD

Ex:  
