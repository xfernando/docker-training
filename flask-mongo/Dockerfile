FROM python:3.6.1-alpine
MAINTAINER Fernando Calheiros "xfernando@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "./server.py"]
