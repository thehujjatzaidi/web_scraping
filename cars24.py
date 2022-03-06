#import the libraries
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#initialize the url
my_url='https://www.cars24.com/buy-used-maruti-suzuki-alto-cars-new-delhi/'


#initate the connection
uClient=uReq(my_url)
page_html=uClient.read()

#parse the file 
page_soup=soup(page_html,"html.parser")

#initilize the variables for parsing
containers=page_soup.findAll('div',{'class':'col-sm-12 col-md-6 col-lg-4'})
print(len(containers))


#initialiuze the file name
filename = "Used_car_data_cars24.csv"

#open the file
f = open(filename,"w")
headers = "Car, Brand, Model, Price, Website \n"

#write headers in the file
f.write(headers)



for container in containers:
	car_raw=container.findAll('div',{'class':'_2UUy0'})
	car_raw1=car_raw[0].h3.get_text().strip()
	car=car_raw1

	price_car=container.findAll('div',{'class':'col-5 col-md-12 col-xl-5'})
	price=price_car[0].get_text()

	f.write(car + "," + car + "," + "Alto" + "," + price.replace("₹","Rs").replace(",","") + "," + "Cars24" + "\n")


'''
	city_in=container.findAll('div',{'class':'item'})
	city=city_in[1].label.get_text()

	mileage_city=container.findAll('div',{'class':'item'})
	driven_kms=mileage_city[2].label.get_text().replace(",","")
	#engine_type=container.findAll('ul',{'class':'text-truncate EhLAi'})
	#engine=engine_type
	#print(engine)

	
	#engine=engine_type.label.string

	'''
	

	#print(car)

f.close()
