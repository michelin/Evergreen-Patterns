---
title: "Reliable Data Exchanges"
date: 2022-04-12T15:52:20+02:00
draft: false
categories:
- architecting
tags:
- architecting
description: "My data exchanges ensure consistency & integrity between systems"
featured_image: "/images/icons/reliable_data_exchanges.png"
---

# MAIN PURPOSE

Our different IT systems and applications exchange data, all the time.

We know that these data exchanges can be a major source of incidents and problems in our systems. There are numerous tools and architectures that aim to make these data exchanges as resilient as possible. Even with these precautions in place, everything fails eventually, so we want to ensure that our data flows and exchanges are easy to diagnose and analyze.

Making these data exchanges observable often needs to be addressed at the architecture level.


# WHAT TO DO

Being able to correlate information across the different systems is key. Different systems may use different IDs for the same business objects, so you need to have a mechanism in place to be able to correlate and map these different IDs to understand the complete lineage of the data, from the originating system to the last consumer.

Implementing verifications mechanisms to check that the integrity of the data received by an application is also a great way to improve the operability and ease investigations.


# EXAMPLES

### End to end visibility

Several strategies can be followed to implement end to end visibility in data exchanges.

First, you need to know and understand how the architecture can already answer parts of the problem. Modern architectures and tools can often provide rich visibility out of the box, and you shouldn’t reinvent the wheel (When using Kafka, API Managers, … take the time to understand what the tools already make observable).


[OpenTelemetry Traces](https://opentelemetry.io/docs/reference/specification/overview/#tracing-signal) is a technology that is also getting more and more traction on the observability market. There are SDKs for numerous languages that you can use to describe standard OpenTelemetry transactions that can be analyzed and visualized in numerous standard tools. This should be the preferred way to implement such a requirement.

You will not always have complete freedom in the implementation of this feature, because you may be interfacing with legacies or with software packages. Even in this case, there are some strategies that may be applicable:

* Reuse the same record identifiers across systems

* Locally store the different identifiers mapping

* Introduce unique transaction identifiers by using UUIDs (Universally Unique Identifier) and propagate these across systems as much as possible

An UUID is a very useful data type looks like this

123e4567-e89b-12d3-a456-426655440000

Use it each time you need a **unique** value

* One line of code to generate: *new UUID()*;

* Unique: To generate the same value twice you would need to generate 1 billion UUIDs per second for about 85 years



### Automated data integrity checks

For this requirement also start by understanding what is already offered and implemented by design in the tools and architectures that you use (schema validation, checksums, ...).

For mass data loading, verifying the integrity and correctness of the data integrated after a batch integration is **essential**.

There are several strategies that can be used

* A simple checksum mechanism: verify after loading that the sum of an amount attribute of all lines inserted are the same as in the input

* A deep comparison of all inserted lines: Can be costly but can be implemented by third party tools (Data Quality tools like OEDQ)

This may require the sending source to be verified along with the data

* These strategies must be built on top of transport-level integrity checking such as hash comparisons (md5sums, …) to ensure files were not tampered with or corrupted during network transfer. This may be **already built-in** if using dedicated data transfer tools. 

 

 

 

 

 

