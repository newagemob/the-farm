'''
Instagram Engagmenet Bot - Follows, Likes, Comments, Unfollows, Hashtags

This bot will follow, like, comment, and unfollow users based on a list of hashtags. It will also unfollow users that do not follow you back.

This bot uses Selenium to interact with the Instagram website. It is not a bot that uses the Instagram API. This means that it is not as fast as a bot that uses the API, but it is also less likely to get your account banned.

TODO: Add a feature to like comments on posts you have liked.
'''

import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Change these variables to match your own account
# access variables from .env file
username = os.getenv('IG_USERNAME')
password = os.getenv('IG_PASSWORD')

# Change these variables to match your own hashtags
hashtags = []

# Change these variables to match your own comments
comments = []


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(2)
        # login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        # login_button.click()
        # time.sleep(2)
        user_element = driver.find_element("xpath", "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element("xpath", "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        print("Logged in as " + self.username)
        time.sleep(10)

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)

        # searching for photos -- grab anchors with an image inside
        hrefs = driver.find_elements(By.TAG_NAME, "a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        # filtering out non photo links -- only want to click on hrefs with an image
        pic_hrefs = [href for href in pic_hrefs if "/p/" in href]

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                # like button is in span with the class name of "_aamw"
                time.sleep(random.randint(5, 10)) # use this to avoid `429 error: too many requests`
                driver.find_element(By.XPATH, "//span[@class='_aamw']").click() # like the photo
                print(f"liked {pic_href}")
            except Exception as e:
                print(f"error liking {pic_href}")

    def comment(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        # searching for photos
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' photos: ' + str(len(pic_hrefs)))
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                comments = driver.find_elements_by_class_name('Ypffh')
                comments[1].click()
                comment_box = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(2, 4))
                comment_box.send_keys(random.choice(comments))
                time.sleep(random.randint(2, 4))
                comment_box.send_keys(Keys.ENTER)
                time.sleep(random.randint(18, 25))
            except Exception as e:
                time.sleep(2)

    def like_mentions(self):
        driver = self.driver
        driver.get("https://www.instagram.com/" + self.username)
        time.sleep(5)
        # open notifications
        # store each notification in a list
        # for each notification, check if it is a mention
        # if it is a mention, click on the notification and like the comment or photo

    def like_comment(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)
        # like the first comment of each photo

    def follow(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        # searching for photos
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' photos: ' + str(len(pic_hrefs)))
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                driver.find_element_by_xpath("//span[@aria-label='Follow']").click()
                time.sleep(random.randint(18, 25))
            except Exception as e:
                time.sleep(2)

    def unfollow(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        # searching for photos
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' photos: ' + str(len(pic_hrefs)))
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                driver.find_element_by_xpath("//span[@aria-label='Following']").click()
                time.sleep(random.randint(2, 4))
                driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
                time.sleep(random.randint(18, 25))
            except Exception as e:
                time.sleep(2)

    def closeBrowser(self):
        self.driver.close()

    def quitBrowser(self):
        self.driver.quit()


def like_photos():
    bot = InstagramBot(username, password)
    bot.login()

    # actions
    for hashtag in hashtags:
        bot.like_photo(hashtag)
        time.sleep(5)
    # end actions
    time.sleep(1)


def follow():
    bot = InstagramBot(username, password)
    bot.login()

    while True:
        # actions
        bot.follow('python')
        # end actions
        time.sleep(1)


def comment():
    bot = InstagramBot(username, password)
    bot.login()

    while True:
        # actions
        bot.comment('python')
        # end actions
        time.sleep(1)


def unfollow():
    bot = InstagramBot(username, password)
    bot.login()

    while True:
        # actions
        bot.unfollow('python')
        # end actions
        time.sleep(1)


if __name__ == "__main__":
    like_photos()
    # follow()
    # comment()
    # unfollow()
