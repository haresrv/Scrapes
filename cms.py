from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


my_url = "https://cms.cb.amrita.edu/login"

uClient = uReq(my_url)
page = uClient.read()
uClient.close()

page_soup = soup(page,'html.parser')

containers = page_soup.findAll("div",{"class":"form-group"})
username = containers[0].findAll("input",{"class":"form-control"})
password = containers[1].findAll("input",{"class":"form-control"})
print(username[0])
print(password[0])


