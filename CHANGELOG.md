# CHANGELOG

<!--
Refer to [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) for guidelines on how to create a good changelog.

Note that the notion of a "changelog" (or of "release notes") is a common practice for projects with well establised releases, but is harder to adopt when using continuous deployment. You may need to adapt the guidelines above if that is your case.
-->

## [0.0.1] - 2023-09-30

### Added

- Initial README.md
- Initial project structure
- Initial documentation structure
- `src` folder with code of a demo
- First demo of the product according to our initial vision
    - Includes a simple simulation of the sensors data collection through HTTP requests
    - Includes a Docker Compose file to run the demo in a containerized environment
    - Includes a Grafana instance to visualize data
    - Includes a simple dashboard with the environment of the factory
    - Includes a simple dashboard with the data collected by the sensors being updated at runtime
    - Includes a README.md with instructions on how to run the demo

## [0.0.2] - 2023-10-27

### Added
- Inclusion of DINASORE in the project
    - Includes a README.md with instructions on how to run it
    - Includes a Docker Compose file to run DINASORE in a containerized environment
    - Includes 4DIAC-IDE, a tool to create and edit IEC 61499 applications, such as DINASORE
    - Includes function blocks used by DINASORE
    - Includes Unit testing for the function blocks
- Inclusion of the Prometheus Gateway service in a docker container
- Inclusion of the Mosquitto MQTT Broker service in a docker container
    - Includes a configuration file for the MQTT Broker

### Fixed

- Fixed the project README.md of the project to run on MAC OS

### Changed
- Updated README.md with instructions on how to run the project
- Updated Prometheus configuration file to include the new Gateway service
- Updated Docker Compose file to include the new Gateway service
- Updated Docker Compose file to remove the Flask Server
- Updated requirements.txt to include DINASORE dependencies

### Removed
- Removed the Flask Server from the project
    - The Gateway service will be used instead
- Removed the Flask Server dependencies from requirements.txt

## [0.0.3] - 2023-11-24

### Added
- Inclusion of alerting rules in Grafana [#91](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/91).
    - Triggers an alert after reaching a certain threshold.
    - Sends an email/discord message to the user.
- Dockerized the Dinasore instances [#52](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/52).
- Created *Sensor_Simulator_V3* function block [#66](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/66).
- Added Unit Tests for the *Sensor_Simulator_V3* [#66](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/66).
- Added reference graphs for 3 types of sensors to be used both in the *Sensor_Simulator_V3* and to the Machine Learning model [#66](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/66).
- Added CI tools to the project [#66](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/71).
    - Added Pylint as a GitHub Action to verify Python code.
    - Added Python Package using Conda as a GitHub Action to verify Jupyter Notebooks code.
    - Added Bandit as a GitHub Action to analyse the Python code.

### Fixed
- Fixed the [docker-compose.yml](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/blob/main/src/docker-compose.yml) file to run the project on MAC OS.

### Changed
- Updated [development.md](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/blob/main/docs/development.md) with the new additions and updates to the source code and the Sprint retrospectives for each team.
- Updated [product.md](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/blob/main/docs/product.md) with the retrospective of the sprint review for Sprint 2.
- Updated Dinasore's function blocks to be able to receive the hosts and ports of the instances as parameters [#52](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/pull/52)

### Removed
- Removed extra documentation files that were inside the [source folder](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/tree/main/src).
- Removed *Sensor_Simulator_V2* function block.

## [0.0.4] - 2023-12-01

### Added
- Added remote deployment servers & respective [documentation](./docs/development/development_guide.md#staging-production--deployment).
- Added a [Coding Guidelines section](./docs/development/development_guide.md#coding-guidelines) to the development guide.
- Added a [Pylint](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/blob/a8a85476b4c3b894c16eb8c6517d7d08d5f8e578/src/.pylintrc) configuration file for the linter to ignore some potential errors on the default DINASORE blocks.
- Added two [Bandit](https://bandit.readthedocs.io/en/latest/index.html) setup files: [.bandit](../.bandit) to specify the targets and the tests plugins to skip and [bandit.yaml](../bandit.yaml) to specify the directories and/or files that we want to exclude from the verification.
- Added a [Bandit configuration file](../.workflows/bandit.yml) to implement the workflow for the GitHub action.
- Added two new visualizations in Grafana to display the job schedule and its tasks.

### Fixed
- Fixed the [docker-compose.yml](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/blob/main/src/docker-compose.yml) to stop usage of deprecated modules.
- Fixed the [environment.yml](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/blob/a8a85476b4c3b894c16eb8c6517d7d08d5f8e578/environment.yml) to use the correct prefix path for Conda.
- Fixed the [package.yml](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/blob/a8a85476b4c3b894c16eb8c6517d7d08d5f8e578/.github/workflows/package.yml) to run the necessary commands for the worflow to work correctly.


### Changed
- Updated [development.md](https://github.com/FEUP-MEIC-DS-2023-1MEIC06/DS-Project/blob/main/docs/development.md) and separated the development guide, security concerns, quality assurance and retrospective sections into separate files for better readability. 
- Updated `General View` and `System View` dashboards in Grafana to include the host to be used in the datalinks.
- Updated the [create.sql](src/data/create.sql) file to contain the new tables for the job schedule and its tasks.
- Updated the [generator.py](src/data/generator.py) script to include data for the tables of the job schedule and its tasks.

### Removed
...