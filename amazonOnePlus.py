from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url="https://www.amazon.in/s?k=one+plus&ref=nb_sb_noss_2"
uClient=uReq(my_url)
page_html=uClient.read()
page_soup=soup(page_html,'html.parser')

filename='amazonOnePlus.csv'
f=open(filename,"w")
headers=("Model,Price\n")
f.write(headers)

containers=page_soup.findAll("div",{"class":"s-include-content-margin s-border-bottom"})
#print(len(containers))

for container in containers:
	model_name=container.findAll("div",{"class":"a-section aok-relative s-image-fixed-height"})
	model=model_name[0].img['alt']

	price_m=container.findAll("div",{"class":"a-row a-size-base a-color-secondary"})
	price_mo=container.findAll("span")
	price=price_mo[7].text



	print(model.replace("(Renewed)",""), price.replace(",",""))
	f.write(model.replace("(Renewed)","").replace(",","")+ "," + price.replace(",","").replace("₹","Rs")+ "\n")

f.close()