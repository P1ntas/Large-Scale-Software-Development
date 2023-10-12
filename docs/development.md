# Development

## Architecture and design

Describe the architecture and design of the system. Use component/deployment diagrams. If needed, resort to package diagrams to organize them into more manageable parts. 

Be clear about what is the current architecture/design and what is the one you envision in the future, in case they are different. 
Identify main risks and justify the most important choices to show the soundness of the architecture and design that you have implemented or plan to implement.

### First Prototype - Sprint 0

The architecture of the first prototype can be seen [here](product.md#domain-analysis).

We decided to use Docker to create the containers for the databases, the python instance and Grafana. This way, we can easily deploy the system in any machine that has docker installed.

# TODO FINISH

## Technology

### First Prototype - Sprint 0

At first, after the first contact with the client, we were told we were free to use any technology we wanted, as long as it doesn't require a lot of maintenance and it is open-source. With this in mind, we decided to use the following technologies, languages and frameworks:

- **Docker**: Docker was used to create the containers for the databases and the python instance. This way, we can easily deploy the system in any machine that has docker installed.

- **Python**: Python was used to create the python instance that simulates the data from the sensors and sends it to the databases. It was also used to create the **Flask** server that exposes the data from the sensors to the **Prometheus** database. For this first prototype, it was also used to generate the data from the sensors and the static data from the systems.

- **PostgreSQL**: PostgreSQL was used to create the database that holds the static data from the systems. This data is used to create the factories, systems, expansions and the sensors. It also holds the thresholds values of the sensors. This technology was chosen because it is open-source, easy to use, and it is one of the most used databases in the world for Relational Database Management System (RMDBS).

- **Flask**: Flask was used to create the server that exposes the data from the sensors to the **Prometheus** database. This choice was made because it is a micro web framework written in Python, and it is very easy to use and to integrate with other technologies. This server exposes the data via HTTP, so that Prometheus can scrape it at a given interval.

- **Prometheus**: Prometheus was used to create the database that holds the data from the sensors. It is used to create the graphs and the alerts. Prometheus scrapes the data that the python instance generated and sent to the **Flask** server.

- **Grafana**: Grafana analytics & monitoring tool was used to display the data and collected metrics to the final user. It shows them via dashboards, and also displays alerts when they are triggered. The Grafana instance queries both the **Prometheus** and the **PostgreSQL** databases on a given interval and dashboard load, respectively. The user can manipulate the queries that are sent in an intuitive way, so that he can filter the data that he wants to see. From here, the user can also trigger any action through the outside systems, just like turning off a system.

The domain of the architecture can be seen [here](product.md#domain-analysis).

### Second Prototype - To be done in the following Sprints

After the first prototype, we had a Q&A session with the client which enlightened us on some of the requirements that we had to implement. With this in mind, we decided to change some of the technologies that we were using, and also add some new ones. The technologies that we decided to use were the following:

- **Docker**: Docker was used to create the containers for the databases and the python instance. This way, we can easily deploy the system in any machine that has docker installed. This technology was chosen because it is open-source, easy to use, and it is one of the most used technologies in the world for containerization.

- **Python**: Python was used to create the python instance that simulates the data from the sensors and sends it to the databases once more, while we do not have the real data from the sensors. It was also used to create the **Flask** server that exposes the data from the sensors to the **Prometheus** database. For this second prototype, it was also used to generate the data from the sensors and the static data from the systems.

- **PostgreSQL**: PostgreSQL was used to create the database that holds the static data from the systems. This data is used to create the factories, systems, expansions and the sensors. It also holds the thresholds values of the sensors. It is open-source, easy to use, and it is one of the most used databases in the world for Relational Database Management System (RMDBS). We also had the option to choose a **MongoDB** database, which is a document database. This means that PostgreSQL is more suitable for the static data, since it is more structured and achieves an higher confidence level to integrate with Grafana, while MongoDB is more suitable for the simulations data that the **MLM** will generate, since it is more flexible and can handle the data in a more efficient way. For now, we will stick with PostgreSQL, since it is the most used system for this purpose and has an easier integration with Grafana.

- **Prometheus**: Prometheus was used to create the database that holds the data from the sensors. It is used to create the graphs and the alerts. Prometheus scrapes the data that the python instance generated and sent to the **Flask** server. We had the option to choose a **InfluxDB** database, which is also a time series database. Both instances achieve the main purpose, but the pros of on system are the cons of the other. Prometheus has a built-in alert system, while InfluxDB has a built-in MQTT handler. While this has to be discussed with the client further, we decided to use Prometheus for the second prototype, since it is the most used system for this purpose and has an easier integration with Grafana.

- **Eclipe Mosquitto**: Eclipse Mosquitto was used to create the MQTT broker that receives all the data from the sensors via the MQTT protocol. It is responsible for sending the data to the EdgeX Foundry instance. This technology was chosen because it is open-source, easy to use, and it is one of the most used technologies in the world for MQTT brokers. We also had the option to choose **EMQX**, which is also a MQTT broker. Both instances achieve the main purpose, but we decided to keep with **Eclipse Mosquitto** since it has an easier integration with EdgeX Foundry.

- **EdgeX Foundry**: EdgeX Foundry was used to create the system that is built on top of the MQTT broker, so it is responsible for the communication between the MQTT broker and the databases and the **M**achine **L**earning **M**odel (**MLM**). It is also responsible to retrieve data to the Apache Storm instance to process it and filter it. It also receives any request made from the Grafana instance (for example, to simulate a new production line) and sends to the desired handler. This technology was chosen because it is open-source, easy to use, and it is one of the most used technologies in the world for IoT systems. We had more options to choose from, but this one was the most suitable for our project.

- **Apache Storm**: Apache Storm was used to create the system that is responsible for the communication between the databases and the **MLM**. This technology was chosen because it is open-source, easy to use, and it is one of the most used technologies in the world for stream processing systems. We also had the option to choose **Apache Flink**, which is also a stream processing system and a batch processing system. This means that Apache Flink is more suitable for the data processing and the data filtering, since it can handle both the real-time data and the historical data, while Apache Storm is more suitable for the communication between the databases and the **MLM**, since it is more lightweight and can handle the data in a more efficient way. For now, we will stick with Apache Storm, since it is the most used system for this purpose.

- **PyTorch**: PyTorch was used to create the **MLM** that is responsible for the prediction of the sensors data. This technology was chosen because it is open-source, easy to use, and it is one of the most used technologies in the world for machine learning models. We had more options to choose from, but for now, we will stick with PyTorch, since it will achieve our main purpose.

- **Grafana**: Grafana analytics & monitoring tool was used to display the data and collected metrics to the final user. It shows them via dashboards, and also displays alerts when they are triggered. The Grafana instance queries both the **Prometheus** and the **PostgreSQL** databases on a given interval and dashboard load, respectively. The user can manipulate the queries that are sent in an intuitive way, so that he can filter the data that he wants to see. From here, the user can also trigger any action through the outside systems, just like turning off a system. This technology was chosen because it is open-source, easy to use, and it is one of the most used technologies in the world for analytics & monitoring tools. Also, some developers have previous experience with the tool.

The domain of the architecture can be seen [here](product.md#domain-analysis).

##  Development guide

Explain what a new developer to the project should know in order to develop the system, including who to build, run and test it in a development environment. 

Document any APIs, formats and protocols needed for development (but don't forget that public APIs should also be accessible from the "How to use" section in your README.md file).

Describe coding conventions and other guidelines adopted by the project.


## Security concerns

Identify potential security vulnerabilities classes and explain what the team has done to mitigate them.


## Quality assurance

Describe which tools are used for quality assurance and link to relevant resources. Namely, provide access to reports for coverage and mutation analysis, static analysis, and other tools that may be used for QA.


## Metrics

Describe how you captured each of the "four key metrics" (e.g., automatic mechanism, survey to the team on the end of each sprint).

Provide here an historical record (for each sprint) of the four key metrics and velocity.


## Restrospectives

Describe (possibly as separate markdown files linked form this section) a written account of your retrospectives. There should be, for each sprint, one retrospective for the entire project, and one for each team.
