---
title: "SLA Inversion"
date: 2024-03-11T06:51:53+01:00
draft: false
status: reviewed
model: gpt-4-turbo-preview
categories: 
 - anti-pattern
tags: 
 - coupling
 - availability
description: "The lowest system's availability is the one of all its coupled dependencies."
---

![Card for SLA Inversion.](/cards/sla-inversion.png)
![The lowest system's availability is the one of all its coupled dependencies.](/images/sla-inversion.webp)

# Description

SLA Inversion occurs in IT systems when the system's overall availability and reliability are determined by the least reliable of its coupled dependencies rather than its own intrinsic design or capabilities. This anti-pattern emerges in architectures where critical components or services depend on external systems, APIs, or services that have lower availability guarantees (SLAs - Service Level Agreements) than the system itself aims to provide. The consequence is a cascading effect where the weakest link determines the maximum achievable reliability and availability of the entire ecosystem, often leading to frequent downtimes, degraded performance, and ultimately, a disappointed user base. This incongruence between expected and actual system performance can erode trust and deter users, impacting the business negatively.

# Possible Mitigations

1. **Dependency Evaluation and Management**: Regularly assess the reliability and SLAs of all external dependencies. Prioritize dependencies based on their criticality to your system's operations and seek alternatives for those with poor performance histories.
2. **Robust Architectural Design**: Design your system with redundancy and fallback mechanisms for critical dependencies. Utilize patterns such as Circuit Breaker and Bulkhead to isolate failures and prevent them from cascading through your system.
3. **Performance Contracts**: Where possible, negotiate SLAs with external service providers to ensure their commitments align with your system's requirements. This might involve additional costs but can be crucial for maintaining system reliability.
4. **Monitoring and Alerting**: Implement comprehensive monitoring for all external dependencies to quickly identify and respond to issues. Establish alerting thresholds that allow for proactive problem-solving before SLA breaches occur.
5. **Decoupling and Modularity**: Where feasible, architect your system in a modular fashion that allows for the easy replacement or bypass of unreliable dependencies. This may also involve building internal capabilities that can serve as backups to critical external services.

Mitigating SLA inversion requires a strategic approach to system design and dependency management, ensuring that external factors do not compromise your system's core objectives and service guarantees.
