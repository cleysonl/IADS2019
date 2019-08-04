import newspaper
import json

#read JSON file
with open('uk_news_outlets.json','r') as myfile:
    data = myfile.read()

#Parse file
obj=json.loads(data)
dict_pages = {}

#Read the urls and get the articles
for link in (obj['news_outlets']):
    web_page = newspaper.build(link['url'])
    for article in web_page.articles:
        print(article.source_url)
        article.download()
        article.parse()
        print("\nAuthors: {}\n".format(article.authors))
        print("\nPublish Date: {}\n".format(article.publish_date))
        print("\nTitle: {}\n".format(article.title))
        print("\nUrl: {}\n".format(article.source_url))
        print("\nUrl: {}\n".format(article.url))    
        # print("\nText: {}\n".format(article.text))

    # print(link['name'])
    # print(link['url'])



#By default, newspaper caches all previously extracted article and eliminates any article it has already extracted
# web_page = newspaper.build('https://www.bbc.co.uk/')
# web_page.size()
# count = 0
# for article in web_page.articles:
#         print(article.source_url)
#         article.download()
#         article.parse()
#         print("\nAuthors: {}\n".format(article.authors))
#         print("\nPublish Date: {}\n".format(article.publish_date))
#         print("\nPublish Date: {}\n".format(article.title))
#         print("\nText: {}\n".format(article.text))
#         count +=1
# print(count)


# print(art)
# list_wp = []
# for url in web_page.category_urls():
#     if(url[:5]=='https' and url[-1]!='/'):
#         list_wp.append(url)

# print(len(list_wp))
# dict_art ={}
# url1 = list_wp[1]
# first_article = newspaper.Article(url= url1)    
# first_article.download()
# first_article.parse()
# dict_art["Article:{}".format(1)] = ({"Authors": first_article.authors,
#                                             "Title": first_article.title,
#                                             "Publish_date": first_article.publish_date,
#                                             "Text": first_article.text})
# for item in dict_art:
#     print(dict_art[item])
# for item in list_wp:
#     print(item)
# print(list_wp)  