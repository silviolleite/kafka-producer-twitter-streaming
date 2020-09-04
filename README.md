# Kafka Producer using the Twitter API

A basic project to demonstrate a kafka producer with tweets in real time   

[![](https://img.shields.io/github/license/embrace-inpe/swds-api-downloader.svg)](https://github.com/embrace-inpe/swds-api-downloader/blob/master/LICENSE)
[![](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/)

## Getting Started

### Installing Kafka

First, we need to install an Apache Kafka docker image for developers.
For it I am using the `landoop/fast-data-dev`, it has a full fledged Kafka installation up and running in seconds.

```shell script
$ docker run --rm --net=host -p 2181:2181 -p 3030:3030 -p 8081-8083:8081-8083 \
       -p 9581-9585:9581-9585 -p 9092:9092 -e ADV_HOST=192.168.99.100 \
       lensesio/fast-data-dev:latest
```

Further details: [https://github.com/lensesio/fast-data-dev](https://github.com/lensesio/fast-data-dev)


### Creating a Kafka topic and consumer  

Let's open a new terminal with a new instance of a `fast-data-dev` container's shell, we just need to run the following:

```shell script
$ docker exec -it fast-data-dev /bin/bash
```

Next, we will create the topic.

```shell script
$ kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 3 --topic twitterTopic
```

After we can start a consumer.

```shell script
$ kafka-console-consumer --bootstrap-server localhost:9092 --topic twitterTopic --group twitter-group
```

Now that we have Kafka ready!

The producer will get tweets from the Twitter API and push those tweets in JSON form to our topic that we created earlier.


### Isolated environment

The `venv` module provides support for creating lightweight “virtual environments” with their own site directories, optionally isolated from system site directories. Each virtual environment has its own Python binary (which matches the version of the binary that was used to create this environment) and can have its own independent set of installed Python packages in its site directories.

See [PEP 405](https://www.python.org/dev/peps/pep-0405) for more information about Python virtual environments. 

Creation of virtual environments is done by executing the command:

```shell script
python3 -m venv .venv
```
Running this command creates the target directory `.venv` on root.


Once a virtual environment has been created, it can be “activated” using a script in the virtual environment’s binary directory.

```shell script
source .venv/bin/activate
```


To deactivate run:

```shell script
deactivate
```

All the commands bellow you must assume that your `venv` is activated.

### Install dependencies

All the project dependencies are mapped on `requirements.txt`.
To install it run:
```shell script
$ pip install -r requirements.txt
```

### Environment file

We use [decouple](https://github.com/henriquebastos/python-decouple) for strict separation of settings from code. It helps us with to store parameters in `.env` file and properly convert values to correct data type.

Copy the file `.env-example` to a `.env` file and replace the values inside of it.

> You must set the `TOPIC` with the Kafka topic created previously 

### Settings
Create a `.env` file and copy all content from 
You must change the keyword list `TWITTER_FILTER_WORDS` on `settings.py` to filter tweets with your favorite keywords.


## Run the project

```shell script
$ python3 twitter-producer.py
```

Or

```shell script
$ ./twitter-producer.py
```
