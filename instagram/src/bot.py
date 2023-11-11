# main.py
import secret
import discord
from discord.ext import commands
from agent.actions import InstagramBot, like_photos, comment_photos
from utils.config import IG_USERNAME, IG_PASSWORD, COMMENTS, RANDOM_HASHTAGS
import random

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


@bot.command()
async def login(ctx):
    try:
        instagram_bot = InstagramBot(IG_USERNAME, IG_PASSWORD)
        instagram_bot.login()
        await ctx.send("Logged in to Instagram.")
    except:
        await ctx.send("Failed to log in to Instagram.")


@bot.command()
async def like(ctx):
    try:
        like_photos()
        await ctx.send("Liked photos on Instagram.")
    except:
        await ctx.send("Failed to like photos on Instagram.")


@bot.command()
async def comment(ctx):
    try:
        for hashtag in RANDOM_HASHTAGS:
            comment_photos(hashtag, random.choice(COMMENTS))
            await ctx.send(f"Commented on photos with the hashtag {hashtag}.")
        await ctx.send("Finished commenting on Instagram photos.")
    except:
        await ctx.send("Failed to comment on Instagram photos.")


if __name__ == "__main__":
    bot.run(secret.discord_bot["token"])
