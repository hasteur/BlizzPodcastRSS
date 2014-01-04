import feedparser
import feedformatter
from multiprocessing.dummy import Pool as ThreadPool
import time

import pdb

urls = [
'http://feeds.feedburner.com/CallToAuction',
'http://feeds.feedburner.com/theaddictedcastmp3',
]
pool = ThreadPool(2)

feeds = pool.map(feedparser.parse,urls)

entries = []
for feed in feeds:
  entries.extend( feed["items"])

sorted_entries = sorted(entries, key= lambda entry: entry["published_parsed"])
sorted_entries.reverse()
short_list = sorted_entries[0:200]
for idx, val in enumerate(short_list):
    #pdb.set_trace()
    site_link = short_list[idx]["feedburner_origenclosurelink"].split('/')[2]
    new_title = '['+site_link+'] '+short_list[idx]['title']
    short_list[idx]['title'] = new_title
    short_list[idx]['published'] = short_list[idx]['published_parsed']
    short_list[idx]['date']=short_list[idx]['published_parsed']

feed = feedformatter.Feed()
feed.feed['title'] = "Feedburner Podcasts Feed"
feed.feed['link'] = 'http://www.example.com'
feed.feed['description'] = 'Feedburner Podcasts Feed'
feed.feed['published'] = time.localtime()
for entry in short_list:
    feed.items.append(entry)
try:
  feed.format_rss2_file('feedburner_v2.xml')
except:
  pdb.post_mortem()
  
