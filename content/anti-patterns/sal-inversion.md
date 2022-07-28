---
title: "SLA Inversion"
date: 2022-04-12T15:51:36+02:00
draft: false
description: ""
featured_image: ""
---

# DESCRIPTION

An IT system has all kind of dependencies which it requires to deliver the service to its end users. 
Typical examples are authentication and storage services but there are also some core low level facilities such as DNS servers and load balancers which are required for the system to function properly. 
All of these dependencies will have an impact on the availability of the system when they go down (and they will!). 
Depending on how the system is coupled with the particular dependency that is failing, the impact may be more or less significant. 
If the system is highly coupled with the dependency then this failure may completely bring the entire system down. You want to avoid your system being highly coupled with dependencies which do not implement enough high availability measures for your requirements. 
Also the blast-radius of a failure in one of your dependencies will be different, for example a printing server failure will probably only impact features that are related to printing whereas an authentication service failure will make your entire application unavailable. 

# What can be done

It is important to know which are the different SLA promised by your different dependencies and to indentify the nature of coupling you have with them. 
-	Ensure that the core dependencies that are common to all your applications and that would bring your entire system down implement the best in class high-availability measures (DNS, Auth services should be very highly available, and ideally leverage managed and scalable cloud services) 
-	Avoid coupling with other third-party applications if you can, for example by introducing asynchronous data exchanges instead of synchronous API calls 

# Key patterns that can mitigate this problem

- Decoupling 
