from Gcal import GCalCSV

import requests
import datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def convertDay(month, day):
    m = int(month)
    d = int(day)
    p_y = datetime.datetime.now().year
    if ( (datetime.datetime(p_y, m, d) - datetime.datetime.now()).days > 0):
        return month+"/"+day+"/"+str(p_y)
    else:
        return month+"/"+day+"/"+str(p_y+1)

def convertTime(time_index):
    time_list = [
        ["9:20", "10:50"],
        ["11:00", "12:30"],
        ["13:30", "15:00"],
        ["15:10", "16:40"],
        ["16:50", "18:20"],
        ["18:30", "20:00"]
    ]
    return time_list[int(time_index)-1]    

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

csv = GCalCSV({
    "Subject":True,
    "Start Date":True,
    "Start Time":True,
    "End Date":True,
    "End Time":True,
    "Description":True,
    "Location":True
})

for names in name_list:
    c_list = names.find_all("td")
    if c_list:
        link = c_list[0].a.get("href")
        name = c_list[0].string

        link_over = session.get(link)
        base = BeautifulSoup(link_over.text, "html.parser")
        each_day = base.find_all("table", {"class":"tbl01 mB20"})
        each_topic = ""
        if "charges" in link:
            each_topic = each_day[3].find_all("tr")
            each_day = each_day[4].find_all("tr")
        else:
            each_topic = each_day[4].find_all("tr")
            each_day = each_day[5].find_all("tr")
            
        if len(each_day) > 3:
            for day in each_day[1:]:
                tds = day.find_all("td")
                index = tds[0].string
                topics = each_topic[int(index)].find_all("td")

                date_base = tds[1].string
                theme = topics[2].string
                time_index = tds[2].string
                place = tds[3].string
                date_month = date_base.split("/")[0]
                date_day = date_base.split("/")[1] 

                date = convertDay(date_month, date_day)
                time = convertTime(time_index)
                csv_elem = {}
                csv_elem["Subject"] = name
                csv_elem["Start Date"] = date
                csv_elem["Start Time"] = time[0]
                csv_elem["End Date"] = date
                csv_elem["End Time"] = time[1]
                csv_elem["Description"] = theme
                csv_elem["Location"] = place
                csv.add(csv_elem)

csv.outputCSV()




        
        