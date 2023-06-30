import requests
from bs4 import BeautifulSoup

URL = "https://www.drugs.com/strattera.html"  # replace with the URL you want to scrape
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# Uncomment below lines to print the entire HTML of the page
# print(soup)

# **********************************************************
# Uncomment below lines to find the first <h1> tag on the page and print its text
# p_tag = soup.find('h1')
# print(p_tag.get_text())

# **********************************************************
# Uncomment below lines to find all <p> tags on the page and print their text
# p_tags = soup.find_all('p')
# for tag in p_tags:
#     print(tag.get_text())

# **********************************************************
# Uncomment below lines to find all <a> tags on the page and print their href attribute
# for link in soup.find_all('a'):
#     print(link.get('href'))

# **********************************************************
# Uncomment below line to extract all the text from a page
# print(soup.get_text())

# **********************************************************
# Find all <a> tags with http links and print them
for link in soup.find_all('a'):
    theLink = link.get('href')
    http = "http"
    if theLink and theLink.startswith(http):
        print(theLink)
