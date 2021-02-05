from selenium import webdriver
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time
import math


#input your email and password
email = "XXXXXXXXXXXX"
password = "XXXXXXXXX"

#increase T if the internet connection is slow
T = 1

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

caps = options.to_capabilities()

driver = webdriver.Chrome(desired_capabilities = caps, executable_path='C:\webdrivers\chromedriver.exe') # to open the chromebrowser 

driver.get("https://auth.uber.com/login/?breeze_local_zone=phx5&next_url=https%3A%2F%2Fwww.ubereats.com%2Flogin-redirect%2F%3Fmarketing_vistor_id%3D76123a15-1734-463c-b473-ea4b17fa7a18%26redirect%3D%252Fhk-en&state=tAnl01kOMwf7yqoUM0cF-0ThPm-s9nHgzNMkeOw-r_c%3D")
time.sleep(T)
login_email = driver.find_element_by_id("useridInput")
login_email.send_keys(email)
login_email.send_keys(Keys.RETURN)
time.sleep(T)


login_pass = driver.find_element_by_id("password")
login_pass.send_keys(password)
login_pass.send_keys(Keys.RETURN)
time.sleep(2)

change_add = driver.find_element_by_xpath("//*[name()='svg' and @aria-label='Deliver to']").click()
time.sleep(T)
change_add2 = driver.find_element_by_xpath("//a[contains(text(),'Change')]").click()
time.sleep(T)
input_add = driver.find_element_by_id("location-typeahead-location-manager-input")
input_add.send_keys("3/F, Citicorp Centre, 18 Whitfield Rd, Causeway Bay")
input_add.send_keys(Keys.RETURN)
time.sleep(T)

select_add = driver.find_element_by_id("location-typeahead-location-manager-item-0").click()
time.sleep(1.5)
save_add = driver.find_element_by_xpath('//button[@data-test="save-address"]').click()
time.sleep(5)

def scrape_url():
    show_button = True
    while show_button == True:
        try:
            show_more = driver.find_element_by_xpath('//button[contains(text(),"Show more")]').click()
            time.sleep(4)
        except:
            show_button = False
    grablinks = driver.find_elements_by_xpath('//*[@id="main-content"]/div/div[3]/div[2]/div/div[2]//a[@aria-hidden="true" and starts-with(@href, "/hk-en/hong-kong/food-delivery/")]')

    all_url = []
    for link in grablinks:
        all_url.append(link.get_attribute("href"))

    print(grablinks)
    print(all_url)
    with open("./all_url.txt",'w') as f:
        for i in all_url:
            f.write(i + "\n")

scrape_url()
print("scraped?")

#change the save directory as required
with open("./all_url.txt",'r') as f:
    text = f.readlines()
    text = [i.strip() for i in text]

test_url = text
x = len(test_url)
ubereat_page = []

for i in range(x):
    driver.get(test_url[i])
    time.sleep(0.3)
    try:
        name = driver.find_element_by_xpath('//*[@id="main-content"]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/h1').text
    except:
        name = None

    try:
        address = driver.find_element_by_xpath('//*[@id="main-content"]/div[3]/div[1]/div[1]/p').text
    except:
        address = None

    try:
        review_count = driver.find_element_by_xpath('//*[@id="main-content"]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[5]').text
    except:
        review_count = None

    try:
        delivery = driver.find_element_by_xpath('//*[@id="main-content"]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]').text
    except:
        delivery = None

    try:
        menu = driver.find_elements_by_xpath('//h4/div')
        menu = [i.text for i in menu]
    except:
        menu = None

    try:
        price = driver.find_elements_by_xpath('//h4/div/../..//following-sibling::div//following-sibling::div/div')
        price = [i.text for i in price]
        if len(price) == 0:
            price = driver.find_elements_by_xpath('//h4/div/../..//following-sibling::div/div')
            price = [i.text for i in price]
    except:
        price = None

    try:
        rating = driver.find_element_by_xpath('//*[@id="main-content"]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[3]').text
    except:
        rating = None

    try:
        food_type = driver.find_element_by_xpath('//*[@id="main-content"]/div[3]/div[1]/div[1]/div').text
    except:
        food_type = None

    ubereat_page.append({"Name" : name,
        "Delivery" : delivery,
        "Address" : address,
        "Food_type" : food_type,
        "Rating" : rating,
        "Reviews": review_count,
        "Menu" : menu,
        "Menu_Prices" : price,
        })
    print(i,x)
df = pd.DataFrame(ubereat_page)
df.to_csv("ubereats.csv", mode='w', header=False, index=False)

