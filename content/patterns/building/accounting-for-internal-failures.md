---
title: "Accounting for Internal Failures"
date: 2022-04-12T15:54:14+02:00
draft: false
categories:
- building
tags:
- building
description: ""
featured_image: "/images/icons/accounting_for_internal_failures.png"
---

# DEFINITION

In our context we talk about internal failure as opposed to third-party failure. By internal we mean all the services, components, application that are under the responsibility of the product team.



# MAIN PURPOSE

A common risk is to believe things will go well all the time, and therefore design and implement only the “happy path”, meaning that we think all the components will always be available, integration process will never fail, etc …

We must do the exact opposite, imagine the worst cases, thinking about what can happen, go wrong and how it will be a non-event for us.



# WHAT TO DO

Systematically try to proactively identify where and how a system might fail. What could go wrong, why would the failure happen.

Build softwares that allow retries after a failure

* Ensure the system is in a state such that a failed job can be rerun without risk of duplicated or partial processing

* Ensure that the system has generated sufficient output that a technical support resource can reliably determine which records have been processed and which records have not

Have a target MTTR defined for every critical batch processing job the application is performing

* Test if it is achievable with the generated log

* Add more log / fix the log if it is not





# BEST PRACTICES

* Partial processing and duplicate loads are supported by design, the code accounts for this to happen

* Transaction boundaries are clearly defined and implemented in the code, in case several distinct actions must be done together to ensure integrity

* When a long running process is performed, there is a way to identify which records have been processed successfully, which records have not

* If a process is run twice by mistake, the second run does not duplicate any data, and at best it is identified as a duplicate run and does nothing.
  * Use staging tables 
  * Flag processed records 
  * Use transactions, savepoints, rollbacks

* Data loading mecanisms use checksum to identify duplicate inputs files

* Data loading mecanisms move input files to a « safe » place before they are integrated

* Every long running process has been brutally aborted as part of operability testing

* Logs are sufficient to understand what has been done/not done during these tests

* MTTR targets are defined for each critical long running process

* After an aborted processing, it is possible to run the remaining part without modifying any input file


# EXAMPLES

Modern development frameworks often come with resilience feature that you can leverage to implement code that is designed to handle common failures.

Some examples coming from the Spring family of Java frameworks:

Retrying failed operations can be implemented easily with “Spring Retry”

Spring Batch can rerun only failed steps from a previous run, a deep understanding of the [Spring Batch Domain Language](https://docs.spring.io/spring-batch/docs/current/reference/html/domain.html#domainLanguageOfBatch) is a great way to implement Batch that recover fast and cleanly 
