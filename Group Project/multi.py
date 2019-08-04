# Downloading articles one at a time is slow. But spamming a single news source like cnn.com with tons of 
# threads or with ASYNC-IO will cause rate limiting and also doing that is very mean.

# We solve this problem by allocating 1-2 threads per news source to both greatly speed up the download
#  time while being respectful.

import newspaper
from newspaper import news_pool

slate_paper = newspaper.build('http://slate.com')
tc_paper = newspaper.build('http://techcrunch.com')
espn_paper = newspaper.build('http://espn.com')

papers = [slate_paper, tc_paper, espn_paper]
news_pool.set(papers, threads_per_source=2) # (3*2) = 6 threads total
news_pool.join()

# At this point, you can safely assume that download() has been
# called on every single article for all 3 sources.
print(news_pool)