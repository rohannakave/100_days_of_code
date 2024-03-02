from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

## Loading URL
response = requests.get(URL)
## Get HTML data of that webpage.
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')
soup.prettify()

## Gather list of movies under class tag in HTML
movie_list = [m_list.get_text() for m_list in soup.find_all(class_="listicleItem_listicle-item__title__BfenH")]
# print(movie_list)

## Write list of movies in new text file
with open("Top 100 movies.txt", "w") as file:
    for i in reversed(movie_list):
        file.write(f"{i}\n")
