import requests
import time
from bs4 import BeautifulSoup

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


cookies = {
    'ASP.NET_SessionId': 'u40bhuancbunufh4lh1i3dwf',
    'UserID': 'e0210471',
    't': '636363666858059252',
    'TreeState': '',
    'tp': '1758939251',
    'ivle12': '7DBA69FBBD9B8FAB1F37802EFF78D2F56634B144978F8D9543D6A8C98B31105C3DFF20F36E10B17B0565EBC0CFD196F2CCBA63B1D614C3AECE35FAD7901C84E6EE3B9B626BED0D452621F614CC415BE34437B8C08FBA9A033C29A6899586F7C183486D489ADC7B6CC33172B8449360F30AF6507C50F9F69FA60F346B159C53E3AD7C6B9247C5E3CD48547F13988D2E86164980F217076C31602A066588A4DADF53FC3306A37B2B864EBE045457E1FC7D',
}


### Uncomment the below code to produce html on old IVLE
# Extract final urls OLD
# with open("final_links_old.txt", "r") as f:
#     urls = f.read().splitlines()


# for url in urls:
#     resp = requests.get(url, cookies=cookies)
#     html = resp.content
#     soup = BeautifulSoup(html, 'html.parser')

#     # Get the parent level tag and corresponding data - for old version of IVLE
#     div = soup.find("div", {"id": "ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_UP"})

#     data = str(div)

#     # Dump the data in a master html file
#     with open("NUS-SOC-Courses-v0.html", "a") as f:
#         f.write(data)

#     time.sleep(10)


# Extract final urls NEW
with open("final_links_new.txt", "r") as f:
    urls = f.read().splitlines()


for url in urls:
    resp = requests.get(url, cookies=cookies)
    html = resp.content
    soup = BeautifulSoup(html, 'html.parser')

    # Get the parent level tag and corresponding data - for new version of IVLE
    div = soup.find("div", {"class": "panel-body"})


    # Convert to string
    data = str(div)
    # print(data)


    ##### PARSE Lecturer info
    url_lect = url.replace("default", "list_lecturers")

    resp = requests.get(url_lect, cookies=cookies)
    html = resp.content
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find("div", {"class": "panel-body"})

    data = data + "<h2>Faculty</h2>" + str(div)



    ### Todo: Incorporate Reading tabs on IVLE



    #### Parse Weblinks
    url_web = url.replace("default", "list_weblinks")

    resp = requests.get(url_web, cookies=cookies)
    html = resp.content
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find("div", {"class": "well"})
    table = div.find("table", {"class": "table table-hover table-striped"})
    rows = table.findAll('tr')
    tds = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]

    weblinks = ""

    for lists in tds:
        if len(lists) != 0:
            for item in lists:
                for i in item:
                    if i != "\n":
                        weblinks = weblinks + "<br/><br/>" + i.strip()

    data = data + "<h2>Weblinks</h2>" + weblinks



    #### Parse TimeTable
    url_time = url.replace("default", "list_timetable")

    resp = requests.get(url_time, cookies=cookies)
    html = resp.content
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find("div", {"class": "panel-body"})

    data = data + "<h2>TimeTable</h2>" + str(div)



    # Dump the data in a master html file
    with open("NUS-SOC-Courses-v1.html", "a") as f:
        f.write(data)

    time.sleep(5)
