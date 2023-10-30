# MES for Industrial Automation

Our product aims to be a helpful, all-encompassing tool for industrial organizations to achieve the goals of [Industry 4.0](https://www.ibm.com/topics/industry-4-0) that consist in improving product quality, reducing costs, and meeting regulatory requirements while staying adaptable to changing market conditions. More information about our product's vision and objectives can be found in the [Product Management](docs/product.md) document.
 

## How to use

Explain how to use your software from user standpoint. This can include short videos, screenshots, or API documentation, depending on what makes sense for your particular software system and target users. If needed, link to external resources or additional markdown files with further details (please place these in the [docs](docs/) directory).

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

### Installation / Setup

- First of all, make sure you are in the `/src` directory of the project.

- If you are running **Windows**, you can use the `install.bat` script. Otherwise, if you are using **Linux** or **Mac OS**, you can use the `install.sh` script.

- **NOTE**: (If your python is tagged as `python3` instead of `python`, you will need to change the scripts accordingly)

- This will install the necessary python packages and create the necessary docker containers, those that matter to the final user is `Grafana` running under the port `3000`, to visualize the data in dashboards and see alerting events, and `Prometheus` running under the port `9090`, to visualize data from sensors manually, as well to see further alerts not shown in the dashboards.

### Usage

#### Prometheus

To access the `Prometheus` interface, go to `localhost:9090`. 

To verify if the data is being scraped correctly, go to the `Status > Targets` tab and check if the `pushgateway` job is up and running. If it is, it should show `UP` under the `State` column.

On the `Expression` tab, you can enter a query to verify the data that is being scraped. For example, you can enter the following queries:
```sql
sensor_value
-- or
sensor_value{sensor_id="1"}
-- or
moving_average{sensor_id="1"}
```
The first one will show all the sensors data, while the second one will only show the value of the sensor with id `1`.

### Grafana

To access the `Grafana` interface, go to `localhost:3000`. Login with the following credentials:
```markdown
**Username**: admin
**Password**: admin
```

Afterwards, you will be redirected to the `Home Dashboard`.

From there, select on the left side the `Dashboards` tab. This will show the available dashboards folders. Select the `General` folder and then select the `General View` dashboard. 

![gif](./docs/images/grafana_home.gif)

Here, you can see the current data hold both by the `PostgreSQL` database and the `Prometheus` database. You can also select the time range of the data to be shown, as well as play with the different variables to see how the data changes.

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

      ![image](./docs/images/Screenshot_1.png)

  5. On the System Explorer, open **MESApp**
  6. From the palette on the right side, drag the following function blocks seen in the image below:

      ![image](./docs/images/Screenshot_2.png)
  7. Now, proceed to link the function blocks and fill the parameters with the following values of the image below:

      ![image](./docs/images/Screenshot_3.png)

  8. Link the function blocks to the corresponding FORTE_PC:
      - **SENSOR_SIMULATOR_V2**, **MOVING_AVERAGE_V2**, **MQTT_PUBLISHER_V3**: Right click on the function block -> Select "Map to .." -> Select "FORTE_PC" -> Select "EMB_RES"
      - **MQTT_SUBSCRIBER_V3**, **PROMETHEUS_WRITER**: Right click on the function block -> Select "Map to .." -> Select "FORTE_PC_1" -> Select "EMB_RES"

      ![image](./docs/images/Screenshot_4.png)

  9. Now the systems are ready for deploy. Change to the **Deploy View** (right corner icon or Window -> Perspective -> Open Perspective -> Deployment);

  10. Select your configuration and click Deploy to upload the configuration to the Smart Components;

      ![image](./docs/images/Screenshot_5.png)

  11. To monitor the system, change to the previous view, then right-click on the project folder, and select Monitor System. Now you can select which variables you want to monitor, for that right-click inside the variable and select Watch;

      ![image](./docs/images/Screenshot_7.png)

  12. Finally, to check the data structure or monitor the process using OPC-UA, you can use the [Prosys client](https://www.prosysopc.com/products/opc-client/), connecting to the component IP address at port 4840 and 4841.

## How to contribute

Explain what a new developer to the project should know in order to develop the system, including who to build, run and test it in a development environment. 

Defer more details about the technical vision to the [development](docs/development.md) documentation, which should include information on architectural, design and technical aspects of the project, justifying the most important choices to show the soundness of the technical vision.

In order to contribute to the project, you have a few options:
- Implement or Update the Grafana Dashboards, including alerting
  - To do so, you can follow the [Grafana Dashboards](docs/grafana.md) documentation.
- Implement or Update the DINASORE's Function Blocks
  - To do so, you can follow the official [DINASORE](https://github.com/DIGI2-FEUP/dinasore/wiki) documentation.

## How to run and operate in a production environment

For a full guide and explanation on the project's environment, technologies and setup, please refer to the [Development Guide](docs/development.md#development-guide).

## Contributions

 * [Team 1](factsheets/team1/team1.md)
   * [Afonso Pacheco](factsheets/team1/afonso_pacheco.md)
   * [Artur Freitas](factsheets/team1/artur_freitas.md) (PO)
   * [João Araújo](factsheets/team1/joao_araujo.md)
   * [José Ramos](factsheets/team1/jose_ramos.md) (SM)
   * [Nuno França](factsheets/team1/nuno_franca.md) 
 * [Team 2](factsheets/team2/team2.md)
   * [Alexandre Costa](factsheets/team2/alexandre_costa.md)
   * [Diogo Fonte](factsheets/team2/diogo_fonte.md)
   * [Fábio Morais](factsheets/team2/fabio_morais.md)
   * [Francisco Prada](factsheets/team2/francisco_prada.md) (SM)
   * [José Castro](factsheets/team2/jose_castro.md) (PO)
   * [Vítor Cavaleiro](factsheets/team2/vitor_cavaleiro.md)
 * [Team 3](factsheets/team3/team3.md)
   * [Afonso Martins](factsheets/team3/afonso_martins.md) (SM)
   * [Anete Pereira](factsheets/team3/anete_pereira.md)
   * [Eduardo Silva](factsheets/team3/eduardo_silva.md)
   * [Hugo Castro](factsheets/team3/hugo_castro.md) 
   * [José Sousa](factsheets/team3/jose_sousa.md)
   * [Luís Paiva](factsheets/team3/luis_paiva.md) (PO) 
 * [Team 4](factsheets/team4/team1.md)
   * [Afonso Pinto](factsheets/team4/afonso_pinto.md) 
   * [Amanda Oliveira](factsheets/team4/amanda_oliveira.md)(SPO)
   * [Duarte Lopes](factsheets/team4/duarte_lopes.md)
   * [Tiago Marques](factsheets/team4/tiago_marques.md)
   * [Tomás Martins](factsheets/team4/tomas_martins.md) (SM)


