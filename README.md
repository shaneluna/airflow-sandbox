# Airflow Sandbox
This is a sandbox project for me to explore [Apache Airflow](https://airflow.apache.org/).

# Getting Started
Following [these](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html) instructions.
- Install prerequisites
    - docker
    - docker-compose
- Run init.sh from the command line: `sh airflow-init.sh`
    - The account created has the login `airflow` and password `airflow`.
- Start all services: `docker-compose up`
    - Note: To stop and delete containers, delete volumes with database data and download images, run: `docker-compose down --volumes --rmi all`