---
title: "Capacity Planning"
date: 2022-04-14T08:48:43+02:00
draft: false
categories:
- running
tags:
- running
description: ""
featured_image: "/images/icons/capacity_planning.png"
---

# Definition

From Wikipedia, "Capacity planning is the process of determining the production capacity needed by an organization to meet changing demands for its products."

In the IT world, it is as a synonym for capacity management which is the term used by ITIL. IT capacity planning involves estimating the storage, computer hardware, software and connection infrastructure resources required over some future period of time.

Capacity planning is very important for IT systems, because you wan't to avoid facing capacity issues that will directly translate to outages. You want to monitor the resource usage of your systems in order to understand what are the trends.

Capacity planning is done on a perimeter, which needs to be clearly defined. It can be done at a data center level, a cluster level, a single business application level, but in all of these cases the overall approach will be very similar.

You also need to know what are the applicable scaling strategies that can be applied to your context. For application, stateless, cloud native architectures that follow the "12 factors" are easy to scale horizontally (easy: deployed on any number of small and cheap server nodes) but older, monolithics, applications will maybe only be able to scale vertically (harder as you will need to upgrade to more expensive and powerful machines to host them). 

# Macro steps

1. Define the actual perimeter of the planning

A complete data Center, a single business application, a Kafka cluster, ....

2. Initial *Inventory* of this perimeter

Produce a detailled inventory of this perimeter. For example, total number of CPUs, memory, storage, that is currently being consumed.

3. *Monitoring* of the usage of these resources to create an initial baseline

Determine what is the current saturation of these resources, and put in place a precise monitoring.

4. Determine what are the main variables impacting the saturation of the resources

Most of the time, the actual usage of your system is the main variable that has an impact of the saturation of the resources, typically the number of users that use it. But there also may be other variables to consider, and systems to systems communication can also greatly impact system performance, you may for example determine that the number of orders is the main variable that has an impact on the performance of your billing system, so this is the variable you want to capture.

Of course, depending on the complexity of the perimeter you are working on, you will probably identify several variables in this step.

5. Forecast evolution of these variables

Maybe the most difficult step, this is where you will attempt to forecast the variation in the usage. You will typically need to involve other people and teams to help you determine what could be the evolution of the different variables in the future (short, medium or long term).

AI ops tools can also help you forecast these variables with machine learning algorithms that can accuratelty detect trends and seasonality.

6. Act

The forecasting will help you determine what are the urgent short term actions that you need to execute to keep saturation levels acceptable and avoid outages.
At a longer term, it is a tool that will help you better prepare for more strategic transformations of your infrastucture needs.


# External Resources

[The 12 factors app](https://12factor.net/)

[The wikipedia page about Capacity Planning](https://en.wikipedia.org/wiki/Capacity_planning)
