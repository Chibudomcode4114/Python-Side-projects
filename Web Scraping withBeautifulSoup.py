# import requests
# from bs4 import BeautifulSoup


# url = "https://www.google.com"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")


# #Extract and print all the links on the page
# for link in soup.find_all("a"):
#     print(link.get("href"))

import requests
from bs4 import BeautifulSoup

def get_all_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract and print all the links on the page
        for link in soup.find_all("a"):
            print(link.get("href"))

    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")

# Example usage
url_to_scrape = "https://www.google.com"
get_all_links(url_to_scrape)
