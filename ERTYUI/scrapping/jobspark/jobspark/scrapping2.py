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

dff = pd.DataFrame(columns=['Job Title','Description', 'Experience Reqd', 'Company', 'City', 'Salary Range', 'Date Posted', 'Rating', 'Site', 'URL'])
driver = webdriver.Chrome()
driver.get("https://www.naukri.com/") 

input_search = driver.find_element(By.XPATH,'//*[@id="root"]/div[7]/div/div/div[1]/div/div/div[1]/div[1]/div/input')
input_search.send_keys('python')
button = driver.find_element(By.XPATH,'//*[@id="root"]/div[7]/div/div/div[6]').click()

# Wait for the job postings to load
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "styles_jlc__main__VdwtF")))

# Retrieve all the job posting elements
posting_elements = driver.find_elements(By.XPATH, "//*[@id='listContainer']/div[2]/div[contains(@class,'styles_jlc__main__VdwtF')]")
print(len(posting_elements))
for job_posting in posting_elements:
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "srp-jobtuple-wrapper")))
    elements = driver.find_elements(By.XPATH, "//*[@id='listContainer']/div[2]/div/div[1][contains(@class,'srp-jobtuple-wrapper')]")
    print(len(elements))
    for job_posting in posting_elements:
       wait = WebDriverWait(driver, 30)
       elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='listContainer']/div[2]/div/div[1]/div[contains(@class,'cust-job-tuple layout-wrapper lay-2 sjw__tuple')]")))
       #elemts = driver.find_elements(By.XPATH, "//*[@id='listContainer']/div[2]/div/div[1]/div[contains(@class,'cust-job-tuple layout-wrapper lay-2 sjw__tuple')]")
       #print(elemts)
       soup = BeautifulSoup(driver.page_source,'lxml')
       post = soup.find_all('div','cust-job-tuple layout-wrapper lay-2 sjw__tuple')
       print(len(post))
     
       titles = []
       exps = []
       salarys= []
       locs = []
       descs = []
       skillss = []
       days = []
       companys = []

for i in post:
    title = i.find('a').text
    titles.append(title)
    company = i.find('span', class_='comp-dtls-wrap').text
    companys.append(companys)
    exp = i.find('span', class_='exp-wrap').text
    exps.append(exp)
    salary = i.find('span', class_='sal-wrap ver-line').text
    salarys.append(salary)
    loc = i.find('span', class_='loc-wrap ver-line').text
    locs.append(loc)
    desc = i.find('span', class_='job-desc ni-job-tuple-icon ni-job-tuple-icon-srp-description')
    desc_text = desc.text if desc else "Description not found"
    descs.append(desc_text)
    skills = i.find('ul', class_='tags-gt').text
    skillss.append(skills)
    day = i.find('span', class_='job-post-day').text
    days.append(day)
print(titles[0])

print(salarys[0])
print(locs[0])
print(descs[0])
print(exps[0])
print(companys[0])     

    