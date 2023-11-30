# main.py
import secret
import discord
from discord.ext import commands
from agent.ig_bot import InstagramBot
from utils.config import (
    RANDOM_HASHTAGS,
    LIQUID_TARGET_DEMO_HASHTAGS,
    RANDOM_HASHTAGS,
    IG_USERNAME,
    IG_PASSWORD,
    COMMENTS,
)
import random
import time

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())
stop_task = False


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


@bot.command()
async def stop(ctx):
    global stop_task
    stop_task = True
    await ctx.send("Stop signal received. Stopping the current task.")


@bot.command()
async def like(ctx):
    global stop_task
    try:
        bot = InstagramBot(IG_USERNAME, IG_PASSWORD)
        bot.login()
        await ctx.send("Logged in to Instagram.")

        for hashtag in RANDOM_HASHTAGS:
            if stop_task:
                await ctx.send("Stop signal received. Stopping the current task.")
                break

            try:
                bot.like_photo(hashtag)
                await ctx.send(f"Liked photos with the hashtag {hashtag}.")
                time.sleep(5)
            except Exception as e:
                print(f"Error liking photos with hashtag {hashtag}: {e}")
                await ctx.send(f"Failed to like photos with the hashtag {hashtag}.")

    except Exception as e:
        print(f"Error logging in to Instagram: {e}")
        await ctx.send("Failed to login to Instagram.")
    finally:
        stop_task = False


@bot.command()
async def comment(ctx):
    try:
        bot = InstagramBot(IG_USERNAME, IG_PASSWORD)
        bot.login()
        await ctx.send("Logged in to Instagram.")

        for hashtag in RANDOM_HASHTAGS:
            if stop_task:
                await ctx.send("Stop signal received. Stopping the current task.")
                break

            try:
                bot.comment_photo(hashtag, random.choice(COMMENTS))
                await ctx.send(f"Commented on photos with the hashtag {hashtag}.")
                time.sleep(5)
            except Exception as e:
                print(f"Error commenting on photos with hashtag {hashtag}: {e}")
                await ctx.send(
                    f"Failed to comment on photos with the hashtag {hashtag}."
                )
        await ctx.send("Finished commenting on Instagram photos.")
    except:
        await ctx.send("Failed to comment on Instagram photos.")


if __name__ == "__main__":
    bot.run(secret.discord_bot["token"])
