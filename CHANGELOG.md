# CHANGELOG

Refer to [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) for guidelines on how to create a good changelog.

Note that the notion of a "changelog" (or of "release notes") is a common practice for projects with well establised releases, but is harder to adopt when using continuous deployment. You may need to adapt the guidelines above if that is your case.

## [0.0.1] - 2020-09-30

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