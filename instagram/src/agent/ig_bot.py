# instagram_bot.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import random


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(2)
        user_element = driver.find_element(By.NAME, "username")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element(By.NAME, "password")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        print("Logged in as " + self.username)
        time.sleep(10)

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)
        # scroll down to load more photos
        for i in range(1, 3):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(2)

        # searching for photos -- grab anchors with a child div with th class name "_aagv" and an img tag inside of it
        hrefs = driver.find_elements(By.XPATH, "//a[contains(@href, '/p/')]")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]

        # sleep for a little bit longer to stay not sus
        time.sleep(random.randint(4, 6))

        # print the current hashtag the bot is searching through
        print(hashtag + " photos: " + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            try:
                # like button is in span with the class name of "_aamw"
                # use this to avoid `429 error: too many requests` -- Instagram does not like bots, but we must persist against the thots
                time.sleep(random.randint(2, 4))
                current_pic = driver.find_element(
                    # like button should be a div with a class "x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x6s0dn4 xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1ypdohk x78zum5 xl56j7k x1y1aw1k x1sxyh0 xwib8y2 xurb0ha xcdnw81" and a role "button"
                    By.XPATH, "//div[@class='x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x6s0dn4 xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1ypdohk x78zum5 xl56j7k x1y1aw1k x1sxyh0 xwib8y2 xurb0ha xcdnw81']"
                )
                print(current_pic)
                current_pic.click()
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


    def follow(self, hashtag):
        driver = self.driver


    def unfollow(self, hashtag):
        driver = self.driver


    def close_browser(self):
        self.driver.close()

    def quit_browser(self):
        self.driver.quit()
