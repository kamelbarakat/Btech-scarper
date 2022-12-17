
import requests
from bs4 import BeautifulSoup
import csv
#price_air  = []
#air_title=[]
#specefication=[]
i=[]
j=[]
x=[]

result = requests.get("https://btech.com/ar/major-domestic-appliances/air-conditioning.html")
src = result.content

soup = BeautifulSoup(src,'html.parser')
#print (soup)

air_title= soup.find_all('h2',{'class':'plpTitle'})
for x in air_title:
    print("name is",x.text)

price_air=soup.find_all('span',{'class':'price-wrapper'})
for j in price_air:
    print("price is",j.text)

links = []
mylinks = soup.find_all("a" , {"class":"listingWrapperSection"})
print(len(mylinks))
for i in mylinks :
    links.append(i.get("href"))

for i in links :
    result = requests.get(i)
    src = result.content
    soup = BeautifulSoup(src, 'html.parser')
    specefication = soup.find_all("tbody" , {"id": "product-attribute-specs-table-tbody"} )
    for i in specefication:
        print("specefication",i.text)






