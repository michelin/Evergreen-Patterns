# Generic Capacity Planing Steps

Here we refer Capacity Planning as activities to understand the future needs of capacities of resources and define a actionable plan to guarantee the supply at committed time. 

Resources here include both IT hardware, software and services.

Capacity Planning is an art of balance. You'd ensure when required, you have the right resources with just right amounts, neither lack of resources, i.e under-capacity, nor waste of resources, i.e over-capacity. 

We breakdown Capacity Planning into following iterative steps:

````mermaid

flowchart TB
    subgraph Perimeter [1. Define Perimeter & Targets]
        A1[Identify types, characters of resources]
        A2[Confirm requirements with stakeholders]
        A3[Valid goals of plan]
        A4[Define targets of plan]
    end
    A1 --> A2 --> A3 --> A4
    subgraph Inventory[2. Initial Inventory]
        B1[Purchase]
        B2[Install]
    end
    B1 --> B2
    subgraph Monitor[3. Monitor for baseline]
        C1[Identify main factors]
        C2[Define golden signals]
        C3[Collect data]
        C4[Analyze patterns & trends]
    end
    C1 --> C2 --> C3 --> C4 --> C1
    subgraph Forecast[4. Forecast & Plan Evolution]
        D1[Secure Budget]
        subgraph Plan[Plan changes]
            DA1[Resource Types]
            DA2[Sourcing]
            DA3[Capacity Management Process]
            DA4[Organization]
        end
        D1 --- Plan
    end
    subgraph Act[5. Take Actions]
        E1[Replenish Stock]
        E2[Migrate to new capacities]
    end


    Perimeter --> Inventory --> Monitor --> Forecast --> Act
    E1 --> Inventory
    E2 --> Perimeter

````

# Capacity Planning for Azure Resources

## General Analysis
When we do Capacity Planning for resources on Azure, we should consider the facts that comparing to self-owned on-premise resources, they are
- 'almost' unlimited, available 'immediately', once you have the Enterprise Agreement settled.
- Can stop at anytime and 'usually' stop the charging immediatly
This means the Inventory step can be much lighter. However, it does NOT mean planning is no more important or needed. On the contrary, without careful planning and management, easy provisoning could cause over-book of resources and huge waste of money. 

So, the main concern of Capacity Planning on Azure is over-capacity. 

Azure resources could have 2 billing models, provisoned and pay-as-you-go. 

Provisioned ones, for example Premium Storage Account, you should careful plan before provision, and monitor the actual utilization once it is in use, and adjust timely when thresholds are met.
The thresholds can be defined based on generic best practices, and gradually tuned during run.

For Pay-As-You-Go resources, you do not worry too much at provisioning time. However, when resources are put in place, you'd start watching the trends, especially increase rate. Compare the rate with historical records or cross check with service consumption. So, monitoring pay-as-you-go resources should highly rely on teams who actually use the resources for upstream services, who has 1st hand info of the service consumptions.

## Monitoring Approaches
Sample: in Asia CDP (Consumer Data Platform) application, how do we apply above principles into the Capacity Monitoring.

- Managed Disks \
  Billing Model: Provsioned\
  Monitoring approach: By comparing (IOPS) to upper limit \
  The Premiumu SSD attached to CDH servers are either P20 or P30. We can monitor IOPS to see whether it is over-sized. We can compare A (the max IOPS of last 30 days) to B (upper limit of the tier). 
  - Over-sized: A < 50% * B
  - Under-sized: A > 80% * B
- Application Gateway \
  Billing Model: Provsioned with Min instance count + Auto-scale\
  Monitoring Approach: By comparing to highest watermark in last 30 days \
  For 2C applicatons, since we can not afford the tens of mins auto scale-out time, we have to ensure most of time, the min instance count can support the max capacity unit needs. The auto-scale is reserved for minimum service level during unexpected traffic surge. In such case, monitoring is to ensure fixed capacity unit is more than highest watermark in last 30 days, but not too much more, 200% buffer should be good enough. 
- Storage Account \
  Billing Model: pay-as-you-go\
  Monitoring Approach: By checking increase rate in last 30 days via a agreed threshold \
  Considering increasing needs from data-driven xxx, we think the storage size will keep increasing even with periodical cleanup. The key is to control the speed of increase at reasonable level. So we will monitor the volumn incease and aler based on the increase rate. 
- DataBricks \
  Billing Model: pay-as-you-go\
  Monitoring approach: By comparing run hours to average in last 30 days \ 
  DataBricks is charged based on computing time (of the VMs allocated to the workspace). It is difficult to check each jobs. We assume the total computing time in one month should be relatively stable, thus we compare the daily figure and average of 1 month. If it is 20% more than avg(last 30 days), we mark it as over-used. If it is 50% less than avg(last 30 days), we mark it as under-used.
- Data Factory \
  Billing Model: pay-as-you-go\
  Monitoring approach: By comparing run counts to average in last 30 days \
  Data Factory is charged by 1) Pipeline orchestration and execution 2) Data flow cluster execution and debugging (no applicable to our application) 3) Data Factory operations. (zero rate in our case). As DataBricks, we assume the total orchestration counts and data move hours in one month should be relatively stable, thus we compare the daily figure and average of 1 month. If it is 20% more than avg(last 30 days), we mark it as over-used. If it is 50% less than avg(last 30 days), we mark it as under-used. 


# To Be Continued 

