# User Stories

## Permissions (to be defined by hierarchy)

|Tag|Name|Description|
|---|---|---|
|WRK|Worker|Users without privilege only able to access machine information|
|MNT|Maintainer|Users able to observe information and perform operations on their assigned machine|
|MAN|Manager|Users that are able to observe and perform operations on a machine, as well as manage Maintainers' access to machines|
|ADM|Administrator|System administrators|

## example user story table 
### Worker
|Identifier|Name|Priority|Description|
|---|---|---|---|
|US001|See Homepage|High|As a manager, I want to be able to check the maintenance history so that I can gather information in order to schedule one. |
#

- See Dashboard Page: As a worker, I want to be able to see a dashboard containing information about the machines so that I can see which machines are available in the factory.  
- See Machine's Characteristics Page: As a worker, I want to be able to see a detailed page about a specific machine I choose so that I can monitor its current, real-time state. 
- See Machine's Characteristics' Log: As a worker, I want to be able to see a detailed log of a specific machine's characteristic so that I can monitor its state over time.
- See Machine's Production Workflow Page: As a worker, I want to be able to see a backwards and forwards timeline of a machine's job schedule, routing, resource allocation and work instructions so I can best monitor it. 
- See Maintenance Alerts: As a worker, I want to receive automatic maintenance alerts and schedules based on a machine's parameters and overall state so that I can always be updated on a machine's status.
- See Production Orders Status: As a worker, I want to be able to view a detailed log of every production order and its current status in order to identify bottlenecks or delays in real time.
- See Data Analysis Page: As a worker, I want to be able to see a dedicated data analytics page that focuses on production status, trends and historical data for each individual machine in order to better understand each machine's efficiency and work upon these results.
- Use Data Analytics Tools: As a worker, I want to make use of various analytics tools that can predict maintenance needs and optimize production processes, so that I can make any machine work more efficiently. 
- User-Friendly Data Display: As a worker, I want the data to be displayed in a intuitive way so that I more easily interpret it.

- Instruct Machine: As a maintainer I want to be able to perform on-the-spot operations on a machine so that I can work more efficiently.
- Control Machine Production Workflow: As a maintainer, I want to be able to create and manipulate a machine's production workflow in any way that I want, using a time-based scheduling system to define the wanted result, so that I can make sure the machine is working correctly and as intended.
- Define Performance Indicators: As a maintainer I want to be able to define a parameter's optimal thresholds as well as set performance targets for a machine so that I can better monitor its state and predict possible problems.

- Assign Mantainer: As a Manager I want to be able to assign mantainer roles, so that I can give permissions.