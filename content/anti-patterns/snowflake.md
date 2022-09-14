---
title: "Snowflake"
date: 2022-04-12T15:51:36+02:00
draft: false
description: ""
interact_with: " "
---

# Description

When using "mutable" infrastructure, servers have a long lifespan. They are provisionned once, and during their lifetime they will go through numerous changes.
The nature of these changes is very diverse, some are very simple modifications of configuration, some are upgrades of some applications services, some are OS kernel upgrades.

After a while, a server becomes more and more risky to modify, it becomes a real challenge to keep track of all past changes, and it is nearly impossible to explain why a specific setting was modified and when. 

These server have become what we call "Snowflake" servers. Servers that are the result of years of accumulated changes and upgrade. They are now impossible to reproduce, and a gradual configuration drift between the different environments has appeared : these production servers are not in sync with they corresponding staging servers. 

# What can be done

Immutable infrastructures are THE solution to this problem. If they are not applicable, "Infrastructure as code" tools such as Ansible coupled with proper configuration management can bring a lot of benefits to help uniformely execute the same changes on all servers, in all environments.

# Key patterns that can mitigate this problem

- Immutability 

# External Resources

[Martin Fowler blog post](https://martinfowler.com/bliki/SnowflakeServer.html)
