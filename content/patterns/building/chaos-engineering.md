---
title: "Chaos Engineering"
date: 2022-04-12T15:54:34+02:00
draft: false
categories:
- building
tags:
- building
description: ""
featured_image: "/images/icons/Chaos_Monkey-31.png"
---

# MAIN PURPOSE

Chaos engineering is the process of experimenting on a system to ensure that it can withstand unexpected disruptions.  
It relies on concepts underlying chaos theory, which focus on random and unpredictable behavior.

This is a modern approach to testing and validating your application architectures, it will help all teams from dev to support to have a better understanding of the product and be more confident that the application will be able to handle faults gracefully.

Bring teams closer by sharing

* Recognize outage patterns.

* Sharing monitoring tools

* Learn how to assess the impact.

* Determine the root cause and mitigate accordingly.

* Practice log analysis.



# HOW IT WORKS?

A common way to introduce chaos is to deliberately inject faults that cause system components to fail. The goal is to observe, monitor, respond to, and improve your system's reliability under adverse circumstances.

You can for example, introduce latency, shutdown components, restrict access or force failover at different level (OS ,database , application , ...)



# WHEN TO APPLY

Ideally, you should apply chaos principles continuously. There's constant change in the environments in which software and hardware run, so monitoring the changes is key. By regularly applying stress or faults on components, you can help expose issues early, before small problems are compounded by a number of other factors.

At least apply chaos engineering principles when you're:

* Deploying new code.

* Adding dependencies.

* Observing changes in usage patterns.

* Mitigating problems.



# WHERE ( which env ) TO APPLY

Ideally, chaos principles should be applied in all environments including production, but we start for sure by the non-production. If possible, apply it continuously. There's constant change in the environments in which software and hardware run, so monitoring the changes is key. By regularly applying stress or faults on components, you can help expose issues early, before small problems are compounded by several other factors



# EXAMPLES


Take dependencies offline (kill process , stopping API apps, shutting down VMs, etc.),
Restrict access (enabling firewall rules, changing connection strings, etc.)
Force Failover at different level  ( OS , database , etc … )  
Overload your system

A lot of different tools / frameworks exists that will help you to simulate abnormal behavior and automate them  


![chaos engineering](/images/building/chaos_engineering1.png)


![chaos engineering2](/images/building/chaos_engineering2.png)

 
