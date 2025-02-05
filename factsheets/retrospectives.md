# Sprint Restrospectives

## **Sprint 1 (12 October - 26 October)**

### Overall Retrospective
(missing on sprint 1)

### Team 1 Retrospective

For the first sprint, our team's objectives were to create a database suitable for static and real-time data, setup Grafana, design and implement a page that allows workers to view machine logs and characteristics, and we were also responsible ([João Araújo](../factsheets/team1/joao_araujo.md)) with helping other team members. In conclusion, we were able to do most tasks, but work still needs to be done.

After the sprint has ended, looking back we noticed we need to improve in some topics, just as, be more active in Discord and in the team overall, improve the user stories per sprint ratio while also reviewing every user story. However not everything needs to be improved, since the beginning that we developed great cooperation, good pace of work as well as always being ready to share information with other teams. There was also simple bad things that we need to avoid moving forward, like terrible communication inside the team and delays in the factsheets. The most substantial doubts we had in this sprint were related to how is the database developed and updated.

### Team 2 Retrospective

Negative points :

- Difficulty in organizing the work considering that it was too sequential
- There were some problems when setting up the DINASORE tool and the 4diac IDE

Positive points:

- Good comunication between team members
- Good starting basis regarding the used technology

### Team 3 Retrospective

During this sprint, our team was assigned the task of developing automatic notifications for events and familiarising with the way they work and are implemented in the Grafana platform. Although we were able to achieve this goal successfully, creating some test notifications, as data was still not dynamic, in large quantity and following a defined pipeline, we were not able to fully develop and test this feature. In conclusion, we acquired all the necessary knowledge to finish this task in the next sprint alongside another task assigned to us, as the work done by the other teams regarding the stream of data will support our development of this feature.

### Team 4 Retrospective

During sprint 1, our team had to deal with a PBI that was of low priority but high workload, which consisted of creating a ML model that, through the information it receives from the database, manipulates the operation of the machines so that it is as efficient as possible. Our efforts turned to understanding as best as we could how we were going to approach the issue, planning the development and integration of the solution. There was also a limitation on the work we could do, as we needed data we didn't have, since the integration of the sensors with the system had not yet been done and the said ML model needs real data to be trained. So, we plan to continue working in this same issue during next sprint, to finish it as quick as possible.

#

## **Sprint 2 (26 October - 17 November)**

### Overall Retrospective
On the one hand, the class worked steadily on the issues, never standing still. On the other hand, no standards were defined until late in the sprint, in terms of commit messages, branch name structure, and anything else related to working guidelines.

#### Team 1 Retrospective
Negative points :
- Progress is sometimes obscure with our team and we don't really know what is going with other team members.

Positive points:
- Good comunication between other teams.
- Started to use more technical practices.

### Team 2 Retrospective

Although communication started off a bit rocky, there was a noticeable improvement in communication and collaboration among team members in the latter half of the sprint. This positive trend contributed to a more cohesive and productive work environment. Due to this, the team successfully accomplished all the predefined tasks set at the beginning of the sprint and dynamically assigned itself to next steps of the project. However, the collaborative hurdles at the start of the sprint, mixed in with sequential work that affected other tasks assigned to the team, meant that productivity bloomed late in the sprint. Even then, our team is proud of the work we've done and with our growth from the first sprint.

### Team 3 Retrospective

During this sprint, the team continued focusing on the implementation of the automatic notifications feature, that turned out to be badly evaluated in terms of effort estimation, as it was more complex than initially thought. Also, the team had to deal with setup issues of the project. As a dynamic Prometheus data simulator was added by another team, we had to re-do our setup, and this took some time, as the software used to simulate the data (Dinasore and 4DIAC-IDE) was excessively complex and not well maintained in terms of versioning and support from the original developers. The team was also able to conclude that, using Grafana, there is no viable way for the user that receives the notification to acknowledge it: there is only going to be another notification when the issue is resolved (e.g., the temperature is back to normal). This is a limitation of Grafana. For the other points of the user story that was attributed to us, we were able to implement them successfully, and notifications are working based off dynamic data from sensors that is being streamed from Prometheus to Grafana.
However, the team considers that the feature is done, although it can be refined in future iterations of the project, as more data becomes available (e.g. discrimination between temperature/pressure types), which will enable to define more suitable ranges for each type of sensor.

### Team 4 Retrospective
During this sprint, the most positive point was the good communication that was maintained throughout the sprint, either synchronous or asynchronous. The least positive part would be the fact that the client tends to communicate in a rather vague way. In order to improve this last point, our team's SM may need to attend the meetings between the client and the PO's in order to understand the situation with his more technical point of view.

#

## **Sprint 3 (17 November - 1 December)**

### Overall Retrospective

### Team 1 Retrospective

#### Start:
    - Using a team branch to push the changes instead of creating a pull request of each feature/fix to the dev branch
    - Communicating more with the team members to better understand the progress of the sprint

#### Stop:
    - Lacking communication between team members
    - Not working as soon as expected to finish the assigned issues
    - Opening pull requests to the dev branch instead of the team branch

#### Continue:
    - Following the coding guidelines correctly

#### General Considerations:

Overall, we aren't totally happy with the work that was carried out this sprint. The lack of communication between the team members and the done work wasn't totally satisfactory. The meeting held in the start of the sprint was useful to understand the current status of the progress made towards our goals and to shift priorities when needed, but it wasn't enough to get more work done better and more adequately.

### Team 2 Retrospective

#### Start:
    - Collecting more metrics in order to better understand our performance during our sprint and identify bottlenecks
    - Enphasizing communication at the start of the sprint to make sure work is laid out more easily during its duration
    - Using a team-wide branch to push changes instead of committing directly to the *dev* branch

#### Stop:
    - Committing directly to the *dev* branch

#### Continue:
    - Good communication throughout the sprint
    - Following the coding guidelines correctly
    - Good work balance between teammates
    - Good overall productivity

#### General Considerations:

Overall, we are happy with how our work was carried out this sprint. We effectively tackled the issues assigned to us and divided the work evenly, allowing for our most productive sprint yet. We held two team-wide meetings to understand the current status of the progress made towards our goals and shifted priorities when needed, which proved to be immensely useful to get more work done better and more adequately.

### Team 3 Retrospective

During this sprint, our team was in charge of analyzing and trying to implement the issue [#7](https://github.com/orgs/FEUP-MEIC-DS-2023-1MEIC06/projects/1?pane=issue&itemId=41408318).

The issue was somewhat related to the machine learning objective for the machines to auto-manage themselves. However, as we had already discussed with anotehr team, this is impossible to implement in relaity, once again due to the presence of only mock data. Also discussing both between us and with other teams, we came to the conclusion that this issue will most likely be abandoned. We also took advantage of the happiness meters to reflect this, as the poor interaction with the client also lead to this doubt state when implementing these kind of issues.

However, we can still analyze this sprint in the "Start, Stop, Continue" way.

### Start

    - We will start to work on another issue that is more feasible to implement, and that is not related to machine learning.
    - We will start to ask from more feedback from the client directly, as their requests are not always clear and feasible.
    - We should start dedicating more time to the project board organization and selection of issues to work on.

### Stop

    - We will stop working on tasks that are too complex and maybe not so much aligned with the project's objectives and acceptance criteria.

### Continue

    - We will continue to work hard and professionally on the issues we are assigned and try to deliver the best possible   solutions.
    - We will continue to research and learn more about the technologies we are using, so that we can deliver better results.
    - We will continue to use good coding and project management practices, so we can stay organized.

### Team 4 Retrospective

#### Start:
    - We will focus our attention on other issues aside the ML one.

#### Stop:
    - We will focus less on the ML issue, because we don't have the client's help on giving us the data we need.

#### Continue:
    - We will continue to make use of the good communication between team 4 members.

#### General Considerations:

This sprint we didn't develop as much as we wished. For several reasons. Also, the lack of real data and communication on the clients side doesn't help.

#

## **Sprint 4**

### Overall Retrospective
The work developed so far is more than satisfactory. All noticed the improvements made so far, so it would be a matter of having more time to develop a more polished product.

### Team 1 Retrospective

#### Start:
    - Weekly reunions with team members to check what everyone is up to more often.

#### Stop:
    - Not working as soon as expected to finish the assigned issues.

#### Continue:
    - Following the coding guidelines correctly.
    - Following the documentation guidelines correctly.
    - Continue the good communication between team members.

#### General Considerations:

Overall, we didn't have enough time to work on this sprint, but we improved the communication between the team. We held a meeting at the start of the sprint, which proved useful to understand the status of the work done until that moment, as well to shift our priorities to the new up and coming tasks that were needed to conclude this sprint.

### Team 2 Retrospective

#### Start:
    - Schedule meetings earlier/at the start of the sprint, so as to make sure everyone can attend them

#### Stop:
    - Waiting for the end of the sprint to start filling out individual factsheets and other content to enable easier releases at the end of the sprint

#### Continue:
    - Having better communication throughout the sprint
    - Following the coding guidelines correctly
    - Good work balance between teammates
    - Good overall productivity

#### General Considerations:

All in all, we are happy with our work this sprint. Because of our low availability due to lack of time, we ended up having less PBIs done - however, we were able to achieve the main points to achieve a working template to be built upon. Furthermore, even despite having less dedicated time, the team got together and worked continuously and together, discussing and helping each other when needed.

### Team 3 Retrospective

During this sprint, our team was in charge of refining and making improvements to the issue [#5](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/issues/5).

The issue, in which we had already previously worked on, was related to implementing Grafana native notifications/alerts based on the data that is being streamed from Prometheus. The notifications are sent when the data is out of the normal range (firingg status), and another notification is sent when the data is back to normal (resolved status). This feature was already implemented, but it was not working as expected, as the notifications were being sent uncontrollably. So, we had to fix the issue adjusting the ranges and we took advantage of th opportunity to implement a templating language that could be of good use later on in the project, when we have real data.

We will, as done before, analyze this sprint in the "Start, Stop, Continue" way.

### Start (if there was another sprint)

    - We would start to try to implement machine learning applied to our notifications.
    - We would try to grab the client's attention to our needs.

### Stop (if there was another sprint)

    - We would stop spending so much time researching on the technologies we are using, as we sometimes are having less than ideal development time.

### Continue (if there was another sprint)

    - We would continue to work hard and professionally on the issues we are assigned and try to deliver the best possible solutions.
    - We would continue to use good coding and project management practices, so we can stay organized.

### Team 4 Retrospective

#### Start (if there was another sprint)

    - We would've finish implementing a complete machine learning solution.
    - Draw the customer's attention to the urgent need for real data.

#### Stop (if there was another sprint)

    - We would stop spending so much time researching on the technologies we are using, as we sometimes are having less than ideal development time.

#### Continue (if there was another sprint)

    - We commit to diligently and professionally addressing the assigned tasks, striving to provide optimal solutions.
    - We intend to maintain our organizational structure by adhering to effective coding and project management practices.
    - We would continue with the good communication and team work spirit that has been developing thoughout this project.

#### General Considerations:

During this sprint, our team did various different issues, not only concerning the previous theme assigned to us (optimization) but also other issues concerning the UI and user functionalities.

The optimization issues could have been easier to work if the client made some real data available.
