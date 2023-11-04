# 🚜 IG Combine 🚜

***Fully featured Instagram bot that likes and comments on photos based on hashtags, follows users based on their followers and following and unfollows users at a set interval.***

# Index

- [🚜 IG Combine 🚜](#-ig-combine-)
- [Index](#index)
  - [🤖 Instagram Bot Quick Start 🤖](#-instagram-bot-quick-start-)
  - [🛠 Troubleshooting 🛠](#-troubleshooting-)
  - [⚠️ Disclaimer ⚠️](#️-disclaimer-️)

## 🤖 Instagram Bot Quick Start 🤖

Edit `engage.py` and add you ***Username***, ***Password***, and ***hashtags*** you want to use.

```
pip install -r requirements.txt
```

If you're on a **Mac**, you can run

```
chmod +x mac_run.command

&&

./mac_run.command
```

## 🛠 Troubleshooting 🛠

The most common issues are not being able to log in and photo URLs not loading.

If you're getting the ***`Please wait a few minutes before you try again`*** error, Instagram thinks you're being sus. Wait an hour before running the bot.

If the photo URLs from the hashtags are not loading, try to increase the sleep time in the `like_photo()` function. Check the developer console; if you're getting a 429 error, then Instagram thinks you're being sus again. Wait an hour before running the bot.

## ⚠️ Disclaimer ⚠️

This does *not* use the official Instagram API. I am not responsible for account bans, content generated, or anything this bot produces. Use at your own risk.
