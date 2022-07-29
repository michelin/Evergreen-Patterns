---
title: "Progressive Roll Out"
date: 2022-04-12T17:46:08+02:00
draft: false
categories:
- releasing
tags:
- releasing
description: "My systems can be deployed in small increments and enable easy upgrade or roll-back"
interact_with: "big_bang_deployment, change_aversion"
---

# Main Purpose

Traditionally, a new product or feature would be released in its full form, to every user at the exact same time. Using progressive roll-out, that same new product or feature would be released in smaller forms, to a few user groups at a time, and in stage intervals.

Progressive roll-out let you break up “big bang” releases into smaller, more manageable increments thus reducing the risks and making roll-back easier.



# When to use it?

Progressive rollout lets you test a new version with a limited set of users, which has many benefits:

* it allows to see how users are reacting to the new version and therefore adapt change management if needed

* if any unanticipated issue occurs, you can pause the rollout, fix the issue, and move ahead. Or you can rollback if required while fixing the issue.

* it allows you to see how new components behave and handle the load in real life environment and how much resources they consume (CPU, RAM, I/O, network, …)

* for cloud-based applications, the resource consumption allows to anticipate the costs

This is therefore especially useful when releasing new significant features or releases.

# How it works

There are different ways to achieve a progressive rollout:

* Canary release: you redirect a portion of your users to the new version before fully rolling out to all users. The users that are redirected can be specific users, a specific category of users, users of a specific location, …

* Feature flagging: new features can be activated using a flag, and for specific users only if needed



Identify sample audience:

* Specific users

* A subset of users (X%)

* A specific category of users

* ...



Identify the success criteria: pass/fail conditions and metrics to watch

Plan the rest of the progressive roll-out 
