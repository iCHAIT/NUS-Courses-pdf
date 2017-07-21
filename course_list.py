import requests

from bs4 import BeautifulSoup

# Disables all the 'Unverified HTTPS request is being made' warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# url of page containing list of all courses available this sem
root_url = "http://mysoc.nus.edu.sg/~postgd/LecturePreview.html"


# Obtained by logging in to the site
# refreshing the page
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

courses = [td.find('a') for td in soup.findAll('td', {"width": 264})]
# Todo: Using the above also fetch all slides - td tag width 140

course_data = {}
ivle_links = []

for course in courses:
    if course not in (None, ''):
        # contains course name and IVLE linkc- maybe useful later
        course_data.update({course.text: course['href']})
        # store all intermediate IVLE links of all modules
        ivle_links.append(course['href'])


# store all intermediate IVLE links to a file
with open("ivle_links.txt", "w") as f:
    for link in ivle_links:
        f.write(link + '\n')
