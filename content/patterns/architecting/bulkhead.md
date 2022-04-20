---
title: "Bulkhead"
date: 2022-04-18T17:53:35+02:00
draft: false
categories: 
 - architecting
tags: 
 - architecting 
description: "My system isolate functionalities to reduce the blast radius when problems occur"
featured_image: "/images/icons/bulkhead.png"
---

For a truly resilient and self-healing architecture, you need isolation, external monitoring, and autonomous decision-making. Bulkhead pattern is one of the component of a truly resilient architecture, alongside with others like Circuit Breaker.

# How it works ?
Bulkheads consists in partitioning your system in order to protect it against cascading errors. Essentially, a bulkhead assigns limited resources to specific (groups of) clients, applications, operations, client endpoints, and so on.

# When to use it ?
Use this pattern to:
- Isolate resources used to consume a set of backend services, especially if the application can provide some level of functionality even when one of the services is not responding.
- Isolate critical consumers from standard consumers.
- The service criticality is the best isolation criteria
- Protect the application from cascading failures.

# How it is implemented ?

## REDUNDANCY
Having a service rendered by more than one instance greatly improve its resilience since the risk of having all of them getting down at the same time is nearly null.
Critical services must be clustered.

## MICRO SERVICES
These services are isolated by design. They are restartable and scalable independently.

## CONTAINERS
Containers offer a good balance of resource isolation with fairly low overhead. This is a complete isolation of the runtime.

## ASYNCHRONOUS MESSAGES
Services that communicate using asynchronous messages can be isolated through different sets of queues. Each queue can have a dedicated set of instances processing messages on the queue, or a single group of instances using an algorithm to dequeue and dispatch processing.

# Examples

## DEDICATED ADMIN NETWORK LINK
Servers & Hypervisors typically use 2 network links, one is dedicated for administrative tasks and will still be available if the other, production network link has issues

## "RESOURCES PER CLIENT" MODEL

Applications that have both internal and external users typically have distinct application servers and APIs to handle the 2 types of traffic
The activity is very different and and external activity also present additional challenges, like ensuring security