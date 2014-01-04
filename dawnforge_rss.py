import feedparser
import feedformatter
from multiprocessing.dummy import Pool as ThreadPool
import time

import pdb

urls = [
'http://feeds.feedburner.com/GroupQuest',
'http://feeds.feedburner.com/Azeroth',
'http://feeds.feedburner.com/obscurecast',
'http://feeds.feedburner.com/shatteredstone'
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
    site_link = ''
    if short_list[idx].has_key('feedburner_origlink'):
        site_link = short_list[idx]["feedburner_origlink"].split('/')[2]
    new_title = '['+site_link+'] '+short_list[idx]['title']
    short_list[idx]['title'] = new_title
    short_list[idx]['published'] = short_list[idx]['published_parsed']

feed = feedformatter.Feed()
feed.feed['title'] = "Dawnforge Feed"
feed.feed['link'] = 'http://www.thedawnforge.com'
feed.feed['description'] = 'Dawnforge Network Feed'
feed.feed['published'] = time.localtime()
for entry in short_list:
    feed.items.append(entry)
try:
  feed.format_rss2_file('dawnforge.xml')
except:
  pdb.post_mortem()
  
