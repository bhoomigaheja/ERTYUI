import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import datetime
import pandas as pd
import numpy as np
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("ttps://www.foundit.in/") 

try:
    driver.find_element(By.XPATH,'//*[@id="closeSpanId"]').click()
except:
    print('close nhi aays')
    pass

input_search = driver.find_element(By.CLASS_NAME,'input-wrapper')
input_search.send_keys('Machine Learning')
button = driver.find_element(By.XPATH,'//*[@id="search-block-expend"]/div[6]/input').click()



