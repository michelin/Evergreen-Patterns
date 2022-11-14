---
title: "Decoupling Middleware"
date: 2022-04-18T17:53:35+02:00
draft: false
categories: 
 - architecting
tags: 
 - architecting 
description: "My systems use middleware to enable asynchronous data exchanges"
interact_with: "sla_inversion, integration_points, big_bang_deployment"
---

# Main purpose
- Tight coupling between distinct components is an operability issue.
- Synchronized communications propagates the SLA between components and cascades failures
- Integration Middlewares can help to break the propagation of the SLA, because they loose this coupling
- Middlewares can protect the left side of the communication from failures of the right side
- This only work when used in an asynchronous exchange

# Examples

![1-Examples](static/images/architecting/1-examples.png)

**Tight coupling** between A and B
if B breaks the A breaks
- The SLA of A is **directly impacted** by the SLA of B
- A will only be available when B is

![2-Examples](static/images/architecting/2-examples.png)

The solution to this problem may be to break the synchronous link between the 2 components: 
- Now A can « survive » a restart or failure of B but **only if the exchange is asynchronous**
- A must handle the response from B as an async **event**
- It **must not** wait (in a polling loop) for the response from B

# General principal

If an exchange is **synchronous** by nature, trying to break coupling with a third party will only bring additional problems.
➡️ <em>This is where Circuit Breakers will help a lot.</em>

Communication with the database is always seen as must be synchronous, but is it really needed?
➡️ <em>Can we design the system so that we can survive a hot database interruption, without compromising our design principles ?</em>

Synchronous is often associated to 'real time': this is **wrong** as near real time can be achieved with async too. These are 2 different concepts

![3-Examples](static/images/architecting/3-examples.png)

# At Michelin

Usage of this pattern is already popular in Michelin IT, with MQ Series mostly/

However we have seen some incorrect usage of it:

- **Trying to « asynchronize » synchronous data exchanges** : we are doing synchronous data exchanges with a technology which is not designed for them
- **They bring additional complexity with operability**
    - Dependency on Infra to manipulate the BackOut contents, …
    - Team loses is autonomy for some issues

The current implementation of this pattern also do not allow Back Pressure and more modern patterns.

