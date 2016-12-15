http://download2.tvshows4mobile.com/Scorpion/Season%2001/Scorpion%20-%20S01E01%20(O2TvSeries.Com).mp4
http://download1.tvshows4mobile.com/Scorpion/Season%2001/Scorpion%20-%20S01E02%20(O2TvSeries.Com).mp4
http://download1.tvshows4mobile.com/Scorpion/Season%2001/Scorpion%20-%20S01E03%20(O2TvSeries.Com).mp4
http://download1.tvshows4mobile.com/Scorpion/Season%2001/Scorpion%20-%20S01E04%20(O2TvSeries.Com).mp4

http://download2.tvshows4mobile.com/Limitless/Season%2001/Limitless%20-%20S01E20%20(TvShows4Mobile.Com).mp4

driver.execute_script("window.history.go(-1)")

url = chromedriver.current_url

  episode_num1 = int(episode_list[3])
        episode_num2 = int(episode_list[1])

        episode_list_string = cdriver.find_element_by_class_name('page_desc')
        episode_list_result = episode_list_string.get_attribute("textContent")
        episode_list_var = str(episode_list_result)
        episode_list = episode_list_var.split()
        episode_num1 = int(episode_list[1])
        episode_num2 = int(episode_list[3])