---
title: "Handshaking & Backpressure"
date: 2022-04-18T17:53:35+02:00
draft: false
categories: 
 - architecting
tags: 
 - architecting 
description: "My systems collaborate with third parties to make sure they can handle my workload"
interact_with: "unbalanced_capacities"
---

# Handshaking

- Ensure that the third party can **accept our sollicitation before we do it**
  - Be proactive
- Requires **automated Health checks**
  - How can we inquire about the health of our target system ?
- Enabler for proper **throttling** and simple **back pressure mechanism**

# Throttling

- In our context, Throttling refers to the action of **deliberately limiting an activity** in order to **remove the burden** on a third party system
- In order to throttle, we need to have a system whose level of activity can be **dynamically controlled**
- In modern programming languages, we are using dynamic thread pools
  - They start with an initial size
  - This size can be **dynamically changed** during runtime

![HB-throttling.png](static/images/architecting/HB-throttling.png)

# Back pressure

- Back pressure describes ways to throttle a **service consumption** and handle **peak volumes**
- A service needs **a way to communicate** back to its callers to indicate that it is under pressure: it is overloaded and needs to breathe
- There are numerous ways to implement Back pressure systems
  - **Add system health information** inside existing responses (new header attributes for example)
  - **Implement an health check** that clients must evaluate **before** sending sollicitations to a service
  - **Use Reactive Streams** that implement Back Pressure “By Design”
  - Use technology specific solutions (Spark Streaming)

![HB-1backpressure](static/images/architecting/HB-1backpressure.png)
![HB-1backpressure](static/images/architecting/HB-2backpressure.png)

- Ensure that in a publisher / consumer scenario a consumer **gets never overwhelmed** by a publisher that publishes too much too fast
- The consumer becomes an **initiator**: when it is available to execute more work, it **requests tasks** to execute from the stream
- Reactive Streams have an implementation impact on **both sides**

## Back pressure with older architecture

- When reactive streams are not applicable because
  - It is not possible to impact the implementation of both sides of the exchange
  - The technology is not available for the runtimes used
- Simpler implementations are still possible with **Health Checks** for example:
  - Query health checks periodically to check if its ok to keep sending activity : maybe a complex batch activity is in progress on the service side, and it is not a good time for sending a lot of work load?

