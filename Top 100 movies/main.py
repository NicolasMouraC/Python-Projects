import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
html = response.text

soup = BeautifulSoup(html, "lxml")
elements = soup.find_all(name="h3", class_="title")

movies = []
for element in elements:
    movies.append(element.get_text())
movies_list = list(reversed(movies))

with open("movies to watch.txt", mode="w") as file:
    for line in movies_list:
        file.write(f"{line}\n")
