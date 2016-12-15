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

    time.sleep(10)

login_linkedin("ayodapov@gmail.com", "ayo3276dapov")

search_input = chromedriver.find_element_by_xpath('//*[@id="main-search-box"]')
search_input.send_keys('weight loss')

search_button = chromedriver.find_element_by_xpath('//*[@id="global-search"]/fieldset/button')
search_button.click()



//*[@id="u_jsonp_4_1"]/div/div/div/ul/li[3]/a/div/div[1]

//*[@id="u_jsonp_4_1"]/div/div/div/ul/li[1]/a/div/div[1]

//*[@id="page-container"]/div[2]/div[1]/ul/li[6]/div/div/ul/li[18]/a

#page-container > div.AppContainer > div.AdaptiveFiltersBar > ul > li.AdaptiveFiltersBar-item.AdaptiveFiltersBar-item--more.u-borderUserColor > div > div > ul > li:nth-child(18) > a

