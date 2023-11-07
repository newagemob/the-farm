import secret
import os
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from pathlib import Path

parent_dir = Path(__file__).parent.absolute()

# SoundCloud link to the track you want to stream
soundcloud_url = secret.soundcloud["url"]

# Define the maximum streaming duration (100 seconds in this case)
max_streaming_duration = 100

def stream_track():
    # Set up Firefox WebDriver with options (you can customize this further)
    options = Options()
    options.headless = False  # Set to True for headless mode
    driver = webdriver.Firefox(options=options)

    while True:  # This loop runs indefinitely until manually stopped
        try:
            # Start the Firefox WebDriver and open the SoundCloud URL
            driver.get(soundcloud_url)
            time.sleep(3)

            # Find the play button element by class and role attributes
            play_button = driver.find_element(
                By.XPATH, "//a[@role='button'] [@class='sc-button-play playButton sc-button m-stretch'] [@tabindex='0'] [@title='Play']")

            # If the play button is found, simulate a click event
            if play_button:
                play_button.click()
                print("Play button found and triggered.")

                # Stream the track for a random duration between 60 to 100 seconds
                streaming_duration = random.uniform(40, 70)
                time.sleep(streaming_duration)

            else:
                print("Play button not found on the page.")

        except Exception as e:
            print(f"Error: {str(e)}")
        finally:
            # refresh the page
            driver.refresh()

if __name__ == "__main__":
    stream_track()
    # This script will keep streaming the track in an infinite loop until manually stopped.
