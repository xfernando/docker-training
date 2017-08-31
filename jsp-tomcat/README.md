Sample Tomcat web application built with a multi-stage Dockerfile.

## Usage
```bash
docker build -t sample-tomcat .
docker run -p 8080:8080 sample-tomcat
```

Open your browser to http://localhost:8080/SampleTomcatWebAppOnDocker, if all runs well, you should see a Hello World message and the name of the container. 
