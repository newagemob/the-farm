# actions.py
import time
from agent.ig_bot import InstagramBot
from utils.config import RANDOM_HASHTAGS, LIQUID_TARGET_DEMO_HASHTAGS, TECH_HASHTAGS, IG_USERNAME, IG_PASSWORD

def like_photos():
    bot = InstagramBot(IG_USERNAME, IG_PASSWORD)
    bot.login()

    for hashtag in TECH_HASHTAGS:
        bot.like_photo(hashtag)
        time.sleep(5)

# Create similar functions for other actions like follow, comment, and unfollow.
