# imports the selenium package
from selenium import webdriver

# finds and uses a program called chromedriver for automation purposes
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# opens up the youtube link on the chromedriver
driver.get("https://www.youtube.com/watch?v=HtUH9z_Oey8")

# finds the youtube play button by it's xpath
playButton = driver.find_element_by_xpath("//*[@id='movie_player']/div[5]/button")

# presses the play button
playButton.click()

# stops the program from closing itself
input('Press ENTER to exit')