import feedparser
import feedformatter
from multiprocessing.dummy import Pool as ThreadPool
import time

import pdb

urls = [
'http://legendsoftriumph.podbean.com/feed/',
'http://ctrlaltwow.podbean.com/feed',
'http://cavernsoflore.podbean.com/feed/',
'http://craftingazeroth.podbean.com/feed/',
'http://craftingazeroth.podbean.com/feed/',
'http://hearthstonecast.podbean.com/feed/',
'http://hearthstonecast.podbean.com/feed/',
'http://nonmailsnutz.podbean.com/feed/',
'http://feeds.feedburner.com/HordeHouse',
'http://spareparts.podomatic.com/rss2.xml',
'http://deededeethetank.podomatic.com/rss2.xml',
'http://wowuncensoredshow.podomatic.com/rss2.xml',
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
    site_link = short_list[idx]["link"].split('/')[2]
    new_title = '['+site_link+'] '+short_list[idx]['title']
    short_list[idx]['title'] = new_title
    short_list[idx]['published'] = short_list[idx]['published_parsed']
    short_list[idx]['date'] = short_list[idx]['published_parsed']

feed = feedformatter.Feed()
feed.feed['title'] = "Podbean Feed"
feed.feed['link'] = 'http://www.example.com'
feed.feed['description'] = 'Podbean RSS feed'
feed.feed['published'] = time.localtime()
for entry in short_list:
    feed.items.append(entry)
try:
  feed.format_rss2_file('podbean.xml')
except:
  pdb.post_mortem()
  
