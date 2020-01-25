import pandas as pd
import numpy as np
import requests
import lxml.html as lh
import requests
from bs4 import BeautifulSoup
import re
import json


def get_data(urls, outpath): 
    total_list = {}
    full_list_images = []
   
    for u in urls: 
        page = requests.get(u)
        soup = BeautifulSoup(page.content,'html.parser')
        tb = soup.find_all('table', class_='main')
        title = soup.find('title').get_text('title')[16:]   

        list_names = []
        images = []
        for link in tb:
            name = link.find('b')
            list_names.append(name.get_text('title'))
            images.append(link.find('img').get('src'))

            #to-do next week: get dimensions 
           # dim = link.find('table').text[46:].split(',')[2]
           # string = dim.replace(' ','').replace('\n','').replace('\xa0','')
        
        full_list_images.append(images)
        total_list[title] = list_names,images
        if not os.path.exists(outpath):
            os.mkdir(outpath)
        #pd.DataFrame(total_list).to_csv(str(outpath)+str(u)+\'.csv')
    
    return total_list


cfg = json.load(open('config_a1.json'))   
data = get_data(**cfg)

links = []
titles = []
for i in data.values(): 
    links.append(i[1])
    titles.append(i[0])

df = pd.DataFrame({'name of painting':titles,'img link':links}, index=[list(data.keys())])
df.head()


#download paintings locally 
full_list_images #contains all the images on all the sites

'''
def download_images(full_list_images): 
    links = soup.find('figure').find_all('img', src=True)
    for link in links:
        timestamp = time.asctime() 
        txt = open('%s.jpg' % timestamp, "wb")
        link = link["src"].split("src=")[-1]
        download_img = urllib2.urlopen(link)
        txt.write(download_img.read())

        txt.close()
'''
