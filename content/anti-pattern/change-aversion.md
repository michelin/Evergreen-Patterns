---
title: Change Aversion
date: 2024-02-24T05:50:18.124446284Z
draft: false
status: draft
model: llama2:13b
categories: 
 - anti-pattern
tags: 
 - anti-pattern, 
description: "Changing systems in production is risky so I avoid it at all cost."
---


Change Aversion
===============

The Change Aversion anti-pattern describes the tendency to avoid making changes to systems in production at all costs, due to the perceived risk of disrupting the system or causing unintended consequences. This can lead to a reluctance to adopt new technologies, fix bugs, or make improvements to the system, resulting in stagnation and decreased efficiency.

Possible Mitigations:

* Implement a thorough testing process before making changes to the production environment, to ensure that changes are well-understood and minimize the risk of disruption.
* Establish a culture of continuous improvement, where small, incremental changes are made regularly, rather than waiting for large-scale updates.
* Use version control and branching strategies to isolate changes and reduce the risk of unintended consequences.

Problem Causes:

* Fear of disrupting the system or causing unintended consequences
* Lack of understanding of the impact of changes on the system
* Perceived lack of time or resources to thoroughly test and implement changes

Tagged as: [technology-risk, stagnation, best-practices]