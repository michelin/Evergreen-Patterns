---
title: "Reliable Service Exposition"
date: 2022-04-12T15:52:31+02:00
draft: false
categories:
- architecting
tags:
- architecting
description: ""
featured_image: "/images/icons/reliable_service_exposition.png"
---

# MAIN PURPOSE

When exposing services that will be consumed by other systems and applications, it is important to implement several key mechanisms to ensure this exposition is as robust, secure, and resilient as possible.

You want your service exposition to be documented, secured and auditable (must log all invocations).

# WHAT TO DO

Do not reinvent the wheel

* Use standard protocols that are supported by a large set of tools and ensure a good testability

* Use standard, human readable formats (JSON), this will greatly help operations and supports to diagnose and analyze issues

* Leverage standard tools such as API Managers, which come with a lot of added benefits



# BEST PRACTICES

* Communicate your service health and status to the outside world (with a dedicated /status endpoint for example)

* Ensure invocations to your service can be throttled to avoid resource saturation

* If using synchronous protocols, always prefer quick and reactive APIs. If you need to execute a long running operation, implement an API to request the progress of this long running task with a task ID

* Log all invocations to your service


# RESOURCES

![api culture](/images/architecting/api_culture.png)

[API at Michelin (Internal Link) ](https://integration.si-pages.michelin.com/APIM/pages/apimpages/)

[developer.michelin.com](https://developer.michelin.com/)
