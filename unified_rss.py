import feedparser
import feedformatter
from multiprocessing.dummy import Pool as ThreadPool
import time

import pdb

urls = [
'dawnforge.xml',
'feedburner_v1.xml',
'feedburner_v2.xml',
'fixer_feed.xml',
'normal.xml',
'podbean.xml',
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
    short_list[idx]['published'] = short_list[idx]['published_parsed']

feed = feedformatter.Feed()
feed.feed['title'] = "Blizzard Podcast Feed"
feed.feed['link'] = 'http://www.example.com'
feed.feed['description'] = 'Blizzard Podcast Feed maintained by hasteur'
feed.feed['published'] = time.localtime()
for entry in short_list:
    feed.items.append(entry)
try:
  feed.format_rss2_file('blizzard.xml')
except:
  pdb.post_mortem()
  
