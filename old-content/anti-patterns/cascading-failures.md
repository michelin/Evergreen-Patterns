---
title: "Cascading Failures"
date: 2022-04-12T15:51:36+02:00
draft: false
description: "Failures of a system propagate to all its highly coupled third parties"
interact_with: "bulkheads, circuit_breaker, using_timeouts, "
---

# Main Purpose

A cascading failure happens when an incident in one part of a given system triggers failures in other parts inside it, or in interconnected systems, with no possibility to stop the propagation. This is causing a domino effect that can have a huge impact. 
One of the most famous patterns in order to avoid a cascading failure is the “Circuit braker”   
