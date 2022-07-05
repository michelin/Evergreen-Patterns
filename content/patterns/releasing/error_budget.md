---
title: "Error Budget"
date: 2022-04-14T16:27:56+02:00
draft: false
categories:
  - releasing 
tags:
  - Releasing 
description: "Service Level Objective violations must be anticipated & trigger consequences"
featured_image: "/images/icons/error_budget.png"
---

# Definition

Error Budgeting is an SRE practice that is very useful to help you find the proper pace and balance between developing new end user features or making your system more resilient and stable.

When implementing SRE practices, you will start by identify the good service level indicators (SLIs) and associate them with objectives (SLOs) that will let you know at any time if the service you are delivering to your users is acceptable or not.
You can refer to the pattern "Defined Service Levels" for more information on SLI & SLOs.

Let's imagine that you manage a service for which you have a target SLO of 99.5% availability.
In this case, your error budget is 0.5% (100 - 99.5), it means that you can be unavailable 0.5% of the time and still meet your objective.
For a bucket of 28 days, it means that your service can be unavailable for 200 minutes.

This budget of time, your Error Budget, is there to be spent if you need to. And you can for example decide to spend it by delivering new features. Outages of the service that are either planned or non-planned should impact your Error Budget the same way (from a end-user standpoint, it doesn't really matter if it was planned or not, the result is the same), but it is something that you can of course decide to change depending on your context.

When you need to determine wether or not you can accept to take risks by delivering new end-user features in production you will check wether or not you have remaining error budget. If you don't then you should not accept this delivery and instead have your build team focus on non functional requirements in order to fix the actual cause for the availability issue (implement additional resilience or self healing patterns for example). 

Preparing a post mortem or Root Cause Analysis review is also a typical consequence of not reaching your SLO and consuming all your error budget.

# How

The consumption of the error budget should of course be monitored so that at any given point of time, you know wether or not you have budget left for the current rolling time window (28 days is a recommandation, because it always contain 4 weekends), and if you are below your SLO, you want to be able to determine your burn rate, which represent how fast you are currently consuming your budget.

The burn rate will represent how urgently you need to react to the problem in order to preserve your objective target. And following it closely will help you be more proactive to SLO violations.

# External resources

https://sre.google/workbook/error-budget-policy/

https://sre.google/workbook/alerting-on-slos/
