from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

s = Service(executable_path='chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://test.beeznests.com/')
driver.find_element(By.XPATH, "/html/body/div/div[9]/div[1]/div[3]/a[4]").click()
driver.implicitly_wait(5)
sleep(5)