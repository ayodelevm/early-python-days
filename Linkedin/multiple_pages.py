from selenium import webdriver
import time

cdriver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver.exe")

url = 'http://tvshows4mobile.com/Scorpion'

cdriver.get(url)

old_new = cdriver.find_element_by_xpath('/html/body/div/div[9]/a[1]')
old_new.click()

all_season = cdriver.find_elements_by_partial_link_text('Season 0')

for a in all_season:
    a.click()
    time.sleep(3)
    
    old_new = cdriver.find_element_by_xpath('/html/body/div/div[9]/a[1]')
    old_new.click()
    
    episode_result = cdriver.find_element_by_xpath('/html/body/div/div[7]/div[4]/div[2]/div[2]')
    episode_result_num = int(episode_result.get_attribute("textContent"))
    page_num =(int(episode_result_num/10)) + 1

    url = cdriver.current_url

    for page in range(1, page_num+1):
        new_url = url + 'page{0}'.format(page)
        
        
        
        
        
        for episode in range(1, 11):
            all_episode = cdriver.find_element_by_xpath('/html/body/div/div[12]/div[{0}]/a'.format(episode))
            all_episode.click()
            time.sleep(3)

            mp4_link = cdriver.find_element_by_partial_link_text('.mp4')
            mp4_link.click()

            time.sleep(5)

            cdriver.back()

        cdriver.get(new_url)
    
else:
    time.sleep(1000)
    cdriver.quit()




  
