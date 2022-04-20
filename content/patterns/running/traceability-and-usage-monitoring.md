---
title: "Traceability and Usage Monitoring"
date: 2022-04-12T16:02:59+02:00
draft: false
families:
- running
description:
featured_image: "/images/icons/traceability_usage_monitoring.png"
---


# Main Purpose

The goal of Traceability & Usage Monitoring is to better understand the usage of the application: when it is used, by which users (which types of users, from which locations ,…), what functions or part of the application are used, how is the application used, …



There are many reasons to do so:

* To follow up the ramp-up and adoption of a new application

* To know when the application is least used to better plan maintenance or changes

* To know when the application is most used to adapt the capacity

* To identify which features are heavily used and determine potential hotspots that could benefit from optimizations, functional partitioning or load balancing.

* To understand which parts are not used and investigate why they are not used in order to either correct issues (UI/UX problem for example) or to remove them if that makes sense (parts that are not used but are still maintained generate costs).

* To better allocate development efforts

* To be able to identify abnormal usage patterns that can impact security or performance of the application

* To detect if the application is not used any more and should be decommissioned

* To understand what a specific user did in the application, in order to troubleshoot an incident

* …



It is important to note the difference between traceability and usage monitoring and auditability:

* the purpose of auditability is to fulfill legal (or functional) requirements. For example, tracing when and by which user a specific field was updated, an element has been validated or rejected, etc …

* the purpose of traceability and usage monitoring is to understand how users are using the application (what functionalities, what frequency, what order, …) and to help troubleshoot by tracing each step performed by the user to ease reproduce the issue.



# How it works

There are different possibilities to trace the usage of an application:

* By tracing events in the logs of the application (in that case, it is better to use dedicated log files which will make analysis easier)

* By generating entries in a database (or other storage system)

It is important to determine which elements are relevant to be traced or not (keep in mind confidentiality, or personal data for example) and the appropriate level of detail.

Is it also important to keep the overhead of tracing these elements as light as possible: it must not impact the application’s performances.



# Example

For example, you can track every time a user clicks on menu entries in your application. This information will allow you to generate analytics such as:

* % of users using functionalities over a day/week/month. You may be able to tell that a given functionality is used by a small number of users (which may be normal: for example, the administration menu is used only a administrators).

* when each functionality is the most used

* frequency of use of each functionality

* when the application is the most used (time of day, day of week, day of month, …)

* etc. …



You can also collect business metrics that will show the usage of the application: the number of objects created or modified per day (it could be documents, orders, invoices, etc …), number of active users or connections per day, … 

 
