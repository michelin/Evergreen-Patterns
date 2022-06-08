---
title: "Up To Date Inventory"
date: 2022-04-12T16:02:59+02:00
draft: false
categories:
- running
description:
featured_image: "/images/icons/up_to_date_inventory.png"
---


# MAIN PURPOSE

IT assets are both expensive to acquire and maintain. As a result, asset management plays a critical role in helping teams ensure the efficient use of resources (availability, up to date, etc.), while supporting the needs of users and business functions.

This is something that is required for many actions, such as

* Incident anticipation, fast detection and diagnosis

* Change impact assessment

* Obsolescence management

* Security vulnerability analysis

* Technical evolutions and modernization management

* Correction and patching assessment and execution follow up

* Duplication or decommissioning assessment and execution follow up

* Cost management

* Digital sustainability assessment

* …



# GOAL

The objective is to have a unique repository with all the elements that make up a system. This data warehouse must allow to know all the components and their characteristics, whether they are material or immaterial. This information is also completed by the dependencies between the different elements. All these links must allow for different views, both from a business and technical perspective.

The first benefit of this work is a better knowledge shared by all the stakeholders of the system.

It saves time in a lot of activities mentioned above, for example

* For the support teams daily work. The mastery allows to quickly identify the source of a malfunction or the workaround to apply (reduce the MTTR – Mean Time To Recover)

* For any analysis or update work. By having the information, maintenance can be better anticipated and planned.

* For any risk analysis: the set of characteristics allows to quickly identify the group of components concerned

This work, beyond the initial inventory, is to be carried out at each change of the system. This allows you to always rethink the reality.



# WHAT NEEDS TO BE DONE


This starts with a collecting of all the technical components, applications, ....  All the information must be described. A strategy of completeness can be implemented through the various changes, or during disaster recovery plan, during the migration of infrastructure, .... (it is advisable to strongly automate these activities … as “Time is Precious” , please refer to that pattern).

This continues by identifying the tree structure that links the different items together. This is a long and time consuming task that must be continuously maintained as changes occur all the time



# EXAMPLES



All servers can be scanned and integrated into the reference database. For each of them, we will recover the technical characteristics as well as the version level of the OS for example. This information will then be completed in the data lake by a scan of the various services present on these servers (application, database, ....). The link between the two elements will then be identified. The tree structure will be completed by indicating that the business process is served by these elements



After this initialization step (simplified) it is time to take advantage of this effort


Let's take examples of contributions in the case of an incident impacting a physical server.

* The support teams will very quickly identify the various VMs hosted on the server to determine the impact in a trustworthy way.

* They will automatically retrieve the impacted business processes to communicate with users.

* This will contribute to the implementation of actions/checks to get each component back up and running more quickly. 
