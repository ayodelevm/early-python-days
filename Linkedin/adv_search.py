from selenium import webdriver
import time

chromedriver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver.exe")

def login_linkedin(myemail, mypassword):

    url = "https://www.linkedin.com/uas/login"

    chromedriver.get(url)

    #print(chromedriver.page_source)

    email = chromedriver.find_element_by_xpath('//*[@id="session_key-login"]')

    email.send_keys(myemail)

    password = chromedriver.find_element_by_xpath('//*[@id="session_password-login"]')

    password.send_keys(mypassword)

    sign_in = chromedriver.find_element_by_xpath('//*[@id="btn-primary"]')

    sign_in.click()

    time.sleep(15)


login_linkedin("ayodapov@gmail.com", "ayo3276dapov")

search_input = chromedriver.find_element_by_xpath('//*[@id="main-search-box"]')
search_input.send_keys('weight loss')

adv_search = chromedriver.find_element_by_xpath('//*[@id="advanced-search"]')
adv_search.click()


//*[@id="id_email"]

