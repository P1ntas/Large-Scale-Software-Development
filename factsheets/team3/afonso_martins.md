# Factsheet for Afonso Martins

## Sprint 0

Sprint 0 was a crucial initial phase dedicated to shaping the project's roadmap by crafting user stories and related content. As the Scrum Master, my contributions, while less prominent in terms of direct development work, played an essential role in orchestrating the team's efforts and ensuring the success of this preparatory phase.

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

### The two user stories that I am most proud of

 * [#5](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/5) - Implemented an automatic notification for testing purposes with different data and delivery endpoints


### The two pull requests that I am most proud of

None relevant


### Two contributions of other types that I am most proud of

We successfully achieved the objectives for this sprint, testing the implementation of the notifications both with an email endpoint and a Discord bot (webhook). The tasks developed during this sprint helped us prove that having real-time notifications is feasible, and the pull request with the complete code for this feature will be done during sprint 2, when we have real-time data being streamed to the dashboards, as only then we can create more types of notifications and complete the testing process. We also need to figure out a way to ensure user acknowledgement and tracking.

As a Scrum Master, I also helped organize the team’s workflow during the sprint.


## Sprint 2

This sprint, the first important task that was done was tackle the unexpected setup complexities, particularly with the dynamic data generators, based on Dinasore and 4DIAC-IDE. After this, the work progressed swiftly and we were able to quickly implement various notifications for sensors (e.g. value is higher than X, value is lower than Y). Also, when the values are restored to normal conditions, another automatic notificarion is sent, but this time marking the problem as resolved. Despite being complete, thi feature might need refinement in teh future, as new data types arise and more data is available, which will enable us to define more suitable ranges for each type of sensor (e.g. temperature, pressure, etc.). So, adaptability and problem-solving skills were evident in addressing challenges related to the project setup and the integration of the Prometheus data simulator in this sprint, and, despite setbacks, everyone contributed significantly to the successful implementation of the assigned user story.

As a Scrum Master, I helped the team with the code itself and with the organization of the workflow. In collaboration with the Scrum Masters from other teams, we also thrived to improve the branch and commit naming conventions (using GitFlow and other patterns), as well as the pull request templates, to make the project more organized and easier to understand for everyone. I also made sure that testing and documentation is being done properly.

### The user storie that I am most proud of

 * [#5](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/5) - Implemented automatic notifications based on value ranges for sensor dynamic data

 ### The pull request that I am most proud of

* [#91](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/91)  - Implemented alerting/notification features

 ### Two contributions of other types that I am most proud of

During this sprint we could successfully overcome the initial setup difficulties, and we were able to implement the automatic notifications feature using dynamic data, which was the main goal of this sprint.

More testing, validation and betetr organization of the repository and overall work was also a point of focus during this sprint. Also, code review was taken more seriously, and we were able to improve the quality of the code that was being pushed to the dev branch.

## Sprint 3

During this sprint, my contribution to the team and project overall, was to research ways of implementing auto-manage processess to the machines. As the sprint went by, the team globally realized that the implementation of this issue might not be feasible, which was actually our final conclusion.
However, I gathered relevant information that might be useful later on, on an hypotetical stage of the project where the client would give us real data regarding machines and production lines. The following links contain this information:

- [Grafana Machine Learning Documentation](https://grafana.com/docs/grafana-cloud/alerting-and-irm/machine-learning/) - Depicts the use of machine learning models that could be implemented if we used a Grafana cloud instance (however, this can be costly)

- [Grafana Webinar on ML and adaptive alerts](https://grafana.com/go/webinar/grafana-machine-learning-adaptive-alerting/) - Introduction to predictions using Grafana linked data

Reflecting on this sprint, I think I coud have contributed in a more positive way if the issue assigned to our team was simpler, as conciliating such a complex theme with other projects was very difficult. In the next sprint

As a Scrum Master, I also interacted with the other teams Scrum Masters so we could decide what to do with the issues we faced along this sprint.

### The user storie that I am most proud of

* None relevant, as we did not implement any code.

 ### The pull request that I am most proud of

* None relevant, as we did not implement any code.

 ### Two contributions of other types that I am most proud of

During this sprint I interacted more with other teams and its members, and I also checked that the alerting feature makes sense with the data, which was updated (however, this can be improved in the next sprint).

I played a big part in organizing our team's work and making sure everyone had something to do. We faced some challenges, but I helped my teammates when they needed support. 

## Sprint 4

...


## Overall Product

Reflect on your specific contributions to the product, technically and as perceived by a user, along the three dimensions below (see Dashboard > Final outcomes > Product). Keep each section below to a maximum of 50 words.


### Technical Soundness

...


### Product Realization

...


### Value for the Client

...
