---
title: "Using Timeouts"
date: 2022-04-18T17:53:35+02:00
draft: false
categories: 
 - architecting
tags: 
 - architecting 
description: "My systems are configured to stop before being fully overloaded"
interact_with: "cascading_failures"
---

# When use it ?

- Every time a third party is involved
  - Even in some of the internals of your own stack : when trying to get access to a resource : remote file system, connection to a DB, a queue, …
- Seems easy?
  - Do we really know and manage the complete chain of timeouts from the user action trigger all the way to the database access or middleware interaction ?
  - What are the good, correct, useful and realistic values to use ?
  - Understanding what are the different types of timeouts of the chain, which component reports them, and how they are reported
   - Different types of timeout are related to completely different types of issues and problems!

# Example

Sample problems and questions you need to answer:

- What happens when the call from **Recommendations** to **Relevance** timeouts ?
  - **Relevance** needs to know that there is no one still needing the result of the ongoing call to **Promotions** in this case.. The worst thing that could happen if that **Relevance** timeouts and retries…
- Does it make sense to use a longer timeout between **Relevance** & **Promotions** than between **Recommendation** and **Relevance** ?
- How can we propagate the information of a client timeout across the chain to avoid unnecessary work ?

![Tux, the Linux mascot](static/images/architecting/UsingTimeouts-examples.png)

# Off the shelf implementations

In Java
- [Resilience4J](https://github.com/resilience4j/resilience4j)
- [String Retry](https://github.com/spring-projects/spring-retry)
- [Hystrix](https://architecture.michelin.com/) is not developed anymore and Resilience4J should be used instead (however it is still rock solid, so do not replace Hystrix on purpose)

In Golang
- The [context package](https://go.dev/blog/pipelines)
Even if Golang is not a standard development technology we use at Michelin, the understanding of the “context” package gives a good example of how these kind of issues could be fixed (how to cancel a complete chain of interactions).

# Best practices

- Historical data is useful when available
  - Use it to define what are good timeout values
- Consider using [Exponential Back-off](https://en.wikipedia.org/wiki/Exponential_backoff) to avoid congestion when you have no idea of when a service will be available again
- Associate with retries but wisely
  - Only if it has a chance to succeed after an instant retry
  - Depends on the nature of the failure
  - Sometimes it may make a problem worse !
  - If possible and applicable to your case, consider a fallback scenario instead of a retry
- Timeout adjustments can have a great impact on the behavior and availability of applications
  - Try to ensure you capture a complete history of their values (in GIT directly)
  - Useful to correlate application health with the values
- When you consume an external API, make sure you use the values recommended by the provider of the API


![Tux, the Linux mascot](static/images/architecting/UsingTimeouts-bestpractices.png)

