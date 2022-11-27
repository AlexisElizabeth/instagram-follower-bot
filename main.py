from InstaFollower import *
import os

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
INSTAGRAM_USERNAME = "tigertherabbitofsweden"
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
SIMILAR_ACCOUNT = "funny.cute.rabbit"

if __name__ == "__main__":
    insta_follower_bot = InstaFollower(CHROME_DRIVER_PATH)
    insta_follower_bot.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
    insta_follower_bot.find_followers(SIMILAR_ACCOUNT)
    insta_follower_bot.follow()
