# Factsheet for Eduardo Silva

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

## Sprint 1

As stated in the development document, the work the team developed during this sprint was mainly related to implementing automatic notifications linked to the data visualization interface, Grafana, and its dashboards. 

### The two user stories that I am most proud of

 * [#5](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/5) - Implemented an automatic notification for testing purposes with different data and delivery endpoints


### The two pull requests that I am most proud of

None relevant


### Two contributions of other types that I am most proud of

We successfully achieved the objectives for this sprint, testing the implementation of the notifications both with an email endpoint and a Discord bot (webhook). The tasks developed during this sprint helped us prove that having real-time notifications is feasible, and the pull request with the complete code for this feature will be done during sprint 2, when we have real-time data being streamed to the dashboards, as only then we can create more types of notifications and complete the testing process. We also need to figure out a way to ensure user acknowledgement and tracking.


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

During this phase of the project, I delved into understanding how to reinforce the security and access control measures for our Grafana system, particularly about safeguarding the data and configuration of performance indicators. My research involved a thorough investigation into methods for enhancing the security features of Grafana. Although the direct implementation is yet to be initiated, this research ensures a nuanced understanding of security measures, paving the way for the future implementation of strict access controls and data security protocols for our indicator configurations.

These links emerged during our exploration: 
- [Grafana roles and permissions documentation](https://grafana.com/docs/grafana/latest/administration/roles-and-permissions/access-control/custom-role-actions-scopes/)
- [Grafana security blog post](https://grafana.com/blog/2022/02/22/how-secure-is-your-grafana-instance-what-you-need-to-know/)

They proved to be a source of information, offering insights into best practices and strategies for augmenting the security landscape of Grafana.

### The user storie that I am most proud of

* None relevant, as we did not implement any code.

 ### The pull request that I am most proud of

* None relevant, as we did not implement any code.

 ### Two contributions of other types that I am most proud of

During this sprint I collaborated closely with José to better undersand the security concerns and features of Grafana.

## Sprint 4

During this current sprint, my focus shifted towards enhancing project communication and notification systems. Specifically, I concentrated on optimizing the notification process using a templating language for our project. I delved into understanding the intricacies of crafting effective and dynamic notifications that can be customized using templates, helping other team members to further enhance this feature we had already developed. I also understood the new parameters for notifications which were implemented by another part of the team.

### The user storie that I am most proud of

* [#5](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/5) - Implemented automatic notifications based on value ranges for sensor dynamic data - updated to feature Go's templating language and more accurate parameters

 ### The pull request that I am most proud of

 * [#151](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/151)

 ### Two contributions of other types that I am most proud of

During this sprint I worked mainly with Afonso and Hugo to make the notifications format better using Go´s templating language.

## Overall Product

Reflect on your specific contributions to the product, technically and as perceived by a user, along the three dimensions below (see Dashboard > Final outcomes > Product). Keep each section below to a maximum of 50 words.


### Technical Soundness

I made substantial, technically proficient contributions to the project, successfuly implementing the tasks that were assigned to me. I also always tried to follow the established project guidelines and coding standards.


### Product Realization

I think overall, the product could have been improved in its usability and user-friendliness. However, I think my contributions helped to make this issue less relevant, as I was able to implement simple and effective notifications with my team.


### Value for the Client

In my point of view, the client will be satisfied with the final product, at least with the features that we implemented. They work and will be useful for the client once we have real data and parameters for the notifications.
