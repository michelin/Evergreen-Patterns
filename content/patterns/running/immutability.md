---
title: "Immutability"
image: "immutability.png"
date: 2022-04-12T12:28:04+02:00
draft: false
families:
  - running
description:
featured_image: "/images/icons/immutabillity.png"
---

# MAIN PURPOSE

In a traditional server infrastructure, servers are continually updated and modified in place. Teams working with this kind of infrastructure log into their servers to manually upgrade or downgrade components, modify configuration files, and deploy new applications directly. These servers are mutable; they are changed after they’re created.

Some  typical problems of mutable infrastructures are the following:

* Each server has a different configuration, often called ‘configuration drift’.

* Technical issues which are hard to find or reproduce

* Changes done to the server are not always tracked as there is not automated way to do it.

* Servers changing over time are unique, difficult to reproduce and become “Snowflake servers”,

* Configuration is tailored for each server and becomes a time-consuming process.



An immutable infrastructure is another infrastructure paradigm in which servers are never modified after they’re created. If something needs to be updated, fixed, or modified in any way, completely new servers are built from a common image with the appropriate changes and are provisioned to replace the old ones (sometimes referred to as “Phoenix” servers in opposition to “Snowflake servers”). After they’re validated, they’re put into use and the old ones are quickly decommissioned.

The benefits of an immutable infrastructure include more consistency and reliability in your infrastructure and a simpler and much more predictable deployment process.

Main benefits of immutable infrastructures:

* Provides consistent configuration across all environments, eases testing and incident reproducibility

* More secure, as interactive logins on immutable servers are not expected and very easy to track

* There is no room for configuration drift. The accurate state of each server is known and stored in source control.

* Servers can be destroyed and rebuilt at will, even on local development environments



# WHAT TO DO

Immutable infrastructure is strongly correlated with the concept of infrastructure as a code. Using it efficiently includes comprehensive deployment automation, fast server provisioning ideally in a cloud computing environment, and solutions for handling stateful (functional business data) or ephemeral data like logs.

For all these reasons, immutable infrastructure is highly associated with the DevOps practice. DevOps includes culture and tools that works to achieve agile development with continuous delivery. And continues delivery drives immutable infrastructure.

Container based solutions are Immutable “by design”, containers being built from a base image, and changes to this base image described in source control management.



# BEST PRACTICES

Everything as code, test, local environments, run as CI / CD jobs



# EXAMPLES

Some of the most popular tools to build Immutable infrastructure:

* Terraform, for server provisioning

* Ansible, for post-provisioning configuration



# EXTERNAL RESOURCE

[ImmutableServer (martinfowler.com)](https://martinfowler.com/bliki/ImmutableServer.html)


[PhoenixServer (martinfowler.com)](https://martinfowler.com/bliki/PhoenixServer.html)

[SnowflakeServer (martinfowler.com)](https://martinfowler.com/bliki/SnowflakeServer.html)


[Configuration Drift - kief.com ](http://kief.com/configuration-drift.html)

