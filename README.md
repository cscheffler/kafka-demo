Kafka demo scripts
==================

This is the demo kit that accompanies the talk I gave at PyConZA 2015 on Apache
Kafka. It contains

 * scripts for performance testing the kafka-python and pykafka client libraries
 * scripts for demoing a producer and balanced consumers

You can watch the video here: https://www.youtube.com/watch?v=b8Cj5-LieH0


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

# TODO: create a topic


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


Demo 4: Running a producer and multiple, balanced consumers
-----------------------------------------------------------


Demo 5: Performance tests
-------------------------

