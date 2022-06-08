---
title: "Collecting Evidence"
date: 2022-04-12T16:02:59+02:00
draft: false
categories:
- running
description:
featured_image: "/images/icons/collecting-evidence.png"
---


# Main Purpose

The purpose of Collecting Evidence is to make sure to gather and preserve all elements (application logs, system logs, memory dumps, temporary files, …) that can be used to determine the root cause of an incident.

Those elements must be collected as soon as possible to make sure that no manual action has been performed that could alter the system’s state. Ideally, the system itself should make it automatic or at least easy.

# When to use it?

When an incident occurs, it is of course important to restore the service as soon as possible, but it is also important to take some (reasonable) time to collect the elements that will allow to perform later a deeper analysis to find the root cause and hopefully fix the issue.

Too often, people will be tempted to rush for the resolution to fix the problem (by restarting the application or the server for example), which will prevent some analysis in the future : core dump will not be possible once the application or server has been restarted, the logs policy may be to keep them a few days only (meaning precious information may be lost when expert are available to analyze them), the data in the DB will have changed making it impossible to reproduce a crash, …

Depending on the context (system’s criticality, recurring issues, …) those evidence may be collected on each failure or only in some cases (for example if the application has been crashing several times in a row).

# How it works

It is important to have a list of elements that must be kept, and to define how to collect them (command and options / parameters, scripts, …), and where to store them before further analysis.

To reduce the amount of time needed to collect the evidence and to be sure not to forget any element, one or several scripts can be written in advance and launched whenever needed.

Some elements can have a significant size (core dumps or memory dumps for example can be very large): you must therefore have enough space dedicated to store them and make sure that they will not consume the space needed by your system to run. You should determine the space needed to store those elements and make sure it is available (or can be made available on demand on a very short time).



# Example

Your application may have a flag that tells whether it has been stopped properly or not (you could set this flag in a script that stops you application for example). When your application is started, it could check this flag and if it detects that the application has not been stopped correctly then it could backup some key elements (last logs, last DB transactions, …). 
