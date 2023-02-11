from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os



def setup():
    current_dir = os.getcwd()
    direc = os.path.join(current_dir, "chromedriver.exe")
    global driver
    s = Service(direc)
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://127.0.0.1:5005")


def valid_login():
    setup()
    y = 5
    driver.find_element(By.XPATH, "/html/body/center/form/input[1]").send_keys("Hello")
    driver.find_element(By.XPATH, "/html/body/center/form/input[2]").click()
    driver.implicitly_wait(5)
    global testcaseoutput_element
    global output
    testcaseoutput_element = driver.find_elements(By.CLASS_NAME, "testcaseoutput")
    output = [x.text for x in testcaseoutput_element]
    output = []
    for x in testcaseoutput_element:
        output.append(x.text)
    if (output == ['Valid_Login']):
        return y
    else:
        y = 6

def browser_close():
    driver.quit()
