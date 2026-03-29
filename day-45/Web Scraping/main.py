from bs4 import BeautifulSoup
import requests


# Request to the site
response = requests.get(url="https://news.ycombinator.com/news")
yc_web = response.text

# Lists
titles_list = []
links_list = []
upovotes_list = []

# Initializing Beautiful soup
soup = BeautifulSoup(yc_web, "html.parser")


# Scraping titles the of articles
span = soup.find_all(class_= "titleline")
for text in span:
    title = text.get_text(strip=True)
    # Getting rid of (...com)
    title = title.split("(")[0]
    titles_list.append(title)

# Scraping link the of articles
for anchor in span:
    anchor = anchor.find_all("a")
    link = anchor[0]["href"]
    # Checking if it is a link
    if link.startswith("https:") or link.startswith("http:"):
        links_list.append(link)
    else:
        links_list.append(link)

# Scraping upvotes the of articles
upvotes = soup.find_all(class_= "score")
for upvote in upvotes:
    # Split to get rid of "points" to have only int
    upvote = int(upvote.get_text().split(" ")[0])
    upovotes_list.append(upvote)

# Check which articles has the most upvotes
highest_num = max(upovotes_list)
position = upovotes_list.index(highest_num)

print(titles_list[position])
print(links_list[position])







