import newspaper
# By default, newspaper caches all previously extracted article and eliminates any article it has already extracted
web_page = newspaper.build('https://www.bbc.co.uk/')
web_page.size()
art = web_page.articles
print(art)
# list_wp = []
# for url in web_page.category_urls():
#     if(url[:5]=='https' and url[-1]!='/'):
#         list_wp.append(url)

# print(len(list_wp))
# dict_art ={}
# url1 = list_wp[0]
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
# # print(list_wp)  