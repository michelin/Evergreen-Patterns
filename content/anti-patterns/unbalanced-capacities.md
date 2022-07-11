---
title: "Unbalanced Capacities"
date: 2022-05-29T15:52:26+02:00
draft: false
description: "The resources consumed by my system are maladjusted to the tasks to be performed"
featured_image: "/images/anti-patterns/unbalanced-capacities.jpg"
---

# Description

Your system consumes resources in order to execute the workload it is assigned. If these are not enough resources available to satisfy the demand, it is probable that the system will start becoming slower and slower, and this will introduce additional problems such as timeouts and blocked threads. 

# What can be done

Monitoring the Golden Signals (Saturation, Latency, Errors, Traffic) is a mandatory activity for any system. This will enable a better understanding of the usage and help in identifying trends and seasonality in usage patterns. Saturation is the key signal to understand how full the current infrastructure is and how this consumption evolves over time.

Typical metrics that are directly linked with resource consmption:
- CPU % Usage
- Memory % Usage
- Network Bandwidth usage
- I/O 

It is important to understand in your specific system what is the main resource that can become a bottleneck : it is not uncommon for example, to see systems which are more quickly restrained by I/O performance (I/O bound) than by the CPU. 

# Key patterns that can mitigate this problem

- Capacity Planning
- Observability, and monitoring the Golden Signals
