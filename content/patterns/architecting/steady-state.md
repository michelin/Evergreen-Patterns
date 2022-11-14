---
title: "Steady State"
date: 2022-04-18T17:53:35+02:00
draft: false
categories: 
 - architecting
tags: 
 - architecting 
description: "My systems operate indefinitely in well known and monitored conditions"
interact_with: "unbalanced_capacities, snowball_effect, reactive_operations"
---

A software is designed to work in defined « normal » conditions.

For example:
- There are some free space in the file system
- Database can extend
- The volume of data inside the DB is in predefined limits
- …

Every time the software consumes resources that are associated with these conditions, it has an automated way to release these resources.

**Automated** is the most important word here

# How it works ?

- Every time a resource is consumed, there is an automated way to release this resource
  - A system should be able to run indefinitely **without any human intervention**
- When a purge of data is required after 3 years of production people will not remember to do it, and if they do it might be unclear on how to do it
  - The system will be slower and slower

![SteadyState-works](static/images/architecting/SteadyState-works.png)

# Examples

**I create a temporary file that contains some processing data**
👍 <em>Steady state</em>: I implement the removal of this file when I am done with it

**I store data in a database**
👍 <em>Steady state</em>: I implement the removal of data which is not useful anymore : it has become « cold » data. Purge or move the cold data out of the transactional system, it is not hard to automate.

**I log application data in files**
👍 <em>Steady State</em>: I use rotation of my log files to avoid multiplication

**I cache processing results in memory**
👍 <em>Steady State</em>: I have a cache invalidation strategy

![SteadyState-examples](static/images/architecting/SteadyState-examples.png)
