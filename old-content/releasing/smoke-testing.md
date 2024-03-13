---
title: "Smoke Testing"
date: 2022-04-12T15:59:09+02:00
draft: false
categories:
- releasing
description: "I have automated tests which validate the most critical functionalities, enabling early post change validation"
interact_with: "toil_routine, change_aversion"
---


# Main Purpose

An origin of the term smoke test comes from electronic hardware testing. If you see smoke coming from the board when you plug in a new board and turn on the power, then you can turn off the power and stop the test.

Another possible origin of the term comes from the plumbing industry: smoke is created and blown into tubing, and then the pipes are examined to make sure no smoke is escaping to verify that there is no leak.

In software development the goal of Smoke Testing is to automate the tests which validate that the most critical functionalities of a system are working.

Smoke tests are mainly used after a start of the system or one of its components, typically following a release, a security patch, a restart, …



The benefits of automating those tests are:

* they are performed faster, meaning the service is restored faster

* they are more reliable (not forgotten steps)

* they can be launched by more people (for example on-call people during the night or weekends).

* they can also be used on non-production environments (training, acceptance) before they are to be used



# How it works

The first step is to identify which functionalities are core and must be tested. The goal is to make sure that all components are well started and are communicating with each other.



Then define test cases that will show if those functionalities are working. The purpose of those test cases is not to go in depth into the application, but rather to make sure as quickly as possible that the application and its components has been started correctly. Each test case should help identify if and where there is an issue.



Finally, those test cases must be encoded in an automation tool that will allow them to be performed automatically to provide a status indicating which functions/components are working or not.

# Example

Example of smoke test scenario:

1) go to the application login page: this will tell if the application server is started.

2) log in the application: this will tell whether the LDAP authentication is working

3) perform a search on an existing object: this will tell if the link with the DB is working

4) perform a query that will trigger a call to another application: this will test if the connection to the other application is working

5) etc … 

