---
title: "Production Aware Testing"
date: 2022-04-12T15:54:49+02:00
draft: false
categories:
- building
tags:
- building
description: "Tests are conducted at production scale on identical infrastructure. They encompass real-world user journeys"
featured_image: "/images/icons/production_aware_testing.png"
---

# MAIN PURPOSE

Before the production deployment we need the possibility to conduct tests on an environment that closely mimicks our real-world production.
The goal is to test codes, builds, and updates to ensure quality under a production-like environment.

Only because of that level of sameness, we will be able to conduct test that encompass real-world user journeys

# HOW IT WORKS?

To be able to do that, everything in the environments should be as close as possible to an exact copy of the production environment.
Software, hardware, architecture and configuration should be the same as production environments and when we say the same we mean same components but also the same versions of components, same level of patches ,etc…..

The way you are deploying the solution should also be identical.

If you have HA or load balancing mechanisms in production, you should retrieve those mechanisms in your environments

Integration flow need to be tested end to end like in production

It goes without saying that sizing and volume is also a key component.


# REAL WORLD USAGE IN MICHELIN

Ex : Delphix

This kind of tools can help you to make copies of databases in minutes with a limited impact on infrastructure ( almost no storage overhead by sharing all the duplicate data blocks between database copies )  

![Production Aware Testing](/images/building/production_aware_testing.png)
