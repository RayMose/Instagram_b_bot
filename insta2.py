
# from selenium import webdriver
# import time

# class InstaFollower:
#     def __init__(self, webdriver_path):
#         # Initialize the WebDriver
#         self.driver = webdriver.Chrome('C:\\Users\\soYa\\Desktop\\Bots\\chromedriver.exe')

#     def login(self, username, password):
#         # Access Instagram
#         self.driver.get("https://www.instagram.com")

#         # Wait for the page to load
#         time.sleep(2)

#         # Find and interact with the login elements
#         username_input = self.driver.find_element_by_name('auto_nation.io')
#         password_input = self.driver.find_element_by_name('@autosil1')

#         # Send Instagram credentials
#         username_input.send_keys(username)
#         password_input.send_keys(password)

#         # Locate and click the login button
#         login_button = self.driver.find_element_by_xpath('//button[@type="submit"]')
#         login_button.click()

#         # Wait for the page to load after login
#         time.sleep(3)

#     def find_followers(self, profile_username):
#         # Navigate to the desired profile
#         profile_url = f"https://www.instagram.com/{automation}"
#         self.driver.get("https://www.instagram.com/explore/tags/automation/")
#         time.sleep(2)

#         # Find and click the followers button
#         followers_button = self.driver.find_element_by_xpath('//a[contains(@href, "/followers/")]')
#         followers_button.click()
#         time.sleep(2)

#         # Scroll the followers list
#         followers_list = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
#         for _ in range(10):
#             self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_list)
#             time.sleep(1)

#     def follow(self):
#         # Find and click the follow button for each follower
#         follow_buttons = self.driver.find_elements_by_xpath('//button[contains(text(), "Follow")]')
#         for button in follow_buttons:
#             button.click()
#             time.sleep(1)

#     def quit(self):
#         # Close the browser
#         self.driver.quit()

# # Initialize the object and call the three methods in order
# bot = InstaFollower(r'C:\Users\soYa\Desktop\Bots\chromedriver.exe')
# bot.login('auto_nation', '@autosil1')
# bot.find_followers('#automation')
# bot.follow()
# bot.quit()




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

CHROME_DRIVER_PATH = r"C:\Users\soYa\Desktop\Bots\chromedriver"
SIMILAR_ACCOUNT = "automation"
USERNAME = "auto_nation.io"
PASSWORD = "@autosil1"


class InstaFollower:

    def __init__(self, path):
        self.driver_service = Service(executable_path=path)
        self.driver = webdriver.Chrome(service=self.driver_service)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element_by_name("auto_nation.io")
        password = self.driver.find_element_by_name("@autosil1")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        pass

    def follow(self):
        pass


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()