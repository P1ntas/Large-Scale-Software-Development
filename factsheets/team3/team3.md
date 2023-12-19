# Factsheet for Team 3

## Sprint 0

Sprint 0 was dedicated to technology familiarization, with a primary focus on Grafana running on Docker. Over the course of three weeks, the team achieved several key milestones in their pursuit of understanding and gaining proficiency in these technologies.

Key Achievements:

- The team successfully set up a development environment by deploying Grafana on Docker containers. This achievement was crucial in ensuring that the team had a stable and consistent environment for further development.

- Team members engaged in thorough research and exploration of Grafana, gaining a fundamental understanding of its features, capabilities, and use cases. This exploration included the creation of sample dashboards and the customization of visualization options within Grafana.

- As part of technology familiarization, the team connected Grafana to various data sources, demonstrating an understanding of how data can be ingested into Grafana for visualization and analysis.

- The team proactively utilized online resources, tutorials, and official documentation to enhance their understanding of Grafana and Docker. This commitment to self-learning was a commendable effort during this sprint.

The team encountered some challenges during this sprint, including initial configuration issues and learning curve associated with Docker and Grafana. However, these challenges served as valuable learning experiences, highlighting the importance of effective troubleshooting and the necessity of in-depth documentation.

### The four user stories that we are most proud of

This can include user stories that the team has written or refined during the sprint. If it was a refinement, explain what you have added or changed.

 * #1
 * #2


### The four pull requests that we are most proud of

This can include PRs that the team has implemented or reviewed during the sprint.

 * #3
 * #4


### Four contributions of other types that we are most proud of

This can be anything that you think worked particularly well and benefited the project as whole, from a hard conversation with the PO that worked out very well, to the adoption of a new framework or library. 



## Sprint 1

During Sprint 1, the team initiated automatic notifications development in Grafana, achieving successful test creation despite limitations in dynamic data. Valuable insights gained lay the foundation for completion in the next sprint, with collaboration on data streaming expected to enhance feature development.

Key achievements:

- The team successfully implemented an automatic notification for testing purposes with different data and delivery endpoints. This achievement was crucial in demonstrating the feasibility of the feature and identifying potential issues.

- The team successfully implemented a Discord bot to receive notifications, demonstrating the ability to integrate Grafana with external applications.

- The sprint provided essential insights, laying the groundwork for completing the task in the next sprint.


## Sprint 2

In Sprint 2, the team focused on implementing the automatic notifications feature, overcoming unexpected complexities in the process. Project setup issues arose due to the integration of a dynamic Prometheus data simulator, requiring a time-consuming reconfiguration. Despite challenges with the simulator software, successful implementation of key user story components was achieved. However, a limitation in Grafana was identified, preventing users from acknowledging notifications; instead, subsequent alerts are generated upon issue resolution.

Key achievements:

- The team successfully implemented various notifications for sensors, including value is higher than X and value is lower than Y. These are the main type of notifications of interest for our project.

- The team successfully implemented notifications for when the values are restored to normal conditions, marking the problem as resolved.

- Essentialy, the team successfully implemented the automatic notifications feature, despite setbacks and opportunities for refinement in the future.

### The user storie that we are most proud of

 * [#5](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/5) - Implemented automatic notifications based on value ranges for sensor dynamic data

### The pull request that we are most proud of

* [#91](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/91)  - Implemented alerting/notification features

### Four contributions of other types that we are most proud of

 * 1 - Adaptability and problem-solving skills were evident in addressing challenges related to the project setup and the integration of the Prometheus data simulator in this sprint.
 * 2 - Taking into account feedback from the last sprint, the team thrived to improve the branch and commit naming conventions (using GitFlow and other patterns), as well as the pull request templates, to make the project more organized and easier to understand for everyone.
 * 3 - We made sure that the feature we developed is well documented and tested, improving on the previous sprint regarding this aspect. Also, the code review process was improved, with more attention to detail and more thoroughness.
 * 4 - We collaborated with other teams by providing feedback, asking questions and overall helping each other to improve the project as a whole.

...


## Sprint 3

During Sprint 3, the team focused on trying to implement machine learning models and auto-manage features for the machines. However, we could only research about this feature until we came to the conclusion that it was not feasible to implement, at least in the current state of the project, as we were not provided with any form of real data that would enable us to successfuly implement and test this feature. The team also worked on the documentation and followed the established guidelines in order to maintain the quality of the project.

Key achievements:

- The team successfully gathered relevant information about the auto-manage feature, and we were able to conclude that it was not feasible to implement it in the current state of the project.

- The information mentioned above was deemed relevant as it could be of great interest for future work on the project, and it was also a good learning experience for the team.

- With these conclusions we are also able to focus on other features that are more feasible to implement, and that will be more useful for the project in the future.

### The user storie that I am most proud of

* None relevant, as we did not implement any code.

 ### The pull request that I am most proud of

* None relevant, as we did not implement any code.

### Four contributions of other types that we are most proud of

 * 1 - The team continued to follow the branch and commit naming conventions (using GitFlow and other patterns), as well as the pull request templates, to make the project more organized and easier to understand for everyone.
 * 2 - We made sure to inform other teams about our conclusions regarding the auto-manage feature, so that they could also focus on other features that are more feasible to implement.
 * 3 - We collaborated with other teams by providing feedback, asking questions and overall helping each other to improve the project as a whole.


## Sprint 4

During Sprint 4, the team focused on trying to implement machine learning models and auto-manage features for the machines. However, we could only research about this feature until we came to the conclusion that it was not feasible to implement, at least in the current state of the project, as we were not provided with any form of real data that would enable us to successfuly implement and test this feature. The team also worked on the documentation and followed the established guidelines in order to maintain the quality of the project.

the team turned its focus on leveraging the capacities of Go's templating language to make maintenance notifications clearer and more human-readable. Also, the parameters for these notifications were reviewed: previously the notifications were firing based on hard-coded values, as at the time of the original implementation all we had was random mock data, which did not allow us to precisely set these parameters. This led to uncontrolalble notification firing, which obviously wasn't ideal.

Key achievements:

- The team successfully researched about ways to make notifications better overall, finding in [Go's templating language](https://grafana.com/docs/grafana/latest/alerting/manage-notifications/template-notifications/using-go-templating-language/) integration with Grafana the ideal solution.

- The mock data coming from the generators was analyzed thoroughly in order to find the best notification parameters.

- These parameters were used to tune the system accordingly.

### The user storie that I am most proud of

* [#5](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/5) - Implemented automatic notifications based on value ranges for sensor dynamic data - updated to feature Go's templating language and more accurate parameters

 ### The pull request that I am most proud of

 * [#151](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/151)

### Four contributions of other types that we are most proud of

 * 1 - The team continued to follow the branch and commit naming conventions (using GitFlow and other patterns), as well as the pull request templates, to make the project more organized and easier to understand for everyone.
 * 2 - We refined the project objectives in order to reflect our priorities
 * 3 - We implemented important features to make the project more usable and intuitive for the end-user. 
 * 4 - We collaborated with other teams by providing feedback, asking questions and overall helping each other to improve the project as a whole.


## Overall Product

Reflect on your specific contributions to the product, technically and as perceived by a user, along the three dimensions below (see Dashboard > Final outcomes > Product). Keep each section below to a size of 40~100 words.


### Technical Soundness


During the project, the whole team strived to follow the establsihed guidelines and coding standards, in order to maintain the quality and scalability of the project. We also made sure to implement all of our features takeing into account the available technologies, and always documented our work.
We think the chosen technologies were a good fit for the proposed architecture as Grafana and Prometheus are suitable for showing data (fed by live scraping) to the user in an intuitive way. Our implementation in particular showcases all of the potential of these technologies. It is also maintainable and robust, as the dashboards and other features can be easily understood and maintained.
The work done laid the foundation for future work on the project, as it is independent of the set of data used, and we are proud of the results we achieved. Also, every member of the team contributed with technical knowledge, improving the overall technical soundness of the project.


### Product Realization

In this project, sometimes it was difficult to turn ideas into reality, as we were not provided with any real data to work with. However, the whole team was able to get better over time, overcoming the initial difficulties and achieving the goals we set for ourselves, implementing important features such as Grafana notifications. We think that the project is in a good state, and we are proud of the work we did. However, if there were additional sprints, we could clearly improve even more, integrating more features and improving the existing ones.
However, we think the product is ready to be delivered to the client, and it has a professional look to it, even with the data we are generating. We also adhered to the technical constraints in place, but always implementing viable solutions to the probloems we faced.

### Value for the Client

The value for the client of our project is clear: together with the other teams, we were able to implement a system that allows the client to monitor the machines in real-time, and to be notified when something goes wrong, alo integrating more features such as the machine learning ones. As the client's requisites were a bit vague, we sometimes had to make decisions on our own, but we think that the client will be satisfied with the results we achieved, as the system is functional and meets the main client's needs. We also think the effort from everyone in our team was adequate to the expected for this project.

