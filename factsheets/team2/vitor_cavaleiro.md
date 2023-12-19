# Factsheet for Vítor Cavaleiro

## Sprint 0

Contributed by sharing thoughts and opinions concerning the initial user stories.

## Sprint 1

### General considerations
During this sprint, I aimed to understand the DINASORE tool's workflow. To achieve this, I followed the provided tutorials, studied the tool's architecture, and participated in the team meetings for further development and planning. In addition to this, the team conducted a practical test using a customized pipeline that closely matched the client's requirements. I was responsible for writing unit tests for the implemented function blocks.

### Two contributions that I am most proud of
- Set up and studied DINASORE. Shared thoughts about the tool with colleagues.
- Created unit tests for the pipeline created by [João Araújo](../factsheets/team1/joao_araujo.md), contributing for the product quality.

### Pull Requests Made
- The inclusion of the unit tests, which can be found [here](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/commit/f27b58669f545f5121a45e5d4119ea4918d5571b).


## Sprint 2

### General considerations

In this sprint, my primary focus was on elevating the development workflow by delving into and incorporating static analysis tools. I proposed a suite of tools to our scrum masters, and successfully integrated SonarQube into our project.
This approach holds significant promise in enhancing code quality and identifying potential issues at this stage of development. SonarQube, a robust static analysis tool, brings valuable insights into code quality, security vulnerabilities, and code smells on the project.

### Three contributions that I am most proud of
- Establish a local SonarQube instance to facilitate team-wide testing of code quality.
- Develop comprehensive documentation for SonarQube, covering setup instructions and configuration details.
- Provide descriptions of identified code vulnerabilities and insights into code quality based on SonarQube analysis.

### Pull Requests Made
- The integration of SonarQube, which can be found [here](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/73).


## Sprint 3

### General considerations

During this sprint, I concentrated on enhancing code analysis tools. The integration of Tox, an automated testing tool, simplified the code testing process and introduced the ability to generate test coverage reports—an aspect previously lacking in SonarQube. The combined use of these tools has made the generation and visualization of test coverage possible.

### Two contributions that I am most proud of
- Configure a local SonarQube instance and automatic test tool that enables test coverage visualization.
- Develop documentation for creating and visualizing test coverage with setup instructions.

### Pull Requests Made
- The integration of tox and test coverage for SonarQube, which can be found [here](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/116).
- Fixed configuration that was genrating conflicts with github actions, which can be found [here](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/120).

## Sprint 4

### General considerations

In the course of this sprint, I conducted a conclusive SonarQube analysis on the repository and delivered a final quality and security assurance report.

### Two contributions that I am most proud of
- Provide descriptions of identified code vulnerabilities and insights into code quality based on SonarQube analysis.
- Develop a final quality and security assurance report.

### Pull Requests Made
- Documentation update for quality assurance and security concerns [here](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/164).

## Overall Product

### Technical Soundness

From my point of view, the technologies used are correspondent with what this project and architecture asked, and their choice of usage is already explained in the different other documents in this project. Their implementation in this project was streamlined to be as easy as possible to build upon. The only problem I can trace in these contexts are the usage of the 4DIAC-IDE, as a manual setup is needed every time a new sensor is added, and this must also be done on the remote server.
In general, I think the technical soundness of the project is one of the things we can most be proud of.

### Product Realization

The features implemented were in-line with the goals outlined by the client. Their implementation borders on every point we discussed with the client and obey the technical constraints required. The features in which we (Team 2) worked on were implemented thoroughly and documented accordingly. However, the final product is missing the integration between the Machine Learning component and the rest of the project.

### Value for the Client

The feedback received from the client was mostly positive, as most of the project requirements were met and handover questions were discussed and rested. This project served as a testing ground for, specifically, DINASORE and 4DIAC-IDE usage, which was a point the client made right at the start, and one of the main tasks our team realized. In our understanding, what we gathered from its implementation will be useful going forward, as it was also discussed that there might be further work done on top of it.
