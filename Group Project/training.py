import newspaper
import json
import pandas as pd
from newspaper import news_pool

#read JSON file
with open('uk_news_outlets.json','r') as myfile:
    data = myfile.read()

#Parse file

obj=json.loads(data)
table_articles = pd.DataFrame(columns=["Article","Source Url","Url","Authors","Title","Publish_date","Text"])
num_art = 0

#Add a while to know which ones 
#Read the urls and get the articles
for i in range(4):
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
