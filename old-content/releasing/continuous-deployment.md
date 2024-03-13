---
title: "Continuous Deployment"
date: 2022-04-12T17:46:08+02:00
draft: false
categories:
- releasing
tags:
- releasing
description: "I deploy my systems with an automation tool which guarantees deployment is fast and reproducible"
interact_with: "toil_routine, snowflake, change_aversion, untracked_operations"
---

# Main Purpose

Continuous Deployment consists in automatically deploying in production any software changes that go through the automated tests of the production pipeline. This helps ensuring consistent Quality of Service over time by mitigating change risks.

Automating deployments is key to ensure fast and reproducible results. Deployment is triggered only if automated tests are successful.

# How it works

Continuous Deployment is the ultimate step following Continuous Integration and Continuous Delivery.

Continuous Deployment is going beyond Continuous Delivery: all changes that are going through the pipeline (integration, automated tests, …) are deployed without human intervention. 

![continuous_deployment](/images/releasing/continuous_deployment.png)
*Source: Atlassian* 

Depending on the context, this can be seen as a polar star or as a goal to reach. For example, for some critical applications, some manual testing and validation may still be required before really deploying to production.

The key point is to automate as much as possible: code validation, integration, tests, deployment to test environments, …. This will reduce the time between coding and feedback, which will improve software quality.

The quality of tests and test mindset in the team must be very high to deliver quality versions.

Another very important point to consider it “feature flags” which become part of the deployment process for new significant features: this allows to synchronize with all stakeholders before activating a feature. The code is pushed in production but can be activated later by setting a flag. 

