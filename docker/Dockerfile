FROM apache/airflow:latest

USER root

RUN apt update && \
    apt-get install -y openjdk-17-jdk && \
    apt-get install -y ant && \
    apt-get clean;


ENV JAVA_HOME  /usr/lib/jvm/java-17-openjdk-amd64

USER airflow

RUN pip install apache-airflow-providers-apache-spark
