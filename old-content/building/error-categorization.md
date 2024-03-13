---
title: "Error Categorization"
date: 2022-04-12T15:54:49+02:00
draft: false
categories:
- building
tags:
- building
description: "My systems' logs use standard error severities agreed between the build and operations"
interact_with: "normal_errors, rushing_to_solution"
---

# MAIN PURPOSE

Error categorization is the mandatory first enabler for Application logging and then monitoring

![Error Categorization](/images/building/error_categorization.png)

# GOAL

Define standard error severities and give them meaning.
A meaningful Error Categorization will facilitate doing good and useful application logging.

It enables communication between Build and Run teams. They need to agree on standard error severities and its consequences, for example if I log an error message at a « Fatal » level, someone may be on-call and woken up in the middle of the night 


# ERROR CATEGORIZATION EXAMPLE 


| Error Severity  | Context         | Implication |
|:----------------|:---------------:| -----:|
| **FATAL**       |   A core component, service, or resource is failing. Developers should assign this error level to events that are expected to impact an entire application or suite of functionality.        |  Indicates service is down and likely not available. Immediate and urgent resolution is requited.  |
| **ERROR**       | An individual transaction or unit of work has failed for an unexpected reason. Error events may occur as a result of a fatal event in the infrastructure in which case a single fatal event will correlate to many error events.             |   In general error event will not trigger immediate investigation by support. However a high frequency of independent error events may be escalated into a fatal event by the monitoring infrastructure.  |
| **WARN**        | A configured threshold or assertion has been reached and a problem may be imminent           |    Waning events do not reliably reach the attention of operations but are useful in development and QA environments  |


# BEST PRACTICES


Have the support / run teams review the contents of the logs that are generated in case of problems, this will ensure they understand it and that they have enough information to react adequately.
