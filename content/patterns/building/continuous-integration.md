---
title: "Continuous Integration"
date: 2022-04-12T15:54:49+02:00
draft: false
categories:
- building
tags:
- building
description: "Committed changes automatically trigger the build of the entire application as well as the automated tests"
featured_image: "/images/icons/continuous_integration.png"
---


# MAIN PURPOSE

Continuous Integration (CI) is a software development practice, where automated builds can be triggered by some sort of event, such as a code check-in or merge.
It is part of the Continuous Integration/Continuous Deployment pipeline practice.

# GOAL

When you see continuous in a pattern name, one of the idea behind it is that by doing an action continuously, therefore by small steps, you will be able to automate it and it will make life dramatically easier.

Even if one of the main goal of Continuous Integration is to reduce the risk, the benefits can be multiple for IT and business.

For IT it can help to improve metrics like deployment frequency, MTTR or Change failure but it will also help you to find problems more easily.

For Business, you will be able to bring value faster by iterating faster and introducing less bugs/errors into production.



# HOW IT WORKS?

Each integration is verified by automated steps but also triggers automated tests to detect integration errors as quickly as possible and deliver a release ready to be deployed by the continuous deployment pipeline.

How continuous integration works

![continuous integration](/images/building/continuous_integration1.png)


Automated testing reduces the chances of human error and ensures that only code that meets certain standards makes it into production



# BEST PRATICES

Here a few examples of best practices regarding Continuous Integration.

Single Source Repo : this is the first step for Continuous Integration , without it, nothing more can be done

Automated:  By continuous we mean automatic and each task needs to be automated (build but also testing)

Commit every day: By doing this frequently, developers quickly find out if there's a conflict between two developments



# EXAMPLES

There are many tools for software development using the continuous
methodologies, GitLab CI/CD is one of the most famous  
