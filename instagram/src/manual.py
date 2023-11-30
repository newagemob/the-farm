# main.py
import time
from agent.ig_bot import InstagramBot
from utils.config import (
    RANDOM_HASHTAGS,
    LIQUID_TARGET_DEMO_HASHTAGS,
    LIQUID_TARGET_DEMO_HASHTAGS_2,
    RANDOM_HASHTAGS,
    IG_USERNAME,
    IG_PASSWORD,
    COMMENTS,
)


def like_photos():
    bot = InstagramBot(IG_USERNAME, IG_PASSWORD)
    bot.login()

    for hashtag in LIQUID_TARGET_DEMO_HASHTAGS_2:
        bot.like_photo(hashtag)
        time.sleep(5)

if __name__ == "__main__":
    like_photos()
    # comment_photos()
    # follow()
    # unfollow()
