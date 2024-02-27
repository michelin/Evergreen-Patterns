---
title: Change Aversion
date: 2024-02-24T05:50:18.124446284Z
draft: false
status: reviewed
model: llama2:13b
categories: 
 - anti-pattern
tags: 
 - change
 - people
 - mtbf 
description: "Changing systems in production is risky so I avoid it at all cost."
---

# Description

The Change Aversion anti-pattern describes the tendency to avoid making changes to systems in production at all costs, due to the perceived risk of disrupting the system or causing unintended consequences. This can lead to a reluctance to adopt new technologies, fix bugs, or make improvements to the system, resulting in stagnation and decreased efficiency.

It is a conviction: do not evolve, improve, or change anything in a system because it works. 
*if it's working don't fix it* 
We now know that the result is an illusion. 
 
The system is living and needs regular attention: 
- to adapt it to the reality of business volumes 
- to update it regularly in terms of security and obsolescence 
- to modify the components that have defects 
- to adapt the system to regulatory requirements 
- to improve its operability based on RCAs, PRB, and feedbacks 
- ...

We can think that doing nothing can bring stability over time, but it accumulates the actions necessary for the successful operation of the system over time. And so the teams consciously or unconsciously do everything to avoid any change for fear of risk at all costs. 

With time it becomes necessary to push in production all these changes accumulated. At this time: 
-	the risk is more important because we deliver in one time an important number of updates. 
-	the risk of bug or regression is more important, and more complex to identify in the mass. 

# Problem Causes:

* Fear of disrupting the system or causing unintended consequences
* Lack of understanding of the impact of changes on the system
* Perceived lack of time or resources to thoroughly test and implement changes

# Possible Mitigations

* Implement a thorough testing process before making changes to the production environment, to ensure that changes are well-understood and minimize the risk of disruption.
* Establish a culture of continuous improvement, where small, incremental changes are made regularly, rather than waiting for large-scale updates.
* Use version control and branching strategies to isolate changes and reduce the risk of unintended consequences.