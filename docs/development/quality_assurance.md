# Quality Assurance

Continuous Integration (CI) tools are currently set in place to ensure correct codebase management and consistency. In terms of static analysis, code is scanned using linters everytime a PR wants to commit changed into the _main_ branch. Furthermore, a [SonarQube](https://www.sonarsource.com/products/sonarqube/?gads_campaign=SQ-Mroi-PMax&gads_ad_group=Global&gads_keyword=&gad_source=1&gclid=CjwKCAiAu9yqBhBmEiwAHTx5pxnFfXXnEDXFcodcgZRO5zP1ALPlJ4zaqIEvecU6Sz8-9v2VsiagzxoCHjUQAvD_BwE) environment was setup, giving us access to more code analysis and extensive reports about bugs, security and vulnerabilities.
The Continuous Integration linter is complaining, however, about some default formatting of the DINASORE blocks (source code for the DINASORE technology, which should not be changed), which can cause problems in the future.

## SonarQube - Latest scan on branch `main`

The Sonar scanner reports a 6.0% code duplication. Additionally, the coverage report reveals a 3.2% code coverage. Regarding code smells, the scanner identifies 79 instances but assigns an A-grade rating for maintainability. In terms of reliability, the scanner points out 2 bugs.

![SonarQube Quality Rating](../images/sonarqube_quality.png)

Regarding code coverage, a lot of components that already came integrated with the DINASORE technology are not covered by tests. This is because the DINASORE technology is not supposed to be changed. If we only consider the implemented components, the coverage increases to 20.3%. The other statistics also improve.

![SonarQube Quality Rating](../images/sonarqube_quality_2.png)
