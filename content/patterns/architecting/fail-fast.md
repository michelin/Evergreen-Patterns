---
title: "Fail Fast"
date: 2022-04-18T17:53:35+02:00
draft: false
categories: 
 - architecting
tags: 
 - architecting 
description: "Before starting a task, my systems ensure it has a chance to be fully completed"
interact_with: "unbalanced_capacities"
---

# Principle

**Before starting a task ensure it has a chance to complete.**
<em>A chef won’t start to cook before he ensured he has all the ingredients</em>

**Fail-fast systems are designed to stop operation rather than attempting to continue a possibly flawed process.**
<em>Eases debugging, improves visibility and understanding of root causes</em>

**Implemented in circuit breakers**
<em>When a circuit status in « Open »: solicitations instantly fail</em>

# Examples

- **Input validation**
  - We validate user input before we submit to a server
  - If required data is missing, we do not try to execute the process
  - Applicable to any kind of validation (uploaded data files, logistic network description, …)
- **Especially before long running operations**
  - Do not generate a big data file before checking that the destination is online for instance
  - …


