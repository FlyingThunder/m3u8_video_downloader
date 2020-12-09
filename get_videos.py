from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import pyautogui
import clipboard
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv("cbtname")
password = os.getenv("cbtpw")
userpath = os.getenv("userpath")
driverpath = os.getenv("driverpath")

capabilities = DesiredCapabilities.CHROME
capabilities["goog:loggingPrefs"] = {"performance": "ALL"}  # chromedriver 75+
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={userpath}") #Path to your chrome profile
options.add_argument("--auto-open-devtools-for-tabs")
driver = webdriver.Chrome(executable_path=f"{driverpath}", options=options)
driver.get("https://www.cbtnuggets.com/login")
logs = driver.get_log("performance")
clipboard.copy("")



def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None

driver.implicitly_wait(2)
print("Logging in")

try:
    USERNAME = driver.find_element_by_xpath('//*[@id="email"]')
    USERNAME.send_keys(f"{username}")
    PASSWORD = driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div[1]/form/fieldset/div[2]/input")
    PASSWORD.send_keys(f"{password}")
    Login_Button=driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div[1]/form/fieldset/button")
    Login_Button.click()
except:
    print("already logged in")

def get_m3u8_video(url):
    time.sleep(1)
    print("Loading new video")
    driver.get(url)

    time.sleep(5)
    title = driver.find_element_by_xpath("/html/body/div/div[2]/main/div/div/section/section[1]/div[3]/div/div/span").text
    print(title)
    time.sleep(0.5)

    print("Video loaded. Moving Cursor")
    pyautogui.moveTo(1200, 540, duration=2)
    print("Cursor moved. Waiting for page to finish loading, then copying URL")
    time.sleep(4)
    print("Page loaded. Copying URL")
    pyautogui.click(button="right")
    time.sleep(0.5)
    pyautogui.press("c")
    time.sleep(0.5)
    pyautogui.press("c")
    time.sleep(0.5)
    pyautogui.press("c")
    time.sleep(0.5)
    pyautogui.press("right")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)

    with open("dump.txt", "a+") as dumpfile:
        dumpfile.write(str({'video': title, 'url': clipboard.paste()}))
        dumpfile.write("\n")

x = 130 #start video
while x < 461:
    get_m3u8_video(f"https://www.cbtnuggets.com/learn/it-training/playlist/nrn:playlist:user:5fcf88f463ebba00155acb18/{x}?autostart=1")
    x += 1