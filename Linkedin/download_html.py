from selenium import webdriver
import time

chromedriver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver.exe")

url = "https://www.linkedin.com/uas/login"

chromedriver.get(url)

#print(chromedriver.page_source)

email = chromedriver.find_element_by_xpath('//*[@id="session_key-login"]')

email.send_keys("ayodapov@gmail.com")

password = chromedriver.find_element_by_xpath('//*[@id="session_password-login"]')

password.send_keys("ayo3276dapov")

sign_in = chromedriver.find_element_by_xpath('//*[@id="btn-primary"]')

sign_in.click()

time.sleep(1000)

chromedriver.quit()