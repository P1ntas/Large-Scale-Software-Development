# Development

## Architecture and design

Describe the architecture and design of the system. Use component/deployment diagrams. If needed, resort to package diagrams to organize them into more manageable parts.

Be clear about what is the current architecture/design and what is the one you envision in the future, in case they are different.
Identify main risks and justify the most important choices to show the soundness of the architecture and design that you have implemented or plan to implement.

### First Prototype - Sprint 0

The architecture of the first prototype can be seen [here](product.md#domain-analysis).

We decided to use Docker to create the containers for the databases, the python instance and Grafana. This way, we can easily deploy the system in any machine that has docker installed.

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

- **Eclipse Mosquitto**: Eclipse Mosquitto was used to create the MQTT broker that receives all the data from the sensors via the MQTT protocol. It is responsible for sending the data to the EdgeX Foundry instance. This technology was chosen because it is open-source, easy to use, and it is one of the most used technologies in the world for MQTT brokers. We also had the option to choose **EMQX**, which is also a MQTT broker. Both instances achieve the main purpose, but we decided to keep with **Eclipse Mosquitto** since it has an easier integration with EdgeX Foundry.

- **DINASORE**: DINASORE is a distributed platform that enables reconfiguration of Cyber-Physical System (CPS). The DINASORE platform allows the implementation of python Function Block (FB) based pipelines for sensor integration, data processing, and systems control. It is also equipped to reach the product's goal of being an Industry 4.0 application, as it uses the OPC-UA protocol to allow communication with the other industrial components. While not our first choice for a pipelining technology, it was requested by the client to be used at sensor-level.

- **PyTorch**: PyTorch was used to create the **MLM** that is responsible for the prediction of the sensors data. This technology was chosen because it is open-source, easy to use, and it is one of the most used technologies in the world for machine learning models. We had more options to choose from, but for now, we will stick with PyTorch, since it will achieve our main purpose.

- **Grafana**: Grafana analytics & monitoring tool was used to display the data and collected metrics to the final user. It shows them via dashboards, and also displays alerts when they are triggered. The Grafana instance queries both the **Prometheus** and the **PostgreSQL** databases on a given interval and dashboard load, respectively. The user can manipulate the queries that are sent in an intuitive way, so that he can filter the data that he wants to see. From here, the user can also trigger any action through the outside systems, just like turning off a system. This technology was chosen because it is open-source, easy to use, and it is one of the most used technologies in the world for analytics & monitoring tools. Also, some developers have previous experience with the tool.

The domain of the architecture can be seen [here](product.md#domain-analysis).

##  Development guide

In this section you can find a comprehensive guide on how to fully setup a production-ready environment with all the needed features to start contributing.

### Requirements

- [Docker](https://www.docker.com/) or [Docker Desktop](https://www.docker.com/products/docker-desktop/). This will be used to containerize the different services used in the project.

- [Python 3](https://www.python.org/downloads/) (At least version 3.8). This is required to run the data generator and to push this data to the **PostgreSQL** database.

- [pip](https://pip.pypa.io/en/stable/installing/). This is required to install the python packages.

- Install 4DIAC-IDE for your system. This will be used to configure the dataflow pipeline. You can install using any of these permalinks:
    - [4diac IDE 1.11.0 Windows 64-bit](http://www.eclipse.org/downloads/download.php?file=/4diac/releases/1.11/4diac-ide/4diac-ide-incubation_1.11.0-win32.win32.x86_64.zip)
    - [4diac IDE 1.11.0 Linux 64-bit](http://www.eclipse.org/downloads/download.php?file=/4diac/releases/1.11/4diac-ide/4diac-ide-incubation_1.11.0-linux.gtk.x86_64.tar.gz)
    - [4diac IDE 1.11.0 Mac OS X](http://www.eclipse.org/downloads/download.php?file=/4diac/releases/1.11/4diac-ide/4diac-ide-incubation_1.11.0-macosx.cocoa.x86_64.dmg)

    **NOTE**: In case the permalinks get outdated, you can install using the from this [online folder](https://drive.google.com/drive/folders/1BG9jSN6q5V6J5MTj7w3r6gF6OH6iEOvm)

    **NOTE**: For more details about the 4DIAC-IDE, check this [link](https://eclipse.dev/4diac/en_help.php?helppage=html/4diacIDE/overview.html).

    **NOTE**: After instalation, ensure you have the 4DIAC-IDE outside of the root of this project, otherwise it will be submited to git.

- (Optional for now) Install [Prosys OPC UA Browser 4.4.0-126](https://www.prosysopc.com/products/opc-client/). This OPC client can be used to observe the results of the OPC UA server built in DINASORE.

### Installation / Setup

- First of all, make sure you are in the `/src` directory of the project.

- If you are running **Windows**, you can use the `install.bat` script. Otherwise, if you are using **Linux** or **Mac OS**, you can use the `install.sh` script.

- **NOTE**: (If your python is tagged as `python3` instead of `python`, you will need to change the scripts accordingly)

- This will install the necessary python packages and create the necessary docker containers, those being:
  - `Grafana` running under the port `3000`;
  - `pgAdmin` running under the port `4321`;
  - `PostgreSQL` running under the port `5432`;
  - `Prometheus` running under the port `9090`;
  - `Prometheus Pushgateway` running under the port `9091`.
  - `Mosquitto MQTT Broker` running under the port `1883`.

  The script will populate the `PostgreSQL` database with the necessary tables and data after the containers are up and running.

  Currently, the data generator script is not running, so the data is going to be the same across the board, but you can remove the comment from the `data_generator()` function on the `main.py` file to produce fresh data.

  The generated data consists of 3 facilities. Each facility has 5-10 systems. Each system has 2-5 expansions, and each expansion 1-2 sensors.

### Usage

#### pgAdmin

PgAdmin is a web interface for `PostgreSQL`. It will be essential to test your queries and to see the data in the database before using it in the `Grafana` dashboard.

To access the `pgAdmin` interface, go to `localhost:4321` and login with the following credentials:
```markdown
**Email**: postgres@pg.pg
**Password**: postgres
```

Then, add a new server with the following credentials:
```markdown
**Host name/address**: postgres  *(Under the docker network the hosts take the name you give them in the docker-compose file, instead of localhost)*
**Port**: 5432
**Maintenance database**: postgres
**Username**: postgres
**Password**: postgres
```

![gif](../docs/images/pgAdmin.gif)

#### PostgreSQL

If you rather, you can use the `psql` command to access the database. To do so, you need to access the `PostgreSQL` container through docker and run the `psql` command. You can do this by running the following command:
```bash
docker exec -it postgres psql -U postgres
```

You can use the file `data/push_to_db.py` to push data to the database.

Note: If you are having problems (for example, have postgres also installed on your machine), you can push the data manually on the `pgAdmin` interface through the `Query Tool` tab.

### Prometheus

To access the `Prometheus` interface, go to `localhost:9090`.

To verify if the data is being scraped from the `Pushgateway` server, go to the `Status > Targets` tab and check if the `pushgateway` is up and running. If it is, it should show `UP` under the `State` column.

On the `Expression` tab, you can enter a query to verify the data that is being scraped. For example, you can enter the following queries:
```sql
sensor_value
-- or
sensor_value{sensor_id="1"}
-- or
moving_average{sensor_id="1"}
```
The first one will show all the sensors data, while the second one will only show the value of the sensor with id `1`.

#### Grafana

To access the `Grafana` interface, go to `localhost:3000`. Login with the following credentials:
```markdown
**Username**: admin
**Password**: admin
```

After logging in, you will be prompted to change the password, but you can skip it. After that, you will be redirected to the `Home Dashboard`.

From there, select on the left side the `Dashboards` tab. This will show the available dashboards folders. Select the `General` folder and then select the `General View` dashboard.

![gif](../docs/images/grafana_home.gif)

Now, you can play around with the variables and see the data in the dashboard.

Note: If you wish to change the existing dashboards, that won't be possible because they are provisioned. You can import the same dashboards, that are stored under `grafana/provisioning/dashboards/general`, and change them as you wish.

If you want to create your own dashboard, you can use the Grafana's built-in tools, but you are free to use plugins to achieve your desired needs. The following plugins are recommended:
- [Apache ECharts](https://grafana.com/grafana/plugins/volkovlabs-echarts-panel/). You can use the [Apache Echarts Playground](https://echarts.apache.org/examples/en/index.html) to tryout the different charts and see the code behind them;
- [Data Manipulation Plugin](https://grafana.com/grafana/plugins/volkovlabs-form-panel/);
- [Variable Panel](https://grafana.com/grafana/plugins/volkovlabs-variable-panel/);
- [Canvas Panel](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/canvas/).

To install any plugin, you need to access the Grafana's terminal through docker and run the install command for the plugin you want, following by a restart of the Grafana server.

Also, [here](https://play.grafana.org/dashboards) you can find some examples.

#### MQTT Broker

The `Mosquitto MQTT Broker` is running under `localhost:1883`, with the service open to receive connections from outside the docker network, such as the sensor simulator.

#### 4DIAC-IDE

To open the 4DIAC-IDE, go to the folder where you installed it and run the `4diac-ide.exe` file.

In order to run the sensor simulator, you have to run DINASORE on your system. For that, you need to run the following commands:
```sh
# Move to the dinasore's root folder
cd src/dinasore

# Default values:
# <ip_address>=localhost, <port_diac>=61499,
# <port_opc>=4840, <log_level>=ERROR,
# <number_samples>=5, <seconds_per_sample>=20
python core/main.py -a <ip_address> \
                    -p <port_diac> \
                    -u <port_opc> \
                    -l <log_level> \
                    -m <number_samples> <seconds_per_sample>

```

**NOTE**: For Mac and Linux users, run with the flag -B to avoid the creation of cache folders (conflicts with the FBs folders): ```python -B core/main.py```

For this project, we need to run two instances of DINASORE, one for the FORTE_PC and another for the FORTE_PC_1. For that, you need to run the following commands:
```sh
# On the first terminal

python core/main.py

# And on another terminal

python core/main.py -p 61500 -u 4841
```

- Now, you can open the 4DIAC-IDE and import the [function blocks folder](./resources/function_blocks/). For that, you can follow the next steps:
  1. Open the 4DIAC-IDE
  2. Go to File -> New -> New System -> *Name the project as *MES*** -> Finish
  3. On the System Explorer, left click to open the **MES** -> Right click on the **Type Library** -> Import -> General -> File System -> Next -> Browse -> Select the [function blocks folder](./resources/function_blocks/) -> Finish
  4. On the System Explorer, open **System Configuration** (**1**). Now add 2 FORTE_PC (**2**) and 1 Ethernet (**3**). Link the Forte PCs to the Ethernet (**4**). Update the port of the second FORTE_PC to 61500 (**5**).

      ![image](../docs/images/Screenshot_1.png)

  5. On the System Explorer, open **MESApp**
  6. From the palette on the right side, drag the following function blocks:
      - **SENSOR_SIMULATOR_V2**
      - **MOVING_AVERAGE_V2**
      - **MQTT_PUBLISHER_V3**
      - **MQTT_SUBSCRIBER_V3**
      - **PROMETHEUS_WRITER**

      ![image](../docs/images/Screenshot_2.png)
  7. Now, proceed to link the function blocks and fill the parameters with:
      - **SENSOR_SIMULATOR_V2**: OFFSET = 0. You can twist this value to emulate, for example, a sensor that can overheat (Offset = 10) or a sensor that is working above the desired temperature (Offset = -10).
      - **MOVING_AVERAGE_V2**: WINDOW = 5. This value is the number of samples that the moving average will use to calculate the average value. You can change this value to see how the moving average changes.
      - **MQTT_PUBLISHER_V3**:
          - TOPIC = "sensor_data". This is the topic that the publisher will use to publish sensor data to.
          - HOST = "localhost". This is the IP address of the MQTT Broker on your machine.
          - PORT = 1883. This is the port of the MQTT Broker on your machine.
          - VALUE_NAME_1 = "sensor_id". This is the id of the sensor.
          - VALUE_NAME_2 = "current_value". This is the current value of the sensor.
          - VALUE_NAME_3 = "moving_average". This is the moving average of the sensor.
      - **MQTT_SUBSCRIBER_V3**:
          - TOPIC = "sensor_data". This is the topic that the subscriber will use to subscribe to.
          - HOST = "localhost". This is the IP address of the MQTT Broker on your machine.
          - PORT = 1883. This is the port of the MQTT Broker on your machine.
          - VALUE_NAME_1 = "sensor_id". This is the id of the sensor.
          - VALUE_NAME_2 = "current_value". This is the current value of the sensor.
          - VALUE_NAME_3 = "moving_average". This is the moving average of the sensor.
      - **PROMETHEUS_WRITER**:
          - HOST = "localhost". This is the IP address of the Prometheus Gateway running on docker.
          - PORT = 9091. This is the port of the Prometheus Gateway running on docker.
          - VALUE_NAME_1 = "sensor_id". This is the id of the sensor.
          - VALUE_NAME_2 = "current_value". This is the current value of the sensor.
          - VALUE_NAME_2_DESCR = "Current value of the sensor". This is the description of the current value of the sensor.
          - VALUE_NAME_3 = "moving_average". This is the moving average of the sensor.
          - VALUE_NAME_3_DESCR = "Moving average of the sensor". This is the description of the moving average of the sensor.
          - JOB_NAME = "sensor_data". This is the job name of the sensor data.

      ![image](../docs/images/Screenshot_3.png)

      NOTE: Make sure to link the function blocks as shown in the image above. This step is important to ensure that the function blocks are linked in the correct order and that it follows the flow of the data.

  8. Link the function blocks to the corresponding FORTE_PC:
      - **SENSOR_SIMULATOR_V2**, **MOVING_AVERAGE_V2**, **MQTT_PUBLISHER_V3**: Right click on the function block -> Select "Map to .." -> Select "FORTE_PC" -> Select "EMB_RES"
      - **MQTT_SUBSCRIBER_V3**, **PROMETHEUS_WRITER**: Right click on the function block -> Select "Map to .." -> Select "FORTE_PC_1" -> Select "EMB_RES"

      ![image](../docs/images/Screenshot_4.png)

  9. Now the systems are ready for deploy. Change to the **Deploy View** (right corner icon or Window -> Perspective -> Open Perspective -> Deployment);

  10. Select your configuration and click Deploy to upload the configuration to the Smart Components;

      ![image](../docs/images/Screenshot_5.png)

  11. To monitor the system, change to the previous view, then right-click on the project folder, and select Monitor System. Now you can select which variables you want to monitor, for that right-click inside the variable and select Watch;

      ![image](../docs/images/Screenshot_7.png)

  12. To stop the monitoring process, right-click in the project folder and select Remove Watches and unselect Monitor System;

  13. If you want to reset each component, right-click in his name in the left bar and select Delete all Resources;

  14. Finally, to check the data structure or monitor the process using OPC-UA, you can use the [Prosys client](https://www.prosysopc.com/products/opc-client/), connecting to the component IP address at port 4840 and 4841.

## Security concerns

Identify potential security vulnerabilities classes and explain what the team has done to mitigate them.


## Quality assurance

Describe which tools are used for quality assurance and link to relevant resources. Namely, provide access to reports for coverage and mutation analysis, static analysis, and other tools that may be used for QA.


## Metrics

Describe how you captured each of the "four key metrics" (e.g., automatic mechanism, survey to the team on the end of each sprint).

Provide here an historical record (for each sprint) of the four key metrics and velocity.

| Sprint | Velocity (T1) | Velocity (T2) | Velocity (T3) | Velocity (T4) | Velocity (Product) |
|-------------|-------------|-------------|-------------|-------------|-------------|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 8 | 0 | 2 | 10 |
| 2 | 10 | 3 | 0 | 0 | 13 |
| 3 |  |  |  |  |  |
| 4 |  |  |  |  |  |

## Restrospectives

### **Sprint 1 (12 October - 26 October)**

#### Project Retrospective

#### Team 1 Retrospective
For the first sprint, our team's objectives were to create a database suitable for static and real-time data, setup Grafana, design and implement a page that allows workers to view machine logs and characteristics, and we were also responsible ([João Araújo](../factsheets/team1/joao_araujo.md)) with helping other team members. In conclusion, we were able to do most tasks, but work still needs to be done.

After the sprint has ended, looking back we noticed we need to improve in some topics, just as, be more active in Discord and in the team overall, improve the user stories per sprint ratio while also reviewing every user story. However not everything needs to be improved, since the beginning that we developed great cooperation, good pace of work as well as always being ready to share information with other teams. There was also simple bad things that we need to avoid moving forward, like terrible communication inside the team and delays in the factsheets. The most substantial doubts we had in this sprint were related to how is the database developed and updated.


#### Team 2 Retrospective
Negative points :
- Difficulty in organizing the work considering that it was too sequential
- There were some problems when setting up the DINASORE tool and the 4diac IDE

Positive points:
- Good comunication between team members
- Good starting basis regarding the used technology


#### Team 3 Retrospective
During this sprint, our team was assigned the task of developing automatic notifications for events and familiarising with the way they work and are implemented in the Grafana platform. Although we were able to achieve this goal successfully, creating some test notifications, as data was still not dynamic, in large quantity and following a defined pipeline, we were not able to fully develop and test this feature. In conclusion, we acquired all the necessary knowledge to finish this task in the next sprint alongside another task assigned to us, as the work done by the other teams regarding the stream of data will support our development of this feature.

#### Team 4 Retrospective
During sprint 1, our team had to deal with a PBI that was of low priority but high workload, which consisted of creating a ML model that, through the information it receives from the database, manipulates the operation of the machines so that it is as efficient as possible. Our efforts turned to understanding as best as we could how we were going to approach the issue, planning the development and integration of the solution. There was also a limitation on the work we could do, as we needed data we didn't have, since the integration of the sensors with the system had not yet been done and the said ML model needs real data to be trained. So, we plan to continue working in this same issue during next sprint, to finish it as quick as possible.

### **Sprint 2**

#### Team 3 Retrospective
During this sprint, the team continued focusing on the implementation of the automatic notifications feature, that turned out to be badly evaluated in terms of effort estimation, as it was more complex than initially thought. Also, the team had to deal with setup issues of the project. As a dynamic Prometheus data simulator was added by another team, we had to re-do our setup, and this took some time, as the software used to simulate the data (Dinasore and 4DIAC-IDE) was excessively complex and not well maintained in terms of versioning and support from the original developers. The team was also able to conclude that, using Grafana, there is no viable way for the user that receives the notification to acknowledge it: there is only going to be another notification when the issue is resolved (e.g., the temperature is back to normal). This is a limitation of Grafana. For the other points of the user story that was attributed to us, we were able to implement them successfully, and notifications are working based off dynamic data from sensors that is being streamed from Prometheus to Grafana.
However, the team considers that the feature is done, although it can be refined in future iterations of the project, as more data becomes available (e.g. discrimination between temperature/pressure types), which will enable to define more suitable ranges for each type of sensor.

### **Sprint 3**

### **Sprint 4**


