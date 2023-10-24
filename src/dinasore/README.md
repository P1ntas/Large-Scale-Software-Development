![logo](https://github.com/DIGI2-FEUP/dinasore/wiki/images/logo.png)

## Contents

- [Installation Guide](#installation-guide)
- [References](#references)


## Installation Guide

- Install the [Mosquitto Broker](https://mosquitto.org/download/) for your system under the default directory.

- Proceed to install the [requirements](../config/requirements.txt) if you haven't already, by running the [install.bash](../install.bash) if you are on Linux/Mac or the [install.bat](../install.bat) if you are on Windows.

- Install 4DIAC-IDE for your system, using any these permalinks:
    - [4diac IDE 1.11.0 Windows 64-bit](http://www.eclipse.org/downloads/download.php?file=/4diac/releases/1.11/4diac-ide/4diac-ide-incubation_1.11.0-win32.win32.x86_64.zip)
    - [4diac IDE 1.11.0 Linux 64-bit](http://www.eclipse.org/downloads/download.php?file=/4diac/releases/1.11/4diac-ide/4diac-ide-incubation_1.11.0-linux.gtk.x86_64.tar.gz)
    - [4diac IDE 1.11.0 Mac OS X](http://www.eclipse.org/downloads/download.php?file=/4diac/releases/1.11/4diac-ide/4diac-ide-incubation_1.11.0-macosx.cocoa.x86_64.dmg)

    **NOTE**: In case the permalinks get outdated, you can install using the from this [online folder](https://drive.google.com/drive/folders/1BG9jSN6q5V6J5MTj7w3r6gF6OH6iEOvm)

    **NOTE**: For more details about the 4DIAC-IDE, check this [link](https://eclipse.dev/4diac/en_help.php?helppage=html/4diacIDE/overview.html).

    **NOTE**: After instalation, ensure you have the 4DIAC-IDE outside of the root of this project, otherwise it will be submited to git.


## How to Run

- Start by running the Mosquitto Broker. For that, you can run the following command under the mosquitto folder:
    ```sh
    net start mosquitto
    ```

    The broker should be running on the default port `1883` (keep this in mind for the next steps).

- Then, open the 4DIAC-IDE and import the [DINASORE](../config/DINASORE) project. To do that, go to `File > Import... > General > Existing Projects into Workspace` and select the [DINASORE](../config/DINASORE) folder.

- Then, in order to run DINASORE on your system, you need to run the following commands:
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


## Learn More

- [DINASORE - A tool for distributed function-block-based systems](https://medium.com/@jrffmatias/dinasore-a-tool-for-distributed-function-block-based-systems-f2613a37e1ca). This article explains the main features of DINASORE with a simple example.

- [Prosys OPC UA Browser 4.4.0-126](https://www.prosysopc.com/products/opc-client/). This OPC client can be used to observe the results of the OPC UA server built in DINASORE.

- [Step 0 - 4diac IDE Overview](https://eclipse.dev/4diac/en_help.php?helppage=html/4diacIDE/overview.html). This page explains how you can setup the 4diac IDE and how to use it more explicitly.

## References

This project was developed using DIGI2 [Dinasore](https://github.com/DIGI2-FEUP/dinasore) and this readme was based on their [installation guide](https://github.com/DIGI2-FEUP/dinasore/wiki/1.-Install), constricting to the needs of our project.
