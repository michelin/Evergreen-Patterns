---
title: "Users"
date: 2022-05-29T15:32:37+02:00
draft: false
description: "You never know how users will use a system"
featured_image: "/images/anti-patterns/users.jpg"
---

# Description

Users will use the system you build and design in ways you have never envisionned. It can have several reasons. Maybe they were not trained adequatly or maybe they are just very creative. Classical testing methods can not catch everything before the first go-live of your system.

# Some typical examples

- Administrators of the application may have access to configuration features that can be dangerous if not understood properly. They can easily break the complete system by entering wrong settings. 
- Users will sometimes double-click or even triple click links when they have been waiting for too long for a UI to respond.
- Users can create links in their browser to directly access specific pages which were not designed to be accessed directly.

# Key patterns that can mitigate this problem

- Chaos Engineering
- Bulkheads
- Embrace Failures
