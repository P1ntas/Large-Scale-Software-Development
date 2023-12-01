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

### Team 4 Retrospective


#

## **Sprint 4**

### Overall Retrospective

### Team 1 Retrospective

### Team 2 Retrospective

### Team 3 Retrospective

### Team 4 Retrospective

