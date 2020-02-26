from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


my_url = "https://www.amrita.edu/program/btech-computer-science-and-engineering"

uClient = uReq(my_url)
page = uClient.read()
uClient.close()

semesters = []
table_headers=[]

page_soup = soup(page,'html.parser')

containers = page_soup.findAll("div",{"class":"col-xs-12 co-sm-12 col-md-6"})
for kj in range(2,len(containers)):
    container = containers[kj]
    table_cols = []
    rows = container.findAll("table",{"class":"table table-bordered table-striped"})
    sem = rows[0]
    semesters.append(rows[0].findAll("td",{'class':'text-center'}))

    row_sub = rows[0].findAll("tr")
    for j in range(2,len(row_sub)-2):
        row_sub2 = row_sub[j].findAll("td")
        for i in range(len(rows[0].findAll("em"))):
            if len(table_headers)!=8:
                table_headers.append(rows[0].findAll("em")[i].text)
        # print(row_sub2)
        r=[]
        for i in ((row_sub2)):
            if i.text:
                r.append(i.text)
        if len(r)==6:
            r.insert(3,'-')
            r.insert(4, '-')
        table_cols.append(r)

        # print(r)
    # print(table_cols)



    import pandas
    #
    df= pandas.DataFrame(columns=table_headers)
    for i in table_cols:
        df.loc[len(df)] = i

    print(df)

    df.to_csv("./Course-Sem"+str(kj-1)+".csv", sep=',',index=False)
