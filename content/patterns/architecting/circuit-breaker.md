---
title: "Circuit Breaker"
date: 2022-04-12T12:27:55+02:00
draft: false
families: 
 - architecting
tags: 
 - architecting 
description: "My systems are protected from third party failures"
featured_image: "/images/icons/circuit-breaker.png"
---

The Circuit Breaker is a very popular resilience pattern to interconnect systems synchronously.
It protects the caller from failures of the invoked service.

Useful reading: Martin Fowler' article

# How it works ?
A Circuit breaker has three states:


Closed (initial default state)
Opened
Half-opened
Fallback
When the Circuit is opened, it is recommended to implement a fallback that will be used instead of the original service.

The fallback should be built in relation with the Business: they should be involved in the decision of what the application should do in this scenario.


# When to use it ?
To prevent an application from trying to invoke a remote service or access a shared resource if this operation is highly likely to fail.

## APPLICABILITY TO LEGACY ARCHITECTURE
Circuit Breakers can often easily be implemented in existing applications. Hystrix for example has been successfully integrated.

## ATTENTION POINTS
This pattern isn’t recommended as a substitute for handling exceptions in the business logic of your applications.

## Monitoring
Circuit-Breakers will automatically restore a service after failures. It is however still very important to monitor their activity. They can hide problems, but the underlying problems they hide should still be fixed if possible.

# How it is implemented ?
Standard, off the shelf implementations are preferred when applicable.

If no standard implementations are available in the target environment, from scratch solutions can be implemented. The complexity of the implementation should not be underestimated however it involves a good knowledge of low level threading mechanisms to be implemented properly.

# Examples

## Hystrix
Hystrix is a very popular Java based implementation developed by Netflix.

### Requirements
Its only requirement is a Java 7+ JVM.
It has been successfully implemented in Michelin in both SpringBoot based projects and Websphere applications (TRW).

## resilience4j
resilience4j contains an implementation of the Circuit-Breaker pattern.

### Requirements
resilience4j requires Java 8 and is targeted towards functional programming.
There are currently no implementations of resilience4j in Michelin projects.
