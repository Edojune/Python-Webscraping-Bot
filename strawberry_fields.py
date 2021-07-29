from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com/watch?v=HtUH9z_Oey8")

playButton = driver.find_element_by_xpath("//*[@id='movie_player']/div[5]/button")

playButton.click()

input('Press ENTER to exit')