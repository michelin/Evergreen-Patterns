---
title: "Reporting System Health State"
date: 2022-04-12T15:54:49+02:00
draft: false
categories:
- building
tags:
- building
description: "My systems are observable: Health Checks, Technical Golden Signals and End User Experience (SLI)"
interact_with: "sla_inversion"
---

# MAIN PURPOSE

All critical aspects of your product are monitored in real-time to ensure that potential issues are detected as soon as possible. System health includes Disk Space, Services, Performance, Scheduled Tasks, Software/Hardware and more.



# WHAT NEED TO BE DONE

* The connectivity to every dependent system is checked in the health check

* State of all major components of the application architecture are evaluated

* All related file systems free space is evaluated as part of the check

* Version numbers of deliverables are reported in the health check

* Deployment dates of components are printed in the check

* Uptime is included

* Significant activity details (whether a batch is currently running) is included

* System health check can be queried from a simple command line, it is « script » friendly, and can be requested by another system


# EXAMPLES

For Spring Boot apps
* Spring Boot ADMIN

For other stacks

* JavaMelody

* JMX

* DropWizard “Operational Menu”



# EXAMPLE  

![Production Aware Testing](/images/building/reporting_system_health_state.png)
