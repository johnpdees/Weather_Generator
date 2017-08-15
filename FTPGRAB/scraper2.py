import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()



url = "http://www.cimis.water.ca.gov/Stations.aspx"  # change to whatever your url is
response = http.request('GET', url)
soup = BeautifulSoup(response.data, "lxml")


#for i in soup.find_all('form'):
#    print (i.attrs['class'])


for tr in soup.find_all('tr')[2:]:
    tds = tr.find_all('td')
    print (tds[0:])



