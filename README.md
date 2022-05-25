# About 

Simple example of data integration process with Apache Airflow in Docker.
Source — API exchangerate.host (https://exchangerate.host/).
Destination — PostgreSQL database. 

## Workflow

exchangerate.host API -> Apache Airflow -> PostgreSQL

## Installation

**Before anything else, you need Docker and `docker-compose` installed.*
(https://docs.docker.com/desktop/windows/install/)
**More details about running AirFlow in Docker*
(https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html)


1. Clone the repository in local folder.
2. Create a `.env` file in the project directory, and add the following variables:
    - `AIRFLOW_UID=50000`
    - `AIRFLOW_GID=0`
3. Execute the command `docker-compose up airflow-init` from the root of the project directory.
4. Execute the command `docker-compose up` from the root of the project directory.
5. Navigate to `localhost:8080` to view the Airflow UI (User: `airflow`; Pwd: `airflow`).

## Setup pgAdmin (for validating the result of ETL process)
1. Navigate to `http://localhost:5050/browser` to view the pgAdmin UI (User: `pgadmin4@pgadmin.org`; Pwd: `admin1234`).
2. Register a new server with the following parameters: 
    - Server name: `postgres_server`
    - Host name/address: `postgresql_etl_server`
    - Port: `5432`
    - Maintenance database: `exchangerate_db`
    - Username: `admin`
    - Password: `admin1234`
 3. Select data from the table `public.exchangerates`


6. To stop and delete containers, delete volumes with database data and download images, run: `docker-compose down --volumes --rmi all`