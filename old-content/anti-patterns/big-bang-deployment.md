---
title: "Big Bang Deployment"
date: 2022-04-12T15:51:36+02:00
draft: false
description: "Go live of my systems is not gradual and is a one shot and very risky operation"
interact_with: "progressive_roll_out, hypercare"
---

# Main Purpose

For bad or good reasons, because we are afraid to apply changes on a product or a solution that is not fully under control, or because we are working in a waterfall mode, we decide to move several months of workload in production all at once. This is what we call a “Big bang” deployment.  
This is the opposite of what we promote most of the time: continuous integration / continuous deployment (CI/CD) because “big bang” deployments embark a lot of risks and almost never go well.   
There is pressure on feature’s delivery, therefore these big releases just tend to get bigger, because people know that the next one will be in a long time. Finding move to production slots becomes a headache because the associated outage is very long. At the end of the day, with so much change at once, the stability often suffers. 
