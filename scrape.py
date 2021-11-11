import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup

filename = "PrivateEducation.csv" #Filename, csv filetype
f = open(filename, 'w') #open file and write

headers = "Company Name,Telephone,Fax,Email,Web\n" #adding of headers
f.write(headers) #writing headers in excel

for i in range(1,22): #iterate through all 21 pages in the website

    my_url ="https://privateeducation.sg/search/Alphabetical?Viewcompany_page=" + str(i) #increase the page number by 1 every iteration to go through all pages of website
    uClient = urlopen(my_url) #opening connection, grabbing page
    page_html = uClient.read() #raw html, offload content into variable
    uClient.close() #close

    page_soup = BeautifulSoup(page_html, "html.parser") #HTML parsing
    containers = page_soup.findAll("div", {"class": "lst-alpha"}) #grabbing all divs with class "lst-alpha", contains wanted information

    for container in containers: #looping through each container
        try:
            name = container.a.text.title() #grab company name, which is under a tag
            print(name)
        except:
            name = "-" #print "-" if unavailable
            print(name)

        try:
            tel = container.div.find("p", {"class": "tel"}) #find all class "tel" for the telephone number
            tel = tel.text #grab text only
            tel = tel[8:] #exclude "tel:" and spaces
            print(tel)
        except:
            tel = "-" #print "-" if unavailable
            print(tel)

        try:
            fax = container.div.find("p", {"class": "fax"}) #find all class "fax" for the fax number
            fax = fax.text #grab text only
            fax = fax[8:] #exclude "fax:" and spaces 
            print(fax)
        except:
            fax = "-" #print "-" if unavailable
            print(fax)

        try:
            email = container.div.find("p", {"class": "email"}) #find all class "email" for the email
            email = email.text #grab text only
            email = email[10:] #exclude "email:" and spaces 
            print(email)
        except:
            email = "-" #print "-" if unavailable
            print(email)
        
        try:
            web = container.div.find("p", {"class": "web"}) #find all class "web" for the website link
            web = "web: " + str(web.a.text) #redundant actually
            web = web[5:] #exclude "web:" and spaces
            print(web)
        except:
            web = "-" #print "-" if unavailable
            print(web)

        print() #print blank line

        f.write(name + "," + tel + "," + fax + "," + email + "," + web +"\n") #Adds all information into excel sheet
f.close() #close file