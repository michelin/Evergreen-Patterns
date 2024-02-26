---
title: "Self Healing"
date: 2022-04-12T16:03:10+02:00
draft: false
categories:
- running
description: "My systems react automatically to an event or make users autonomous to minimize request to operations"
interact_with: "toil_routine, hero_problem_solving"
---


# MAIN PURPOSE

The main expectation is to provide an automatic resolution to an identified situation.

The automation will be triggered by:

- an identified event (via monitoring or directly by the system).

- a direct request from a user of the system (solicitation)The solution must allow to answer all or part of the situation as soon as possible. This automatic resolution must also be tracked in the tools to allow for analysis and reporting.

# GOAL

Self-Healing offers many benefits:

- Improved QoS by addressing situations before user disruption

- Ability to have 24/7 support

- Fast response and consistent quality.

- Reduction of the recurring workload for the support teams (often toil)

- Reduction of support costs



# WHAT NEEDS TO BE DONE

**For Event from monitoring**

Providing a self-healing solution with event requires:

* Having observability / monitoring in place.

* Having a defined Run Book in order to have the diagnosis and the remediation actions

* Automating the run book use cases.

**For User solicitation**

Providing a self-healing solution to users requires:

* Knowing your users and their expectations to identify the most appropriate channel

* Having a conversational solution with users (chatbot, callbot, search engine, ...)

* Implementing scenarios to establish a diagnosis and identify the most appropriate solution



All actions must be tracked in an ITSM tool to ensure traceability, reporting and analysis.

Note that a use case treated as part of a self-healing approach is eligible for problem management in order to eradicate the given situation.


# EXAMPLES

**For Event**



An alert was issued by the monitoring tools following a data transfer error.

This documented event triggers a remediation scenario that will:

- Attempt to send the data again within a few minutes.

- If the transfer still fails, it will use an alternative protocol

- A communication is sent to support team & users



For User solicitation



Implementation of a chatbot for a defined population of users allowing to treat a large part of the user's requests:

* How to use the solution

* Re-initialize your password.

* Request a mass data integration.


The conversational AI tool allows to identify the user's request and deliver the expected solution via its knowledge base or automated cases. 

 

  
