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
driver.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=&txtLocation=India") 

try:
    driver.find_element(By.XPATH,'//*[@id="closeSpanId"]').click()
except:
    print('close nhi aays')
    pass

input_search = driver.find_element(By.XPATH,'//*[@id="txtKeywords"]')
input_search.send_keys('Machine Learning')
button = driver.find_element(By.XPATH,'//*[@id="quickSearchBean"]/button').click()
soup = BeautifulSoup(driver.page_source,'lxml')
result = soup.find('ul', class_='new-joblist')
result2 = result.find_all('li', class_='clearfix job-bx wht-shd-bx')
    
page_counter = 0
    
    # print(result2)
pages = np.arange(1, 25)

exception = 0

for page in pages:
    if page_counter == 0:
      next_counter = 0 
    else:
      next_counter = 1
        
page_next_counter = np.arange(2,12)
for page_next in page_next_counter:
            for i in result2:
                # TITLE
                title = i.find('a')
                title = title.text
                print(title.encode('utf-8'))
                
                # Description
                description = i.find('label').next_sibling.strip()
                print(description)

                # COMPANY
                text = i.find('h3', class_='joblist-comp-name')
                text = text.text
                initial_company = text.find('(')
                Company = text[:initial_company]
                Company = Company.strip()
                print(Company)

                # Exp
                Mat_icons = i.find_all('i', class_='material-icons')
                # print('THIS IS MATERIAL ICONS:', Mat_icons)
                Exp = Mat_icons[0].next_sibling.text.strip()
                # print(Exp)

                # City
                spans = i.find_all('span')
                City = spans[1].text

                # Date Posted
                Date = i.find('span', class_='sim-posted')
                Date = Date.text.strip()
                print(Date)

                URL = i.find('a').get('href')
                print(URL)

                try:
                    Salary = i.find('i', class_="material-icons rupee").next_sibling
                    print(Salary)
                except Exception as e:
                    print("EXCEPTION OCCURRED AT SALARY")
                    exception = exception + 1
                    Salary = 'Not Mentioned'

