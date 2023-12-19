# Factsheet for José Sousa

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
Throughout this project phase, I dedicated substantial time to researching ways to enhance the security and access control measures for our Grafana system, with a specific focus on safeguarding the data and configuration of performance indicators.
I collaborated with my colleague, Eduardo, who was also working on this aspect of the project. Together, we shared insights, discussed findings, and coordinated our efforts to streamline our approach in fortifying the security of our Grafana instance. While the direct implementation is pending, this collaborative research helped us understand security measures.

### The user storie that I am most proud of

* None relevant, as we did not implement any code.

 ### The pull request that I am most proud of

* None relevant, as we did not implement any code.

 ### Two contributions of other types that I am most proud of

I collaborated with Eduardo and the rest of the team to enhance the workflow and share ideas.

## Sprint 4

In sprint 4, I focused on fine-tuning notification triggers to match the details in our updated user stories. I had to analyze the new data which was introduced in the project in order to find the best set of parameters that would regulate the notifications sent by Grafana.

### The user storie that I am most proud of

* [#5](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/5) - Implemented automatic notifications based on value ranges for sensor dynamic data - updated to feature Go's templating language and more accurate parameters

 ### The pull request that I am most proud of

* [#151](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/151)

 ### Two contributions of other types that I am most proud of 
I discussed my ideas with other team members.
I worked closely with Anete in pair programming.

## Overall Product

Reflect on your specific contributions to the product, technically and as perceived by a user, along the three dimensions below (see Dashboard > Final outcomes > Product). Keep each section below to a maximum of 50 words.


### Technical Soundness

I always used the available technologies and tried to extract the most value from them, so I think that my contributions to the project were technically sound. For all of the user stories we were assigned,followed this mentality, and we were able to implement them successfully, creating robust solutions that showed a good application of the technologies.


### Product Realization

All of our features were implemented, however I think that the notifications could be improveed in the future, as for all of the  project we didn't have access to real data, so we could not define the best parameters, for example. I think the client was also responsible for this.
Despite the setbacks I think the set of features implemented allow a viable product for the problem at hand, making it have a professional look and feel, exhibiting the quality attributes required while obeying the constraints imposed. 


### Value for the Client

I think overall the final product still holds value for the client, as the features we and the other teams implemented allow to perform the main objectives established in the beginning of the project. However, this is still a base that could be improved with real data. All in all, I think the client will be happy with the product we delivered.