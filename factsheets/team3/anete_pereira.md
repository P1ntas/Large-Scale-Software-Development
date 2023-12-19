# Factsheet for Anete Pereira

## Sprint 0

While I successfully set up Grafana on Docker containers, ensuring a stable development environment, my contributions during this sprint were limited and I didn't make any substancial constributions to the project, as this sprint 0 primarily focused on creating user stories, defining the vision of the product and related content. 


### The two user stories that I am most proud of

This can include user stories that you have written or refined during the sprint. If it was a refinement, explain what you have added or changed.

 * #1
 * #2


### The two pull requests that I am most proud of

This can include PRs that you have implemented or reviewed during the sprint.

 * #3
 * #4


### Two contributions of other types that I am most proud of

This can be anything that you think worked particularly well and benefited the project as whole, from a hard conversation with the PO that worked out very well, to the adoption of a new framework or library. 



## Sprint 1

As stated in the development document, the work the team developed during this sprint was mainly related to implementing automatic notifications linked to the data visualization interface, Grafana, and its dashboards. 

### Two user stories that I am most proud of

 * [#5](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/5) - Implemented an automatic notification for testing purposes with different data and delivery endpoints

### The two pull requests that I am most proud of

None relevant

### Two contributions of other types that I am most proud of 

We successfully achieved this testing the implementation both with an email endpoint and a Discord bot (webhook). This helped us prove that having real-time notifications is feasible, and the pull request with the complete code for this feature will be done during sprint 2, when we have real-time data being streamed to the dashboards, as only then we can create more types of notifications and complete the testing process. We also need to figure out a way to ensure user acknowledgement and tracking.


## Sprint 2

This sprint, the first important task that was done was tackle the unexpected setup complexities, particularly with the dynamic data generators, based on Dinasore and 4DIAC-IDE. After this, the work progressed swiftly and we were able to quickly implement various notifications for sensors (e.g. value is higher than X, value is lower than Y). Also, when the values are restored to normal conditions, another automatic notificarion is sent, but this time marking the problem as resolved. Despite being complete, thi feature might need refinement in teh future, as new data types arise and more data is available, which will enable us to define more suitable ranges for each type of sensor (e.g. temperature, pressure, etc.). So, adaptability and problem-solving skills were evident in addressing challenges related to the project setup and the integration of the Prometheus data simulator in this sprint, and, despite setbacks, everyone contributed significantly to the successful implementation of the assigned user story.

### The user storie that I am most proud of

 * [#5](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/5) - Implemented automatic notifications based on value ranges for sensor dynamic data

 ### The pull request that I am most proud of

* [#91](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/91)  - Implemented alerting/notification features

 ### Two contributions of other types that I am most proud of

During this sprint we could successfully overcome the initial setup difficulties, and we were able to implement the automatic notifications feature using dynamic data, which was the main goal of this sprint.

More testing, validation and betetr organization of the repository and overall work was also a point of focus during this sprint. Also, code review was taken more seriously, and we were able to improve the quality of the code that was being pushed to the dev branch.


## Sprint 3

During this sprint, my primary focus was on advancing the subtask associated with our user story, specifically pertaining to the display of performance indicators through a user-friendly interface. To lay the groundwork for this task, I got into the extensive documentation provided by Grafana.The link [https://grafana.com/docs/grafana-cloud/introduction/metrics-and-visualizations/] served as a valuable resource, providing insights into the nuances of visualization options within the Grafana ecosystem. 
I also dug deep into Grafana interface, checking out different ways to show our data in an easy-to-understand way. This part was super important for planning how our performance indicators will look. Even though I didn’t chenge the actual interface yet because we don’t have access to the real data of the machines, all this research sets us up well. It makes sure that when we have the data, we're on the right track to make our performance indicators look awesome and easy for everyone to use.

### The user storie that I am most proud of

* None relevant, as we did not implement any code.

 ### The pull request that I am most proud of

* None relevant, as we did not implement any code.

 ### Two contributions of other types that I am most proud of
With the knowledge that I acquired during this research, I helped my team members to better understand the grafana interface. 


## Sprint 4

During sprint 4, my primary focus was on refining the parameters which define the triggering of notifications to align with their specific contexts, as outlined in our revised user storie. This involved a comprehensive review and adjustment of the notification system to ensure that alerts are generated based on relevant criteria. To facilitate this task, I explored various documentation sources related to this. A key reference was the [Grafana Alerting Documentation](https://grafana.com/docs/grafana/latest/alerting/), which provided valuable insights into configuring notification parameters and aligning them with our project's requirements. Unlike in sprint 2 where mock data was utilized, this sprint involved practical and more realistic adjustments to the notification system.

### The user storie that I am most proud of

* [#5](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/5) - Implemented automatic notifications based on value ranges for sensor dynamic data - updated to feature Go's templating language and more accurate parameters

 ### The pull request that I am most proud of

* [#151](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/151)

 ### Two contributions of other types that I am most proud of 
Applied acquired knowledge to guide team members in understanding the new values of parameters set in the notifications and how it was done.
I worked closely with Jose to implement this new part of our user storie, mainly doing pair programming.

## Overall Product

Reflect on your specific contributions to the product, technically and as perceived by a user, along the three dimensions below (see Dashboard > Final outcomes > Product). Keep each section below to a maximum of 50 words.


### Technical Soundness


I think that my contributions to the project were technically sound. I was able to implement the notifications feature, which was the main goal of our user story, and I also researched about the grafana interface, which was very important for the development of our project and allowed our implementation to be understandable, maintainable and scalable, exhibitiing good applications of the chosen technologies.



### Product Realization


Transforming ideas into reality wasn't always straightforward. However, what we could implement was functional Grafana notifications — a proof of successful component integration within our project. We think the product seems professional and effectively satisfies the requirements with viable solutions, making it ready to be delivered.



### Value for the Client


I think that my work was valuable for the client. The alerting features our team implemented are crucial for monitoring the machines and identify anomalies, enhancing the client's performance and overall happinness.

