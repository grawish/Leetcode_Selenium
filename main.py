import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://leetcode.com/")

while "1" != input("press 1 when signed in: "):
    pass

print("accessing Questions")
driver.get("https://leetcode.com/problemset/all/?status=Solved")
sleep(3)
links = driver.find_elements_by_tag_name("a")
for link in links:
    pass

driver.close()
