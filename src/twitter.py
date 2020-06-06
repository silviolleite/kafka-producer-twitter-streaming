import tweepy

from src.kafka import KafkaProducer


class StreamListener(tweepy.StreamListener):
    """
    This is a class provided by tweepy to access the Twitter Streaming API.
    """

    def __init__(self):
        """
        The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
        """
        super().__init__(
            api=tweepy.API(
                wait_on_rate_limit=True,
                wait_on_rate_limit_notify=True,
                timeout=60,
                retry_delay=5,
                retry_count=10,
                retry_errors={401, 404, 500, 503}
            )
        )

    producer = KafkaProducer()

    def on_connect(self) -> None:
        """
        Called initially to connect to the Twitter Streaming API

        :return: void
        """
        print("You are now connected to the Twitter streaming API.")

    def on_error(self, status_code: int) -> bool:
        """
        On error - if an error occurs, display the error / status code

        :param status_code: int
        :return: bool
        """
        print("Error received in kafka producer " + repr(status_code))
        return True

    def on_data(self, data: str) -> bool:
        """
        This method is called whenever new data arrives from live stream.
        We asynchronously push this data to kafka queue.

        :param data: JSON
        :return: bool
        """
        try:
            self.producer.send(data)
        except Exception as e:
            print(e)
            return False
        return True

    def on_timeout(self) -> bool:
        """
        Don't kill the stream

        :return: bool
        """
        return True
