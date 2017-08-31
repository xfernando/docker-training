FROM maven:3.5.0-jdk-8
COPY . /src
WORKDIR /src
RUN mvn package

FROM tomcat:8.0.46-jre8
COPY --from=0 /src/target/SampleTomcatWebAppOnDocker.war /usr/local/tomcat/webapps
