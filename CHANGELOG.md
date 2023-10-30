# CHANGELOG

Refer to [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) for guidelines on how to create a good changelog.

Note that the notion of a "changelog" (or of "release notes") is a common practice for projects with well establised releases, but is harder to adopt when using continuous deployment. You may need to adapt the guidelines above if that is your case.

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