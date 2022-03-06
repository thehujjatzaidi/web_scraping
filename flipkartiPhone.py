#import the libraries
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#initialize the url
my_url='https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

#initate the connection
uClient=uReq(my_url)
page_html=uClient.read()

#parse the file 
page_soup=soup(page_html,"html.parser")

#initilize the variables for parsing
containers=page_soup.findAll("div",{"class":"_3O0U0u"})



#initialiuze the file name
filename = "flipkartiPhone.csv"

#open the file
f = open(filename,"w")
headers = "Model, Price, Rating\n"

#write headers in the file
f.write(headers)

#loop over the containers containing the iphones
for container in containers:
	model = container.div.img["alt"]

	price_tag=container.findAll("div",{"class":"_1vC4OE _2rQ-NK"})
	price=price_tag[0].text

	product_rating=container.findAll("div",{"class":"hGSR34"})
	rating=product_rating[0].text

	print(model.replace(",","|")+ price.replace(",","").replace("₹","Rs") + rating )
	f.write(model.replace(",","|") + "," + price.replace(",","").replace("₹","Rs") + ","+rating + "\n")
f.close()