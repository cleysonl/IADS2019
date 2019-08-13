{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import newspaper\n",
    "import json\n",
    "import pandas as pd\n",
    "\n",
    "#read JSON file\n",
    "with open('uk_news_outlets.json','r') as myfile:\n",
    "    data = myfile.read()\n",
    "\n",
    "#Parse file\n",
    "\n",
    "obj=json.loads(data)\n",
    "table_articles = pd.DataFrame(columns=[\"Article\",\"Source Url\",\"Url\",\"Authors\",\"Title\",\"Publish_date\",\"Text\"])\n",
    "num_art = 0\n",
    "\n",
    "#Add a while to know which ones \n",
    "#Read the urls and get the articles\n",
    "for i in range(4):\n",
    "    for link in (obj['news_outlets']):\n",
    "        print(link)\n",
    "        web_page = newspaper.build(link['url'])\n",
    "        for article in web_page.articles:  \n",
    "            dict_art={}\n",
    "            article.download()\n",
    "            article.parse()\n",
    "            dict_art =pd.DataFrame({ \"Article\": \"Article {}\".format(num_art),\n",
    "                                     \"Source Url\" : article.source_url,\n",
    "                                     \"Url\" : article.url,\n",
    "                                     \"Authors\": article.authors,\n",
    "                                     \"Title\": article.title,\n",
    "                                     \"Publish_date\": article.publish_date,\n",
    "                                     \"Text\": article.text})\n",
    "            table_articles= pd.concat([table_articles,dict_art],axis=0)   \n",
    "            num_art+=1\n",
    "\n",
    "# table_articles.head()\n",
    "\n",
    "art_csv = table_articles.to_csv('art_data1.csv')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
