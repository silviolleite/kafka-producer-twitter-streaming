from confluent_kafka import Producer, Message
from confluent_kafka.cimpl import KafkaError

from settings import TOPIC, BROKER_URL


class KafkaProducer(object):
    """
    This is a class provide a Confluent Kafka Producer.
    """

    def __init__(self):
        # New Confluent Kafka Producer
        self.producer = Producer({'bootstrap.servers': BROKER_URL})

    def send(self, data: str) -> None:
        """
        Send the data to kafka producer

        :param data: str
        :return: void
        """

        # Trigger any available delivery report callbacks from previous produce() calls
        self.producer.poll(0)

        # Asynchronously produce a message, the delivery report callback
        # will be triggered from poll() above, when the message has
        # been successfully delivered or failed permanently.
        self.producer.produce(TOPIC, data.encode('utf-8'), callback=self.delivery_report)

    @staticmethod
    def delivery_report(err: KafkaError, msg: Message) -> None:
        """
        Called once for each message produced to indicate delivery result.
        Triggered by poll()

        :param err: KafkaError
        :param msg: Message
        :return: void
        """
        if err is not None:
            print(f'Message delivery failed: {err}')
        else:
            print(f'Message delivered to {msg.topic()} [{msg.partition()}]')
