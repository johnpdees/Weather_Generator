"""This scraper is intended to pull weather station data from the html code of the CIMIS website. As of yet, this imple
   mentation has been left for another time."""

import requests
from lxml import html

page = requests.get('http://www.cimis.water.ca.gov/Stations.aspx')
tree = html.fromstring(page.content)

#Xpath List
#/html/body/form/div[4]/div[3]/div/div[3]/div[3]/div[2]/div/div/div/table/tbody/tr[1]/td[2]
#/html/body/form/div[4]/div[3]/div/div[3]/div[3]/div[2]/div/div/div/table/tbody/tr[1]/td[3]
#/html/body/form/div[4]/div[3]/div/div[3]/div[3]/div[2]/div/div/div/table/tbody/tr[1]/td[4]
#/html/body/form/div[4]/div[3]/div/div[3]/div[3]/div[2]/div/div/div/table/tbody/tr[1]/td[5]/span

#This will create a list of station numbers:
station_num = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of names
station_name = tree.xpath('//span[@class="item-price"]/text()')
#This will create a list of counties:
counties = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of status
status = tree.xpath('//span[@class="item-price"]/text()')

print('Station Numbers: ', station_num)
print('Station names: ', station_name)
print('Counties: ', counties)
print('Status: ', status)

