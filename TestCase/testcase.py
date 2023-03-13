from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import allure
global driver


def setup():
    global driver
    s = Service("C:\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://127.0.0.1:5005")

allure.step("Entering text`{username}` in textfield")
def enter_textfield(username):
    setup()
    driver.find_element(By.XPATH, "/html/body/center/center/form/input[1]").send_keys(username);    

@allure.description("Validate with valid text")
@allure.severity(severity_level="CRITICAL")
def valid_login():
    setup()
    enter_textfield("hello")
    driver.find_element(By.XPATH, "/html/body/center/center/form/input[2]").click()
    driver.implicitly_wait(5)
    global testcaseoutput_element
    global output
    testcaseoutput_element = driver.find_elements(By.CLASS_NAME, "testcaseoutput")
    output = [x.text for x in testcaseoutput_element]
    output = []
    for x in testcaseoutput_element:
        output.append(x.text)
    if (output == ['Valid_Login']):
        y = 5
        return y
    else:
        y = 6
        return y


@allure.description("Validate with invalid text")
@allure.severity(severity_level="NORMAL")
def invalid_login():
    setup()
    enter_textfield("@#$%")
    driver.find_element(By.XPATH, "/html/body/center/center/form/input[2]").click()
    driver.implicitly_wait(5)
    global testcaseoutput_element
    global output
    testcaseoutput_element = driver.find_elements(By.CLASS_NAME, "testcaseoutput")
    output = [x.text for x in testcaseoutput_element]
    output = []
    for x in testcaseoutput_element:
        output.append(x.text)
    if (output == ['Valid_Login']):
        y = 6
        return y
    else:
        y = 5
        return y


def browser_close():
    driver.quit()

def test_validlogin():
    global output
    output = valid_login()
    assert output == 5
    browser_close()


# def test_invalidlogin():
#     output = invalid_login()
#     try:
#         assert output == 5
#     finally:
#         if AssertionError:
#             allure.attach(driver.get_screenshot_as_png(),
#                           name="Invalid Text",
#                           attachment_type=allure.attachment_type.PNG)
#             browser_close()