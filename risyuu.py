import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


account_data = open("account.txt", "r")
lines = account_data.readlines()
USER = lines[0].rstrip('\n')
PASS = lines[1]
session = requests.session()

login_info = {
    "data[User][account]":USER,
    "data[User][password]":PASS,
}

url_login = "https://subjregist.naist.jp/users/login"
res = session.post(url_login, data=login_info)
res.raise_for_status()
soup = BeautifulSoup(res.text,"html.parser")
s = session.get("https://subjregist.naist.jp/schedules/preview_monthly")
#s = soup.find_all("a", {"class":"menu_disp"})[3]
print(s.text)
        
        