# ETL
ETL with Apache Airflow and Spark

# Part 1: PySpark

Create a folder called bitnami. Download and place the docker compose file in this folder by using the following cURL command:\
`curl https://raw.githubusercontent.com/bitnami/bitnami-docker-spark/master/docker-compose.yml -o docker-compose.yml`

Fire up a docker container by navigating to the bitnami folder in terminal and executing the docker config file, `docker-compose up`
note: for Apple silicon users, insert 'platform: linux/amd64' before the image in the docker compose file

The Data: \
copy the `departuredelays.csv` file from this repo to the docker file, 'bitnami_spark_1' container. Verify it has successfully been installed.

We need to copy data from the bitnami folder to the docker container. To do this, run a docker cp command from the data folder on your local machine: `docker cp departuredelays.csv bitnami_spark_1:departuredelays.csv`. Confirm the file was transferred by opening CLI for the docker container. This is accomplished by finding the container ID by executing `docker ps`. Then, entering the docker by executing `docker exec -it <container_id> /bin/bash`

Using the docker CLI, open PySpark:`pyspark`
Start a PySpark session by entering the following: 
`from pyspark.sql import SparkSession`
#spark session
`spark = (SparkSession
    .builder
    .appName("DepartureDelays")
    .getOrCreate())`
 
From the PySpark interface, run the code below to load the departuredelays.csv file

Define path to data
`csv_file = "/departuredelays.csv"`

Create a dataframe with all entries in csv
`df  = (spark.read.format("csv")
    .option("interSchema", "true")
    .option("header", "true")
    .load(csv_file))`

create a view of the dataframe
`df.createOrReplaceTempView("delays_table")`

Query the data from the view
`spark.sql("""SELECT distance, origin, destination FROM delays_table WHERE distance > 1000 ORDER BY distance DESC""").show(10)`

# Part 2: Airflow
Get the docker config file
Create an empty folder called airflow on your local machine. Navigate to the airflow folder within Terminal and pull the airflow file via cURL
`curl 'https://airflow.apache.org/docs/apache-airflow/2.1.1/docker-compose.yaml' -o docker-compose.yaml`

Open the generated docker-compose.yaml file. Under "environment", set teh AIRFLOW__CORE__LOAD_EXAMPLES variable equal to false.

Open the docker by navigating to the directory with docker-compose.yaml in terminal and executing `docker-compose up`. When the container is established, an interface will be accessible locally at https://localhost:8080. 

<insert image of airflow>
The system can be accessed by using the default user name and password, "airflow."

<insert image of DAGs>

Start the DAG by toggling the switch to the leeft of its name. Select the DAG and open up the Graph View. Select the DAG again and open "logs" to confirm the operation was run successfully. 

<insert image of logs>














