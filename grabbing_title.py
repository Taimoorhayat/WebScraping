import requests
import bs4



 ###  Showing the html of requested page ###
 getlink.text
 
 
get_link = requests.get("https://www.google.com/")

 ###  Showing the html of requested page ###
 getlink.text

Title = bs4.BeautifulSoup(get_link.text,"lxml")
exact_title = Title.select("title")[0].getText()

print(exact_title)
