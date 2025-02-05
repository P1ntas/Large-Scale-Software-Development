# Factsheet for Fábio Morais

## Sprint 0

Took part in the writing of the initial user stories


## Sprint 1

At first analysis of the dinasore repository in order to get familiar with this tool. This included the completion of the tutorial that was later discussed by the whole team in a meeting with the objective of setting a good starting point for the sprint.
Later in the sprint worked mostly together with [João Araújo](../team1/joao_araujo.md) in the creation of a dinasore project that would simulate data from a sensor and write it to prometheus. My part would consist mostly in reproducing the project made by João locally testing that everything was working as it should. This reproduction followed different steps from his work which led to deal with different problems. I also took part in the giving of feedback that helped in the creation of the setup guide and documentation.


### Two contributions of other types that I am most proud of

- My contribution in the first team meeting was important in the familiarization of the group with dinasore and on the set of the good environment for the sprint
- The support gave to João, which was already much more familiar with this environment, is something im proud since it made me have to adapt to his speed and workflow

## Sprint 2


#### The user story that I am most proud of
 * [#29](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/29)

### The two pull requests that I am most proud of

This can include PRs that you have implemented or reviewed during the sprint.

 * [83] (https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/83)
 * [52] (https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/52)


### Two contributions of other types that I am most proud of

- The help given to the team regarding the dockerization which was the main task for our group.
- The update of the documentation regarding the new sensor simulator which led me to integrate it in the pipeline with the help of João (responsible for the creation of this FB) and test it in order to find the correct parameters. As this was done after the dockerization it included updating also the documentation regarding other parameters, mainly hosts.


## Sprint 3

#### The user story that I am most proud of
 * [#102](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/102)

### The two pull requests that I am most proud of

This can include PRs that you have implemented or reviewed during the sprint.

 *  [114] (https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/114)
 *  [105] (https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/105)


### Two contributions of other types that I am most proud of

- Worked together with João in the machine's job schedule display. This led among other things to a change in the mockup data adding the task concept that would be used in grafana's state timeline.
- Took part in the work distribution, contributing for a better workflow inside the team.


## Sprint 4

#### The user story that I am most proud of
 * [#103](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/103)

 ### The two pull requests that I am most proud of

This can include PRs that you have implemented or reviewed during the sprint.

 *  [148] (https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/148)

 ### Two contributions of other types that I am most proud of

- As grafana only works with one way the issue had to be done via plugin. This requested some work of familiarization with the new plugin.
- Finished the task creation on grafana which was the first part of the issue attributed to me. Although I had some problems in commiting the grafana changes, those were solved with the help of [João Araújo](../team1/joao_araujo.md). Also helped him finish the rest of the issue.



## Overall Product

### Technical Soundness

From my point of view, the technologies used are correspondent with what this project and architecture asked, and their choice of usage is already explained in the different other documents in this project. Their implementation in this project was streamlined to be as easy as possible to build upon. The only problem I can trace in these contexts are the usage of the 4DIAC-IDE, as a manual setup is needed every time a new sensor is added, and this must also be done on the remote server.
In general, I think the technical soundness of the project is one of the things we can most be proud of.

### Product Realization

The features implemented were in-line with the goals outlined by the client. Their implementation borders on every point we discussed with the client and obey the technical constraints required. The features in which we (Team 2) worked on were implemented thoroughly and documented accordingly. However, the final product is missing the integration between the Machine Learning component and the rest of the project.

### Value for the Client

The feedback received from the client was mostly positive, as most of the project requirements were met and handover questions were discussed and rested. This project served as a testing ground for, specifically, DINASORE and 4DIAC-IDE usage, which was a point the client made right at the start, and one of the main tasks our team realized. In our understanding, what we gathered from its implementation will be useful going forward, as it was also discussed that there might be further work done on top of it.
