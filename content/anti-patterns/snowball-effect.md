---
title: "Snowball Effect"
date: 2022-05-29T15:53:06+02:00
draft: false
description: ""
interact_with: "steady_state, continuous_operability, observability, capacity_planning, immutability"
---

Simple issues, if not managed quickly, can generate very complex situations that can be very hard to resolve. 
Systems must be designed to handle issues and making sure small issues are not going to generate bigger issues over time. Detecting issues and triggering self-healing or raising alerts is also a key feature of systems to avoid unmanageable situations. 
 
Example: a filesystem is full, which will cause errors on the storage of an application, which will cause incoherent state between the filesystem and the status in the database and erroneous data to be sent to other applications, which over time will be more and more complex to solve. 
