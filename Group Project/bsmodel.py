import urllib.request, urllib.error
import requests
from bs4 import BeautifulSoup
import json
import newspaper
import pandas as pd


#os.chdir("/Users/samanthalee/preqin")
data = {}
data['article'] = []

with open('uk_news_outlets.json','r') as json_file:
    news_outlet = json.load(json_file)
    for n in news_outlet['news_outlets']:
        url = n['url']
        print(url)
        try:
            response = urllib.request.urlopen(url)
        
            soup = BeautifulSoup(response, 'html.parser')
        
            for link in soup.find_all('a'):
                data['article'].append({'url': link.get('href')},)
        except urllib.error.URLError as e:
            print(e.reason)

with open('article.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

with open('article.json','r') as myfile:
    data = myfile.read()

#Parse file

obj=json.loads(data)
table_articles = pd.DataFrame(columns=["Article","Source Url","Url","Authors","Title","Publish_date","Text"])
num_art = 0

#Add a while to know which ones 
#Read the urls and get the articles
for link in (obj['news_outlets']):
    print(link)
    web_page = newspaper.build(link['url'])
    for article in web_page.articles:
        dict_art={}
        article.download()
        article.parse()
        dict_art =pd.DataFrame({ "Article": "Article {}".format(num_art),
                                "Source Url" : article.source_url,
                                "Url" : article.url,
                                "Authors": article.authors,
                                "Title": article.title,
                                "Publish_date": article.publish_date,
                                "Text": article.text})
        table_articles= pd.concat([table_articles,dict_art],axis=0)   
        num_art+=1

# table_articles.head()

art_csv = table_articles.to_csv('art_data1.csv')
