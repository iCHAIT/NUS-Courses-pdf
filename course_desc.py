import requests
from bs4 import BeautifulSoup


# Disables all the 'Unverified HTTPS request is being made' warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# url of intermediate ivle page

cookies = {
    'ASP.NET_SessionId': 'u40bhuancbunufh4lh1i3dwf',
    'UserID': 'e0210471',
    't': '636362806904372117',
    'TreeState': '',
    'ivle12': '3AAE24AE25C079DA1A676189547FCC2A0FD280F6586ED7984A4C4AD260F36D24BD6998762CE3D4CD58736F814B5FF26BC56EF3526F68851E15885FC6EFA5AB244F24965532C0BDFADC81907076008D9350F76A2159BC5B84D9E04F04C12888023CEE42E98F698C9A4636DE83D6AD227C12282F4213D5B3FD22146EC5E3AF61995E404CA23D06464CFB8B71679C31DD986544A8D4777A74159C44ADDAE48D4B497B3ED264960AB6B130B844C07BA1174D',
}


# Read all intermediate IVLE links
with open("ivle_links.txt", "r") as f:
    urls = f.read().splitlines()


for url in urls:
    resp = requests.get(url, cookies=cookies, verify=False)
    html = resp.content
    soup = BeautifulSoup(html, 'html.parser')
    tr = soup.find('tr', {'class': "dataGridCtrl-Item"})
    if tr not in (None, ''):
        td = tr.findAll('td')[1]
    a = td.find('a')
    val = str(a)

    # Prepare ultimate url that contains all relevant info on IVLE
    relevant_url = ""

    # Process string to extract relevant text for module
    for i, j in enumerate(val.split('/')):
        if i == 1:
            relevant_url = relevant_url + "/" + j
        elif i == 2:
            relevant_url = relevant_url + "/" + j
        elif i == 3:
            j = j.split(",")
            relevant_url = relevant_url + "/" + j[0]

    url = relevant_url[:-1]

    # All modules have below format on IVLE
    final_url = "https://ivle.nus.edu.sg" + url

    # Store the final urls to a file
    with open("final_links.txt", "a") as f:
        f.write(final_url + "\n")
