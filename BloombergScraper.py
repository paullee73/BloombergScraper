import urllib2  
from bs4 import BeautifulSoup  
import csv
from Countries import Countries

quote_page = 'https://www.bloomberg.com/quote/BBL:TB' 
page = urllib2.urlopen(quote_page) 
soup = BeautifulSoup(page, 'html.parser')

#get name
name_box = soup.find('h1', attrs={'class': 'name'}) 
if(name_box != None):
    name = name_box.text.strip() # strip() is used to remove starting and trailing  
    print name  

#get sector
sector_name = soup.find('a', attrs={'href':'/markets/sectors/financials'})
if(sector_name != None):
    sector = sector_name.text.strip()
    print sector
else:
    sector = None

#get industry
industry_name = soup.find('a', attrs={'data-tracker-label':'financials.02'})
if(industry_name != None):    
    industry = industry_name.text.strip()
    print industry
else:
    industry = None

#get profile
profile_info = soup.find('div', attrs={'class':'profile__description'})
if(profile_info != None):
    profile = profile_info.text.strip()
    print profile
else:
    profile = None


#get country
country_name = soup.find('div', attrs={'class':'profile__detail profile__detail__address'})
if(country_name != None):
    country = country_name.text.strip().split()
    lastEle = country[len(country)-1]
    countryObj = Countries()
    country = countryObj.find_country(lastEle)

# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:  
    writer = csv.writer(csv_file)
    writer.writerow([name, sector, industry, profile, country])
