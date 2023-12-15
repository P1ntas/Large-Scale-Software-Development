# Factsheet for Team 1 

## Sprint 0

Our team played a pivotal role in establishing the project's foundation. We collectively approved the initial technology framework, organized the project backlog, and initiated client communication.

During the project's start, our team led the creation of our first prototype through thorough research, simplifying the setup process in a Docker container. Clear documentation made it accessible to the teams. We identified new technologies following client Q&A sessions.

In this sprint, our focus was on teamwork and market research. Our research uncovered technologies like critical manufacturing software and Notion for project inspiration and management.


### The four user stories that we are most proud of

- [#14](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/14) As a User, I want to have a solid database that can store the machine's logs over time, so that I can visualize it later
- [#4](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/4) As a User I want to be able to see a detailed log of a specific machine's characteristics so that I can monitor its state over time

### The four pull requests that we are most proud of

The two PRs we're most proud of:
- [#12](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/12) - The development of the Architecture and Design of models eased the visualization of the technologies to be used.
- [#17](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/17) - The inclusion of the first prototype in the repository was a crucial step to show the integration of the first technologies that we were going to use, as well as an easy way to build the prototype on the other's machines.


### Four contributions of other types that we are most proud of

- One of our most critical achievements was the development of the first prototype. This prototype served as a crucial visual representation for elements of our team that required a clearer understanding of the project.

- We also authored a comprehensive development guide for this initial prototype, streamlining the setup process in a Docker container through a single-file setup. The documentation is designed to be clear and concise, ensuring that all team members can easily replicate the prototype on their own machines and grasp the underlying technologies.

- Our market research played a vital role in shaping various aspects of the project, including the creation of user stories, the product vision, questions related to the system, and many other key elements.

- We contributed to the project startup regarding the technologies used for future work.


## Sprint 1


In this Sprint, our team maintained our ongoing communication with the client, addressing any uncertainties and seeking clarification. We actively engaged in proposing solutions based on the valuable feedback provided by the client.

Additionally, we were was tasked with the responsibility of upgrading the existing database schema, helping other teams with tasks like integrating DINASORE and making adicional dashboards in grafana.


### The four user stories that we are most proud of

- [#13](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/13) - The successful integration of [DINASORE](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/13) on the project. This was essential to show the client that our project is feasible to be used in any kind of environment, as well as it is easy to integrate the pipeline with other technologies that may come.

- [#4](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/4) - The integration of a new dashboard in Grafana that is more user-friendly and has more information than the previous one.

- [#14](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/14) - Did the database squema. Probably will need to upgrade in the future.

- [#13](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/13) - Helped team 2 in the progression of the user stories.

### The four pull requests that we are most proud of

- [#27](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/27) - Fixed DINASORE's features to be used in our project with ease.

- [#34](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/32) - Sucessfuly integrated DINASORE into our project with [Team 2](../team2/team2.md). This integration was essential to show the client that our project is feasible to be updated by managers that would use this later on, since the pipeline is fully customizable.

- [#49](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/49) - Uploaded the new database uml.

### Four contributions of other types that we are most proud of

- We've undertaken the task of documenting DINASORE, providing a user-friendly tutorial for our fellow team members.

- In addition to our documentation work, we've been actively assisting [Team 2](../team2/team2.md) and [Team 3](../team4/team4.md) in integrating DINASORE into the project. 

- We've been instrumental in the development of a robust sensor generator, ensuring that it generates the essential data needed to train their respective models effectively.

- The documentation we did empowers others to easily follow and customize the pipeline to suit their specific requirements in the future.

## Sprint 2

### The four user stories that we are most proud of

- [#28](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/28) - Sucessfuly created new reference graphs for the newly created sensors. Added unit testing to these sensors and created a function block, in DINASORE, to generate the data for these sensors according to the type.

- [#29](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/29) - Helped [Team 2](../team2/team2.md) in the dockerization of the DINASORE pipeline and the creation of the docker-compose file to run the pipeline with ease.

- [#14](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/14) - Upgraded the database schema in a way that is both scalable and optimized for enhanced performance and created a SQL schema to be used in the next sprint.

- [#4](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/4) - Helped in the integration of new graphs in the Grafana dashboard and shared ideas in how to make the logs more dynamic to the end user.


### The four pull requests that we are most proud of

- [#67](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/67) - Finished the grafana dashboard implementation

- [#75](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/75) - Finished the Logs implementation in Grafana

- [#65](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/65) - Fixed [Team 2](../team2/team2.md) minor bugs on dockerization of DINASORE and updated the docker-compose.yml file to run the pipeline on docker with ease.

- [#66](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/66) - Created a function block in DINASORE to generate data for the new sensors which closes the issue [#28](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/28).


### Four contributions of other types that we are most proud of

- We've been helping [Team 4](../team4/team4.md) with the types of data generated by the diferent sensors so that they can use on their Machine Learning models.

- We've helped integrate github actions to the project so that we can have a better CI/CD pipeline and have a better overview of the project's status.
  
- Updated the product.md more specifically the recent tools that we're using in the project.

- We discussed how we were going to deal with the low technical practices with other teams.


## Sprint 3

### The four user stories that we are most proud of

- [#102](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/102) - Sucessfuly created new visualizations in Grafana with the details of a systems job scheduler. Also displays the jobs running at a given time and allows the user to see the details of a given job.

- [#98](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/98) - Together with [Team 2](../team2/team2.md), we fixed the documentation content distribution across multiple files and fixed previous documentation issues.

- [#56](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/56) - Integrate real-time data feeds for maintenance features.

- [#6](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/6) - Created a Mockup

### The four pull requests that we are most proud of

- [#114](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/114) - This PR was essential to add the new Grafana visualizations to the development branch according to a systems job scheduler.

- [#101](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/101) - Updated the documentation and the Changelog to reflect the changes made in the project in sprint 2.

- [Mockup](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/blob/documentation/docs/images/mockup.png) - Created a Mockup for Data Analytics page

- [#108](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/108) - Implemented maintenance status, schedule and logs.

### Four contributions of other types that we are most proud of

- I've been helping [Team 2](../team2/team2.md) with the fix of the documentation content distribution across multiple files and fixed previous documentation issues.

- I've helped my team members to understand the new view of the project according to the client's feedback and helped them to understand the new requirements for the next sprint.


## Sprint 4

### The four user stories that I am most proud of

- [#103](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/103) - Together with the member [Fábio Morais from Team 2](../team2/fabio_morais.md), we successfully improved the previously done dashboard regarding the job scheduling, including a forms that creates a new task to be scheduled and the updates are reflected in the dashboard and in the database.

- [#147](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/147) - Corrected a bug related to the dashboard use dinasore data on the new graphs.

- [#14](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/14) - Remodeled the sql and worked on generator file but was not able to complete due to time.

### The four pull requests that we are most proud of

- [#147](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/147) - Corrected a bug related to the dashboard use dinasore data on the new graphs.

- [#148](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/148) - This PR closes the issue [#103](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/103) and provides an updated dashboard for the job scheduling task, as well as a form to create new tasks to be scheduled.

### Four contributions of other types that I am most proud of

- Helped [Team 2](../team2/team2.md) once more on improving the documentation about the project has a whole.

- Helped the other teams with any kinds of problems they had during the development of the project, specially during the setup, which proved useful for the improvement of the documentation.

- Engaging in talks with team members in how to solve some related problems.


## Overall Product

Reflect on your specific contributions to the product, technically and as perceived by a user, along the three dimensions below (see Dashboard > Final outcomes > Product). Keep each section below to a size of 40~100 words.


### Technical Soundness

...


### Product Realization

...


### Value for the Client

...
