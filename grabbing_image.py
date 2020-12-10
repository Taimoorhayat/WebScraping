import requests
import bs4
result = requests.get("https://en.wikipedia.org/wiki/Shrek")
soup = bs4.BeautifulSoup(result.text,"lxml")
soup.select('.thumbimage')
comp = soup.select('.thumbimage')[0]
getreq = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Mike_Myers_David_Shankbone_2010_NYC.jpg/170px-Mike_Myers_David_Shankbone_2010_NYC.jpg')
getreq.content
