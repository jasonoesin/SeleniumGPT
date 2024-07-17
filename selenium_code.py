from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get('https://danaindo.bantuan-kendala.biz.id/')

driver.quit()
