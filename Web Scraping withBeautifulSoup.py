import requests
from bs4 import BeautifulSoup


url = "https://www.google.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


#Extract and print all the links on the page
for link in soup.find_all("a"):
    print(link.get("href"))