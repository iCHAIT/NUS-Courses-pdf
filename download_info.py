import requests
import time
from bs4 import BeautifulSoup

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


cookies = {
    'ASP.NET_SessionId': 'u40bhuancbunufh4lh1i3dwf',
    'UserID': 'e0210471',
    't': '636362806904372117',
    'TreeState': '',
    'ivle12': '43C5F27FBACEA6E42CCB0FC9B03D6C5908DADFA3BFD58FB4BAE021EDE05E005270EAF11251166AF7FCC2DD06367F656093340EBA71325DBD30E524C2A919AC7AEF89DEF6D943387F9B84A19B93D5B5EA5D0C10947B184F989FA192481279F43955DB35F53FEA985474632DD9D0C3099FD60B09A0DFCA7566F8D5190EAF5F41910B281CCCF1F80E253640312510E26024972A849A2BE8108830769F86259EF6CD2D1824DD8AB6EF48B1E2C340C436F60B',
}


# Extract final urls
with open("final_links.txt", "r") as f:
    urls = f.read().splitlines()


for url in urls:
    resp = requests.get(url, cookies=cookies)
    html = resp.content
    soup = BeautifulSoup(html, 'html.parser')

    # Get the parent level tag and corresponding data
    div = soup.find("div", {"id": "ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_UP"})
    # Convert to string
    data = str(div)

    # Dump the data in a master html file
    with open("first.html", "a") as f:
        f.write(data)

    time.sleep(10)

    # Finally use pandoc to port html to pdf
    # Yayy||
