from pykafka import KafkaClient
import time
import uuid
try:
    import configparser  # Python 3
except ImportError:
    import ConfigParser as configparser  # Python 2


config = configparser.ConfigParser()
config.read('settings.conf')

kafka_client = KafkaClient(hosts=config.get('kafka_demo', 'kafka_hosts'))  # Create Kafka client
topic = kafka_client.topics[config.get('kafka_demo', 'topic')]  # This will create the topic if it does not exist
display_interval = int(config.get('kafka_demo', 'display_interval'))

print 'Producing messages to topic %r. Press Ctrl-C to interrupt.' % topic.name
display_iteration = 0
message_count = 0
start_time = time.time()
with topic.get_producer() as producer:  # Create Kafka producer on the given topic
    while True:
        identifier = str(uuid.uuid4())  # Encode the message (this should result in a byte string)
        producer.produce(identifier)  # Send the message to Kafka
        message_count += 1
        now = time.time()
        if now - start_time > display_interval:
            print '%i) %i messages produced at %.0f messages / second' % (
                display_iteration,
                message_count,
                message_count / (now - start_time))
            display_iteration += 1
            message_count = 0
            start_time = time.time()
