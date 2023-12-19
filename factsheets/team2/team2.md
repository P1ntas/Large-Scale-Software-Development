# Factsheet for Team 2

## Sprint 0

Contributed towards the approval of the initial technology common basis, wrote the initial user stories and helped organize the project backlog. Actively established contact with the client and setup the communication environment.

## Sprint 1

### The two user stories that we are most proud of

- Every DINASORE-related issue of the sprint.

### The two pull requests that we are most proud of

- [#30](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/30)
- [#31](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/31)

### General Contributions

**This sprint, the team worked closely with [João Araújo](../factsheets/team1/joao_araujo.md). We will be taking his work into account when talking about the team's contributions.**
Took care of the familiarization and implementation of the DINASORE technology and further discusses the architecture and requirements in the data extraction stage of the product (sensor-level extraction).

## Sprint 2

### The two user stories that we are most proud of

- [DINASORE Dockerization](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/29)
- [Setup CI/CD Environment](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/62)

### The two pull requests that we are most proud of

- [DINASORE Dockerization](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/52)
- [CI/CD Integration](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/71)

### General Contributions

Managed the Dockerization for the DINASORE tool, established the majority of CI/CD tools, configured critical code vulnerability analysis tools, and revised the documentation by adding a new sensor simulator.

## Sprint 3

### Some user stories that we are most proud of

- [Fix CI Tools](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/97)
- [Job Scheduling: Visualization](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/102)
- [SonarQube Coverage](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/112)

### Some pull requests that we are most proud of

- [Job Scheduling: Visualization](hhttps://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/114)
- [SonarQube Coverage](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/116)
- [Fix CI Tools](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/105)

### General Contributions

Fixed the CI pipeline and integrated *Bandit* to scan for security issues, structured, started and integrated the job scheduling feature, revised documentation & added coding guidelines, added SonarQube test coverage, finalized setup of the remote deployment servers and handled deployment automation with GitHub Actions.

## Sprint 4

### Some user stories that we are most proud of

- [Production Workflow Management: Identify Bottlenecks or Delays in Real Time](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/122)
- [Production Workflow Management: Update Task](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/159)
- [DINASORE: Integration with Live Sensors](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/157)

### Some pull requests that we are most proud of

- [Job Scheduling: Visualization](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/102)
- [Production Workflow Management: Implement a Resource Allocation module for each Task](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/103)
- [Setup CI/CD](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/62)

### General Contributions

For this sprint, we had assigned the job scheduling feature. As grafanna works in a one directional way, we had to use a plugin named Data Manipulation. So the first part of this sprint was mostly used to get familiar with it.
After this, we started the implementation. First a form was made for the creation of tasks. Finally, another form was created in order to assign tasks to a schedule.
This methods would later be fundamental for the AI to interact with machines.


## Overall Product

### Technical Soundness

In our point of view, the technologies used are correspondent with what this project and architecture asked, and their choice of usage is already explained in the different other documents in this project. Their implementation in this project was streamlined to be as easy as possible to build upon. The only problem I can trace in these contexts are the usage of the 4DIAC-IDE, as a manual setup is needed every time a new sensor is added, and this must also be done on the remote server.
In general, I think the technical soundness of the project is one of the things we can most be proud of.

### Product Realization

The features implemented were in-line with the goals outlined by the client. Their implementation borders on every point we discussed with the client and obey the technical constraints required. The features in which we (Team 2) worked on were implemented thoroughly and documented accordingly. However, the final product is missing the integration between the Machine Learning component and the rest of the project.

### Value for the Client

The feedback received from the client was mostly positive, as most of the project requirements were met and handover questions were discussed and rested. This project served as a testing ground for, specifically, DINASORE and 4DIAC-IDE usage, which was a point the client made right at the start, and one of the main tasks our team realized. In our understanding, what we gathered from its implementation will be useful going forward, as it was also discussed that there might be further work done on top of it.
