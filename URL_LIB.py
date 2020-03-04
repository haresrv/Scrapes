from urllib.request import urlopen as uReq
from urllib.parse import urlparse,urlunparse,quote,urlsplit,urlencode
from urllib import robotparser as rb

my_url = "https://cms.cb.amrita.edu/login"

uClient = uReq(my_url)
page = uClient.read()
uClient.close()

parser = urlparse(my_url)

print("URLPARSE-->",parser)
print("URLUNPARSE-->",urlunparse(parser))
print("QUOTE-->",quote(my_url))
print("URLSPLIT-->",urlsplit(my_url))


qry = {"name":"HareSRV", "RollNo.":17119}
print("URL ENCODE-->",quote(urlencode(qry)))

try:
    x = uReq('https://www.googdjdble.com')
    print(x.read())

# Catching the exception generated
except Exception as e:
    print(str(e))

try:
    x = uReq('https://www.google.com/search?q=test')
    print(x.read())

# Catching the exception generated
except Exception as e:
    print(str(e))

bot = rb.RobotFileParser()

x= bot.set_url('https://intranet.cb.amrita.edu/robots.txt')
print(x)

y=bot.read()
print(y)

z = bot.can_fetch('*', 'https://intranet.cb.amrita.edu')
print(z)

# but can not crawl the disallowed url
w = bot.can_fetch('*', 'https://intranet.cb.amrita.edu/admin/')
print(w)