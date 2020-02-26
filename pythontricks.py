# import youtube_dl
import webbrowser
# import sched
# import time
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


pages= 3
ImageURL=[]
FacultyNames=[]
MainRole = []
AdditionalRole=[]

my_url = "https://www.amrita.edu/faculty?field_faculty_department_tid=38&field_faculty_designation_tid=All&field_faculty_campus_tid=53&field_faculty_department_main_tid=101&field_center_name_tid=All&page="
for j in range(pages):
	
	url=my_url+str(j)
	uClient = uReq(url)
	page = uClient.read()
	uClient.close()
	page_soup = soup(page,"html.parser")

	containers = page_soup.findAll("div",{"class":"row row-margin-top"})
	for i in range(len(containers)):
		container = containers[i]

		images = container.findAll("div",{"class":"col-md-3"})
		ImageURL.append((images[0].img["src"]))

		text = container.findAll("div",{"class":"col-md-9"})
		roles =  text[0].strong.div.div
		role = roles.findAll("div",{"class":"views-field views-field-field-faculty-designation"})
		if (len(role)>1):
			MainRole.append((role[0].text))
			AdditionalRole.append((role[1].text))
		else:
			MainRole.append((role[0].text))
			AdditionalRole.append((None))

		FacultyNames.append((text[0].h2.text))

# print(container.div)

# print(AdditionalRole)

# import csv
# with open("Roles.csv", 'w', newline='') as myfile:
#      wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#      wr.writerow(FacultyNames)

import pandas
df = pandas.DataFrame(data={"Name": FacultyNames, "Role": MainRole, "Additional": AdditionalRole})
df.to_csv("./Roles.csv", sep=',',index=False)

# def my_func():
# 	s.enter(5,1,my_func,argument=())
# 	print("HELLO")


# s= sched.scheduler(time.time,time.sleep)	

# s.enter(5,1,my_func,argument=())
# s.run()

# url = "https://intranet.cb.amrita.edu/"
# webbrowser.open_new(url)

"""
links= ["https://www.youtube.com/watch?v=MHlwl6GsT8s"]

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
# ydl.download(links)
with ydl:
	result = ydl.extract_info("https://www.youtube.com/watch?v=MHlwl6GsT8s",
		download=False)

if 'entries' in result:
    # Can be a playlist or a list of videos
    video = result['entries'][0]
else:
    # Just a video
    video = result

print(video)
video_url = video['url']
print(video_url)	

"""

