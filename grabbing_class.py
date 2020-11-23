
##Syntax to pass to the .select() method             Match Results

##soup.select('div')                                 All elements with the <div> tag

##soup.select('#some_id')                             The HTML element containing the id attribute of some_id

#soup.select('.notice')                              All the HTML elements with the CSS class named notice

##soup.select('div span')                         Any elements named <span> that are within an element named <div>

##soup.select('div > span')                 Any elements named <span> that are directly within an element named <div>, with no other element in between


import requests
import bs4

res = requests.get("https://www.netflix.com/browse")
soup = bs4.BeautifulSoup(res.text,"lxml")

first_item = soup.select('a')


for item in soup.select('.href'):
    print(item.text)
