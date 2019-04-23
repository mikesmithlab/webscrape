import requests
from bs4 import BeautifulSoup

html = requests.get("http://localhost:8082/planets.html").text
soup = BeautifulSoup(html, "lxml")

list_all = soup.body.div.table.children

table = soup.find("table")

#print([str(t2)[:50] for t2 in table.findAll("td")])

#print(table.find("tr", {"name": "Mars"}))



items = dict()

planets = table.findAll("tr", {"class": "planet"})
for planet in planets:
    data = planet.findAll("td")
    items[data[1].text.strip()] = data[2].text.strip()

print(items)
