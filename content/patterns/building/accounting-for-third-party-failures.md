---
title: "Accounting for Third Party Failures"
date: 2022-04-12T15:53:33+02:00
draft: false
categories:
- building 
tags:
- building
description: ""
featured_image: "/images/icons/accounting_for_external_failures.png"
---

# DEFINITION

In our context a third-party is a product, a service or an application that is not under the responsibility of the product team.

# MAIN PURPOSE

A common risk is to believe things will go well all the time, and therefore design and implement only the “happy path”, meaning that we think all the components will always be available, integration process will never fail, etc …

We must do the exact opposite, imagine the worst cases, thinking about what can happen, go wrong and how it will be a non-event for us.

![1](/images/building/3_party_failures.png)


# WHAT TO DO

Systematically try to proactively identify where and how a system might fail. What could go wrong, why would the failure happen.



Use Fuses

* Fuses : When a threshold or error condition is reached, the fuse blows and halts processing

and Fallbacks

* The business users must be involved in deciding what must be done as an alternative scenario

* Is a service degradation possible?

* Provide the result of the last successful invocation, stop the processing, display an error, …





# BEST PRACTICES

* Thresholds are in place for every retriable functionality

* The state of all the « fuses » in the system can be queried

* A fuse goes back to its normal state automatically or with a simple command

* Timeouts are in place, and their value is known in advance, for every synchronous communication with a third-party system

* Failures are not cascaded

* Implement Fallbacks and Graceful degradation



# EXAMPLES

[Resilience4J](https://github.com/resilience4j/resilience4j)


* Open-Source Java Library that implements a lot of fault tolerence patterns

* Retry

* Circuit Breaker

* Rate Limiter

* Time Limiter

* Bulkhead

* Cache

* Fallback 
