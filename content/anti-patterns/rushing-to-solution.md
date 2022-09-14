---
title: "Rushing to Solution"
date: 2022-05-28T15:52:39+02:00
draft: false
description: "Restoring a system during an outage is the top priority but not taking enough time for collecting data or analyzing"
interact_with: "error_categorization, application_logging, chaos_engineering, embrace_failures"
---

Whenever a failure occurs, restoring the service as soon as possible is of course important, but finding the root cause of the issue is also important to make sure we are doing the right actions and to prevent any reoccurrence. If the root cause can’t be found directly, then collecting the necessary elements to understand what has happened and find the root cause is key. 
Collecting the elements does not mean doing the analysis: once the elements are secured, the service can be restored, and then the analysis can begin 
 
Example : when an application is very slow, restarting it may solve the issue on the short term, but if you take some time before restarting it to make a memory dump, the analyze some metrics (cpu, RAM, I/O, …), to look at the running processes on the server, to copy some logs to a safe place for future analysis, then you may be able to investigate and find the root cause and prevent the incident to happened again. 
