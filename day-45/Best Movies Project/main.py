from bs4 import BeautifulSoup
import requests


# Request to the site
response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire_web = response.text

# Initializing BeautifulSoup
soup = BeautifulSoup(empire_web, "html.parser")

# Finding titles of movies
movies = soup.find_all("h3", class_= "title")
# Getting name of the movie
movies_name = [name.get_text() for name in movies]
# Reversing order of the list
movies_name.reverse()


# Opening movies.txt
with open("movies.txt", "w", encoding="utf-8") as file:
    # Writing names of the movies to movies.txt
    for line in movies_name:
        file.writelines(f"{line}\n")


