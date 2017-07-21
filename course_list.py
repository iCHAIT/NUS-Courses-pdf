import requests
import logging

from bs4 import BeautifulSoup

# Disables all the 'Unverified HTTPS request is being made' warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', filename='course_list.log',
                    level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S')


# url of page containing list of all courses available this sem
root_url = "http://mysoc.nus.edu.sg/~postgd/LecturePreview.html"



# Obtained by logging in to the site
# and refreshing the page
# Then exporting the "Request as Curl" (in chrome)
# and then using https://curl.trillworks.com/
# to convert the curl command to python requests code
cookies = {
    'AuthDBICookieHandler_NUSNET_mysoc': 'd749de343aaa38c413c805845dbd3596',
    'NSC_nztpd-evbm-ofx': 'ffffffffc3a00a0d45525d5f4f58455e445a4a42378c',
}


resp = requests.get(root_url, cookies=cookies, verify=False)

html = resp.content


soup = BeautifulSoup(html, 'html.parser')

# parse_html = BeautifulSoup(html)
# print(parse_html)
# results = soup.findAll("td", {"width" : 264})

results = [td.find('a') for td in soup.findAll('td', {"width": 264})]

course_data = {}

for result in results:
    if result not in (None, ''):
        course_data.update({result.text: result['href']})



