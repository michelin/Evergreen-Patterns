---
title: "Application Logging"
date: 2022-04-12T15:54:25+02:00
draft: false
categories:
- building
tags:
- building
description: "My systems log information necessary for troubleshooting and monitoring"
interact_with: "normal_errors, rushing_to_solution, untracked_operations"
---

# MAIN PURPOSE

Application logging is the process of saving application events. With this information in hand, the team can assess threats and analyze errors before they disrupt the service.
They are the most helpful and reliable evidence to conduct a proper root cause analysis of an incident.

Application logs are not used just for averting operational problems, but also to provide business intelligence through data mining.

# HOW IT WORKS?

In order help you and standardize the process of logging, you should use frameworks like for the Java platform. Several Java logging frameworks exist.  Log4J is one of them. 

![application logging](/images/building/application_logging1.png)

There are 3 main components

Logger:  Loggers in Java are objects which trigger log events. They are created and called in the code of the application, where Log Events are generated, before passing them to the next component which is an Appender

Appender : Appenders are responsible for delivering LogEvents to their destination, it can be file ,database , standard output, …

Layout : It is used by  the Appender to format what your are logging

# WHAT TO LOG
We can organize in 5 main categories the most important things your application have to log..

**Requests**  
Record each request or invocation of service within the application. This includes service or API access, application access, authentication and authorization.

**Audit Trail**
We are talking about changes that have been made to your data. Any change to data including creating new data, updating or deleting data.

**Threats and vulnerabilities**
Log suspicious human activities (e.g., failed authentication). When a suspicious event is noticed, make sure the logs capture all information related to it

**System events**
System events must capture information on behaviors like starts, stops, restarts, but also regarding communication connects, disconnects, reconnects, retry events

**Performance**
Faults and exceptions that can impact the availability or stability of the system. These include exceeded capacity limit or resource usage, system errors or bugs, connectivity issues, slow response times or unhandled errors.

# WHAT NOT TO LOG

At least do not log information related to security.
It can be security credentials like passwords, security keys and secrets, auth tokens, but also personal information  
Be mindful of such sensitive information and keep it away from the logs.



# BEST PRATICES

Here are examples of best practices regarding application logging.

Log entries should answer the following questions:
**who** *(username)*, **when** *(timestamp)*, **where** *(context,database)*, **what** *(command)*, **result** *(exception)*


**Log Level**
The log level is used to denote the severity of each event in the system. In most logging frameworks, the following levels are available:
Fatal, Error , Warn, Info, Debug, Trace .


**Friendly Log Message (short & sweet )**  
Make every log message meaningful and related to the context.
If you log too little, we may not be able to capture adequate information, If you log too much, it will end up with performance or space disk issues.

**Be Able to Configure the active log level**
Based on the context (deployment environment, incident,..)  the active log level also must be changed

**Use timestamps**  
Make sure that the timestamp is placed at the beginning of the log message with yyyy-mm-dd HH:mm:ss .

**Use the English language**  
Some tools and terminal consoles do not support printing and storing log messages with certain Unicode characters and our support team are located all over the world



# MOST COMMON MISTAKES

**Database logging**
Avoid using a database for logging, database should contain mostly functional data, technical data like logs are better placed in external files that are easier to access and parse.

**Gratuitous logging**
Often, this is not caught until the system is in or near production.

During test cycles, cluttered application logs are often attributed to open defects

This is part of the technical debt; this is a reason why logs are not used!!

**« Normal » or « expected » errors !!**
This is part of the technical debt; this is a reason why logs are not used!!

**Insufficient or obtuse error logging**

Messages are frequently logged at the wrong severity level.

No reliable way to correlate user events with logged exceptions  
Insufficient detail in error messages when they are logged


# EXAMPLES


**Implementation examples**
SLF4J
LOGBACK
SPLUNK for the Web interface access

Ex : LogBack  

![application logging](/images/building/application_logging2.png)

