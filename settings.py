"""
Settings for Twitter Producer project.
"""

from decouple import config

# KAFKA settings
TOPIC = config('TOPIC', default='')
BROKER_URL = config('BROKER_URL', default='localhost:9092')

# Twitter API settings
TWITTER_API_KEY = config('TWITTER_API_KEY')
TWITTER_API_SECRET = config('TWITTER_API_SECRET')
TWITTER_ACCESS_TOKEN_KEY = config('TWITTER_ACCESS_TOKEN_KEY')
TWITTER_ACCESS_TOKEN_SECRET = config('TWITTER_ACCESS_TOKEN_SECRET')

# Keywords list to filter tweets
TWITTER_FILTER_WORDS = ['coronavirus', 'covid19', '#covid19', '#brasil', 'corona', '#corona', 'virus', '#virus']
