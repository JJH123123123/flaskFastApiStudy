import requests
from bs4 import BeautifulSoup as BS

url = "https://mobileadmin.cnu.ac.kr/food/index.jsp"
response = requests.get(url)

if response.status_code == 200:
    soup = BS(response.text, "html.parser")
    print(soup.prettify())
else:
    print(response.status_code)
