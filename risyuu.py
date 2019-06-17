import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


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

name_list = soup.find_all("tr")
for names in name_list:
    print("----------------")
    c_list = names.find_all("td")
    if c_list:
        link = c_list[0].a.get("href")
        name = c_list[0].string
        season = c_list[1].string
        teacher = c_list[2].string
        d_range = c_list[3].string

        print(link)
        print(name)
        print(season)
        print(teacher)
        print(d_range)