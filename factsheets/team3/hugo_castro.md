# Factsheet for Hugo Castro

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

During this phase of the project, my focus was on advancing the task related to providing customizable notification settings. In pursuit of this goal, I conducted thorough research to identify robust strategies within Grafana's alerting and notification framework. This documentation delve into template notifications, a feature that could be instrumental in creating customizable and dynamic notification settings. This research phase laid a solid foundation to incorporating flexible and user-friendly notification settings into our system in the future, ensuring that users can efficiently customize alerts according to their unique needs and operational requirements.

A significant resource I explored is the following link: [Grafana manage notifications](https://grafana.com/docs/grafana/latest/alerting/manage-notifications/template-notifications/).

### The user storie that I am most proud of

* None relevant, as we did not implement any code.

 ### The pull request that I am most proud of

* None relevant, as we did not implement any code.

### Two contributions of other types that I am most proud of
I helped my team understand better how to customize notifications. 

## Sprint 4

In this last sprint, my primary objective was refining the project's notification systems, streamlining the notification process through the use of the templating language. Harnessing the power of templates, I helped to build clearer and more concise notifications, which will make them hold more value and transmit information to the user in a better way. I actively collaborated with other team members to augment an existing feature (notifications), contributing for its improvement.

### The user storie that I am most proud of

* [#5](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/5) - Implemented automatic notifications based on value ranges for sensor dynamic data - updated to feature Go's templating language and more accurate parameters

 ### The pull request that I am most proud of

* [#151](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/151)

### Two contributions of other types that I am most proud of
I worked mainly with Afonso and Eduardo to implement more helpful notifications in the system.
I also helped other team members when they had any doubts.

## Overall Product

Reflect on your specific contributions to the product, technically and as perceived by a user, along the three dimensions below (see Dashboard > Final outcomes > Product). Keep each section below to a maximum of 50 words.


### Technical Soundness


My contributions to the project were technically proficient, as I used the technical knowledge I acquired during the course to implement the features I was assigned to. I also strived to use the establsihed technologies (which were a good fit) for the project and also helped other team members when they had any doubts. I also made sure all features were easy to understand and robust.



### Product Realization


Acknowledging potential enhancements in the product's usability, I actively addressed this aspect. My collaboration with the team resulted in the implementation of streamlined and potent notifications, significantly elevating the overall user-friendliness and professional look of the product, which clearly exhibits a good use of the chosen technologies.



### Value for the Client


From my perspective, the final product, particularly the features we implemented, should leave the client satisfied and happy, as we implememnted simple to use yet effective features.

