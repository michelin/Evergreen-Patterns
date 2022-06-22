---
title: "Defined Service Levels"
date: 2022-04-12T15:52:02+02:00
draft: false
categories:
 - architecting
tags:
 - architecting
description: "Business has defined expectations of my system's availability & performance"
featured_image: "/images/icons/define_service_levels.png"
---

# MAIN PURPOSE

When trying to define whether your systems offer a good quality of service, it is important to define what “Good” means in your own specific context. Observable Service Levels should be defined and measured so that you can know very confidently at any time if your systems are delivering a good experience to their businesses. Defining which are the good service levels is not an easy task and identifying which metrics must be captured to measure them must be done early enough.

Identifying Service Levels Indicators (SLI) and setting Service Level Objectives (SLO) for them is also a foundation for SRE (System Reliability Engineering) practices, and even if you are not deploying the complete SRE practices on your product, we recommend that you still define and measure SLIs and SLOs.

The most popular SLIs include availability, request latency, system throughput and Error rate.

SLIs and SLOs are a foundation for a error budgeting, a best practice balancing development and operations objectives.

# WHAT TO DO

SLO refers to a service-level objective. These objectives are defined as means to determine whether a system is operating at a level acceptable for the business. All personnel within a development and operations organizations understand the fact that, when a system is unavailable and unreliable, it is unable to perform its function to the customer with any level of consistency.

While it would be nice if services were able to operate perfectly, 100% of the time, it is not possible. Therefore, SLOs are a benchmark for determining a target level of system reliability. This includes measurable objectives such as simple availability (e.g., the system must be accessible 99.9% of the time) or system performance (e.g., 99.5% of requests must complete within 500ms). Together, these objectives combine to provide an accurate depiction of system quality for which the organization can stand by.

SLOs are hard to monitor without indicators that provide the backing metrics and associated insights for measuring these objectives. These measurements are known as SLIs or “service-level indicators”. By tracking and evaluating SLIs (error rate, request latency, etc.), you can effectively monitor service availability, quality, and performance to ensure that the system is living up to the level of reliability promised by the SLOs.



# BEST PRACTICES

* Ensure both the build team, the support and the business understand what the objectives are and agree with them

* Involve SRE expertise early on to help you identify these requirements

* Set realistic objectives and iterate regularly to refine them

* Define what are the consequences of not reaching the objectives, should you reprioritize implementation of stabilization features from your backlog in this case? Should you organize post-mortems?

# EXAMPLES 

![1](/images/architecting/splunk.png)

*A2P: comparing the performance of the promise web service to a SLO (95% of all invocations should be done in less than 500ms)*

![2](/images/architecting/splunk2.png)

*A2P: 15 days of SLOs*

# EXTERNAL RESOURCES

[Learn how to set SLOs -- SRE tips | Google Cloud Blog](https://cloud.google.com/blog/products/management-tools/practical-guide-to-setting-slos)

[Google - Site Reliability Engineering (sre.google) ](https://sre.google/workbook/implementing-slos/)
