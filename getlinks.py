
import requests
from bs4 import BeautifulSoup

inp = input('insert url: ')

grab = requests.get(inp)
soup = BeautifulSoup(grab.text, 'html.parser')

# opening a file in write mode
f = open("links.txt", "w")
# traverse paragraphs from soup
for link in soup.find_all("a"):
    data = link.get('href')
    data = str(data)
    f.write(data)
    f.write("\n")

f.close()
