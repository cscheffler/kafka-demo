Kafka demo scripts
==================

This is the demo kit that accompanies the talk I gave at PyConZA 2015 on Apache
Kafka. It contains

 * scripts for performance testing the kafka-python and pykafka client libraries
 * scripts for demoing a producer and balanced consumers

You can watch the talk here: https://www.youtube.com/watch?v=b8Cj5-LieH0


Dependencies
------------

This demo requires Kafka 0.8.2. If you do not have access to a Kafka cluster,
you can set it up in standalone mode, by downloading it here:

    http://kafka.apache.org/downloads.html

and installing it following the instructions here:

    http://kafka.apache.org/documentation.html#quickstart

You will also need the kafka-python and pykafka client libraries. You can just
pip install them (but see version notes below for pykafka).

I used kafka-python 0.9.4 and pykafka 2.0.1.

At the time of writing, pykafka 2.0.1 hasn't been released yet. 2.0.0 has some
bugs that break the performance testing code. These have been fixed and will be
available in 2.0.1, but for now you will have to install pykafka from the
master branch of the source repo at https://github.com/Parsely/pykafka


Configuration
-------------

Edit at settings.conf to connect to your Kafka and Zookeeper hosts. By default,
it is set up for a standalone Kafka installation on localhost.

For the tests below to run properly, create a topic called "test" by executing

    cd /opt/kafka
    ./bin/kafka-topics.sh --topic test --partitions 6 --create \
        --zookeeper localhost:2181 --replication-factor 1

The test topic will have 6 partitions (more on this in demo 4 below).

To check that your topic got created properly, you can execute

    ./bin/kafka-topics.sh --describe --zookeeper localhost:2181


Demo 1: Running a producer
--------------------------

python demo-producer.py

This will produce messages as fast as possible and display how many got
produced, once every 5 seconds.


Demo 2: Running a consumer
--------------------------

python demo-consumer.py

This will consume already produced messages as fast as possible and display how
many got consumed, once every 5 seconds. It will also show the list of
partitions from which messages got consumed. More on this in demo 4.


Demo 3: Clearing out your Kafka and Zookeeper data
--------------------------------------------------

To delete all Kafka logs and Zookeeper data, you can do the following. This is
for test purposes only and should obviously never be done in production.

  1. Stop your Kafka server
  2. Stop your Zookeeper server
  3. rm -Rf /tmp/zookeeper/*
     This is the default data location for a standalone Zookeeper install. See
     the dataDir property in config/zookeeper.properties for where your
     installation is storing things.
  4. rm -Rf /tmp/kafka-logs/*
     This is the default data location for a standalone Kafka install. See the
     log.dirs property in config/server.properties for where your installation
     is storing its Kafka logs.
  5. Start your Zookeeper server
  6. Start your Kafka server
  7. Re-create your Kafka topics


Demo 4: Running a producer and multiple, balanced consumers
-----------------------------------------------------------

Run demo-producer.py and a few copies of demo-consumer.py simultaneously, in
different terminals. You should see that the different consumers automatically
read from different partitions. If a consumer is killed or added, the
partitions being read will automatically be rebalanced between the consumers.

Note that this will work only if your topic has more than 1 partition. Nothing
useful happens if you have more consumers than you have partitions. See the
"Configuration" section above on how to create a topic with multiple
partitions.


Demo 5: Performance tests
-------------------------

