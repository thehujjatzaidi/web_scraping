#import the libraries
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#initialize the url
my_url='https://droom.in/cars?page=1&tab=grid&bucket=car&category=car&model=swift&make=maruti+suzuki'


#initate the connection
uClient=uReq(my_url)
page_html=uClient.read()

#parse the file 
page_soup=soup(page_html,"html.parser")

#initilize the variables for parsing
containers=page_soup.findAll('div',{'class':'col-lg-4 col-md-4 col-sm-2'})
print(len(containers))

#initialiuze the file name
filename = "Used_car_data.csv"

#open the file
f = open(filename,"w")
headers = "Car, Brand, Model, Mileage, Price, City, Website \n"

#write headers in the file
f.write(headers)



for container in containers:
	car_raw=container.findAll('div',{'class':'header'})
	car_raw1=car_raw[0].get_text().strip()
	car=car_raw1.replace("used","").replace(" ","").strip()
	
	engine_type=container.findAll('div',{'class':'item'})
	engine=engine_type[0].label.get_text().replace(" ","").strip()

	price_car=container.findAll('div',{'class':'price'})
	price=price_car[0].get_text().replace(" ","").replace(",","").strip()

	city_in=container.findAll('div',{'class':'item'})
	city=city_in[1].label.get_text().replace(" ","").strip()

	mileage_city=container.findAll('div',{'class':'item'})
	driven_kms=mileage_city[2].label.get_text().replace(",","").replace(" ","").strip()

	
	#engine=engine_type.label.string

	
	f.write(car + "," + car.strip() + "," + "Swift" + "," + driven_kms.strip() + "," + price.replace("₹","Rs") + "," + city + "," + "Droom" + "\n")
	print(car.strip(), "swift", driven_kms, price, city, "droom")

f.close()


