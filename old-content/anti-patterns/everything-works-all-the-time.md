---
title: "Everything Works All The Time"
date: 2022-05-29T15:53:06+02:00
draft: false
description: "My systems only implement the happy paths with no design for failure"
interact_with: "continuous_architecture, continuous_operability"
---

Systems are designed and built considering that everything will happen as planned and are therefore only considering the “happy path”: 
-	When they are waiting for files from other applications: they consider all those files will be received, and that they will all be on time and with the right format with no data issue 
-	When they are relying on external webservices, they expect them to be always available 
-	When they are sending data to a third-party system, they do not check the response to make sure everything is ok 
-	There is no (or not enough) troubleshooting information in the logs 
-	There is no timeout to interrupt abnormally long transactions 
-	Etc … 
 
When designing and building a system, it is very important to imagine what could go wrong (both internally and externally) and how to handle it or at least how to minimize the impact and help troubleshoot. In some cases, there may be a degraded mode providing only the most critical functionalities. 
 
Example: 
An application is having a significant batch plan with different jobs, some of them using files that are received from other applications. When one of those files is not received, the whole batch plan is stuck until it arrives, even for jobs that are not depending on those files. In this case, it would have been a good idea to: 
-	Define what to do if the file is late (there may be a degraded mode) 
-	Decouple parts of batch plan, so that parts not depending on a particular file are not impacted if it is not received 
