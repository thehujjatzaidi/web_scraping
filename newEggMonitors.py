#import the libraries
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#initialize the url
my_url='https://www.newegg.com/global/in-en/p/pl?Submit=StoreIM&Depa=133&Category=19'

#initate the connection
uClient=uReq(my_url)
page_html=uClient.read()

#parse the file 
page_soup=soup(page_html,"html.parser")

#initilize the variables for parsing
containers=page_soup.findAll("div",{"class":"item-info"})



#initialiuze the file name
filename = "newEggMonitors.csv"

#open the file
f = open(filename,"w")
headers = "Brand, Model, Price\n"

#write headers in the file
f.write(headers)

#loop over the containers containing the monitors
for container in containers:
	monitor=container.findAll("a",{"class":"item-title"})
	for tag in container.findAll("a",{"class":"item-brand"}):
		print(tag.img["alt"])
	for a in monitor:
		print(a.text)
	for price_text in container.findAll("li",{"class":"price-current"}):
		print(tag.img["alt"]+ "," + a.text.replace(",","") + "," + price_text.text.replace("₹","Rs").replace(",",""))
		f.write( tag.img["alt"]+ "," + a.text.replace(",","") + "," + price_text.text.replace(",","").replace("₹","Rs") + "\n" )

f.close()
