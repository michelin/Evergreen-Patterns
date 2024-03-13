---
title: Collecting Evidence
date: 2024-02-22T18:18:54+01:00
draft: false
status: reviewed
categories: 
 - running
tags: 
 - resilience
 - logging
 - system-analysis
 - mttr
description: "During a failure my systems retain relevant logs and data to enable both quick resolution and cold analysis."
---

![Card for Collecting Evidence.](/cards/capacity-planning.png)
![During a failure my systems retain relevant logs and data to enable both quick resolution and cold analysis.](/images/capacity-planning.webp)

# Description
The "Collecting Evidence" pattern is a strategic approach designed to ensure that, in the event of a failure, a system is capable of retaining critical logs and data. This capability enables not only quick remediation of issues but also allows for a detailed post-mortem analysis to prevent future occurrences. By systematically capturing and storing diagnostic information, systems adhering to this pattern can significantly reduce downtime and improve reliability over time.

# Key Principles
- **Comprehensive Logging**: Ensure every action, error, and transaction is logged with enough context to be useful without overwhelming the system or operators.
- **Data Retention Policies**: Define clear policies for how long different types of data are retained, balancing the need for analysis with the costs of storage.
- **Accessibility**: Make sure that logs and data are easily accessible to both automated systems and human operators for analysis and debugging purposes.
- **Security & Compliance**: Ensure that data collection and retention practices comply with relevant regulations and are secured against unauthorized access.

# Benefits
- **Quick Issue Resolution**: Immediate access to relevant data allows for faster diagnosis and fixing of issues, reducing system downtime.
- **Continuous Improvement**: Cold analysis of historical data enables the identification of patterns and weaknesses, informing future system improvements.
- **Operational Awareness**: Keeping detailed records supports a deeper understanding of system behavior under various conditions, aiding in capacity planning and performance tuning.
- **Compliance & Security**: Adhering to data retention and security standards not only ensures compliance but also helps in early detection of security breaches.

# Implementation Strategies
- **Structured Logging**: Implement structured logging to create detailed, easily parseable logs that can be dynamically queried.
- **Centralized Logging System**: Utilize a centralized logging system to aggregate logs from multiple sources, making it easier to search and analyze data.
- **Log Rotation & Archiving**: Implement log rotation and archiving strategies to manage the size of data retained actively while ensuring important information is not lost.
- **Automated Alerts & Analysis**: Use automated tools to generate alerts based on specific log patterns and to perform preliminary analysis, highlighting potential issues before they become critical.

# Conclusion
The "Collecting Evidence" pattern is a critical component of building resilient, scalable, and maintainable systems. By prioritizing the structured collection and retention of relevant system data, organizations can enhance their ability to respond quickly to issues, analyze and learn from past failures, and ensure system improvements are data-driven. This pattern not only supports operational excellence but also contributes to a culture of continuous improvement and compliance.