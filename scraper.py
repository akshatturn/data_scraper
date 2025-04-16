import requests
import pandas as pd
import os
import json
from selenium import webdriver

def get_session_cookies():
    currentdir = os.path.dirname(__file__)
    driver = webdriver.Chrome(os.path.join(currentdir, "chromedriver"))
    driver.get("https://www.nsedata.com")
    cookies = driver.get_cookies()
    cookie_dict = {}
    with open('cookies.json', 'w') as line:
        for cookie in cookies:
            cookie_dict[cookie["name"]] = cookie["value"]
        line.write(json.dumps(cookie_dict))
    print(cookie_dict)
    driver.quit()
    return cookie_dict

url = "https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O"
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate"
}

cookie_dict = get_session_cookies()

session = requests.session()

for cookie in cookie_dict:
    session.cookies.set(cookie, cookie_dict[cookie])

r = session.get(url, headers=headers)

print(r.json())