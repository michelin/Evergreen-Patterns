---
title: "Traceability Of Data Flows"
date: 2022-04-12T15:54:49+02:00
draft: false
categories:
- building
tags:
- building
description: "My systems' dataflows are easy to monitor and diagnose thanks to correlation (UUIDs...)"
featured_image: "/images/icons/traceability_of_data_flows.png"
---

# MAIN PURPOSE

Applications of our information systems exchange data, all the time. Referential data is pushed from data referential to transactional applications. Transactional data are exchanged between these applications and pushed to BI systems for analytics requirements.

Our business relies more and more on this data to be always available and as quickly as possible to make the best decisions. Our customers also expect data to be communicated to them in a timely and consistent fashion.

Being able to understand these data flows is a mandatory requirement and implementing end to end traceability of the data is a must have to understand the problems that will rise during these exchanges.

# HOW IT WORKS

Lineage of the data needs to be described somewhere, ideally all data flows of the information systems should be described in a central and shared repository and data owners should be clearly identified.

When transmitting data across system, include all the data that would help diagnose issues in case of problems. For example, include all identifiers that can help teams to quickly identify which data was successful transferred or not.

Logging all data transfers events is also mandatory, minimum required information are:

* start of transfer date

* source and destination (ip addresses, application names, …)

* size in bytes

* end of transfer date

* status


# EXAMPLES

Please refer to the pattern “Reliable Data Exchanges” for more implementation details and examples. 
