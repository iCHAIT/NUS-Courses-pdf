import requests
from bs4 import BeautifulSoup


# Disables all the 'Unverified HTTPS request is being made' warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# url of intermediate ivle page

cookies = {
    'ASP.NET_SessionId': 'u40bhuancbunufh4lh1i3dwf',
    'ivle12': 'F7144B1AF5BF6307186A7A46FACC1CB5CF3AAC63BBD63CD512071BE4EBCE8DB9E8FFA23B2A6212B2FA60E5AD2D6FC04ACF907CD569E700A4CA36351BA7F03A6B015CD030361F0125C19B2B8F1FC2F56946EBDB397B39BA10D16B2C7EE10BA20531E2A3AA3E50A6A9D6843C32ADF1A88089B4CA7D91A7068CDB77DCBCD1773D3AC49BD84D27AEFF43990E4D87B44CDCFA8D64388493C571106EC7A6957DB459E330E6C8C9D7455ABE1C515795E59D1129',
    'UserID': 'e0210471',
    't': '636363666858059252',
    'TreeState': '',
    'tp': '1758939251',
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
    else:
        continue

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
    final_url_old = "https://ivle.nus.edu.sg" + url
    final_url_new = "https://ivle.nus.edu.sg/V1" + url

    # Store the final urls to a file
    with open("final_links_old.txt", "a") as f:
        f.write(final_url_old + "\n")

    # Store the final urls to a file
    with open("final_links_new.txt", "a") as f:
        f.write(final_url_new + "\n")
