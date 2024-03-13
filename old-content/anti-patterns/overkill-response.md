---
title: "Overkill Response"
date: 2022-05-29T15:53:06+02:00
draft: false
description: "I use drastic measures that have a large impact to fix simple issues"
interact_with: "chaos_engineering, continuous_knowledge, hypercare"
---

When an issue occurs, understanding the impact and defining the right action(s) to fix it, with no or minimum side effect, is key. The set of measures should be enough to fix the issue, but not too much to avoid any unnecessary impacts. Before doing something that will have a significant impact, take a moment to see if another action is possible with a more limited impact. It is possible to have a set of gradual measures that can be applied one after another until the issue is fixed. Not applying these “just right” practices is an “overkill response” impacting Quality of Service and it may also prevent the ability to diagnose root causes. 
 
Examples: 
-	if a process is not responding, restarting the full server will impact other processes and applications. There are other options to be considered before, such as killing the process having the issue for example. 
-	If an ETL job is having an issue and debugging must be activated: activate it only for the job having the issue, not for the full ETL server as it would slow down the server and generate lots of logs. 
-	If a single job of a batch plan has failed and other jobs do not rely on it, there is no need to relaunch the complete batch plan which would slow down the application for several hours. 
