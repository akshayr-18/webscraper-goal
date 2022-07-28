#First attempt at building a WebScraper- Fake Python Jobs Site
import requests
from bs4 import BeautifulSoup

url="http://realpython.github.io/fake-jobs/"
page=requests.get(url)

soup=BeautifulSoup(page.content, "html.parser")
results=soup.find(id="ResultsContainer")
jobs_all=results.find_all("div",class_="card-content")
jobs=results.find_all("h2",string="Python")
for job in jobs_all:
    tit=job.find("h2",class_="title")
    comp=job.find("h3",class_="company")
    loc=job.find("p",class_="location")
    print(tit.text.strip())
    print(comp.text.strip())
    print(loc.text.strip())
    print()
