---
title: "Integration Points"
date: 2022-05-29T15:53:06+02:00
draft: false
description: ""
interact_with: "decoupling_middleware, circuit_breaker, reliable_data_exchange, traceability_of_data_flows"
---

# Description

Connections between systems always bring challenges and more complexity in the day to day operations. Systems are connected in order to share data or services and these can be critical for the reliability or even just the availability of your application.

Integration also often brings an additional dependency in the architecture : the middleware which is responsible for implementing the actual integration, direct point to point integration between 2 applications is often seen as an integration anti-pattern and is avoided, API managers are used even in simple request/reply scenarios, as they come with a lot of added values for operations (monitoring, security, throlling, ...).

# Some typical issues that needs to be adressed

- What should happen if the system I want to connect with is not available ? Are there any fallback scenarios that can be implemented to mitigate the impact on my end users ?
- Is the SLA of the target system compatible with mine ?
- Is the SLA of the integration middleware compatible with mine ?
- How can I know if the target system is up/down in a reliable manner ?

# What can be done

# Key patterns that can mitigate this problem

- Bulkheads, in order to reduce the blast radius of the integration problems
- Decoupling

# Related anti-patterns

- Sla Inversion

# Resources
