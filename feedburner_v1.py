import feedparser
import feedformatter
from multiprocessing.dummy import Pool as ThreadPool
import time

import pdb

urls = [
'http://feeds.feedburner.com/alternative-blog/podcasts',
'http://feeds.feedburner.com/BattlePetsWithAlludraAndKephas',
'http://feeds.feedburner.com/CallToAuction',
'http://feeds.feedburner.com/ClockworkRiot',
'http://feeds.feedburner.com/ctrtoo',
'http://feeds.feedburner.com/BlizzprosHearthstonePodcast',
'http://feeds.feedburner.com/hordeforlife',
'http://feeds.feedburner.com/HuntingPartyPodcastOutdps',
'http://feeds.feedburner.com/outofmanapodcast',
'http://feeds.feedburner.com/PowerWordGold',
'http://feeds.feedburner.com/RaleighitecomHolyShattPodcast',
'http://feeds.feedburner.com/ready_check',
'http://feeds.feedburner.com/therawrcastshow',
'http://feeds.feedburner.com/TheAddicted',
'http://feeds2.feedburner.com/TwistedNetherBlogcast',
'http://feeds.feedburner.com/Warcrafttrolls',
'http://feeds.feedburner.com/WarcraftLessTraveled',
'http://feeds.feedburner.com/WarcraftWellRead',
'http://feeds.feedburner.com/30MinuteCooldown',
'http://feeds.feedburner.com/blogspot/CwJAbe',
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
    site_link = short_list[idx]["feedburner_origlink"].split('/')[2]
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
  feed.format_rss2_file('feedburner_v1.xml')
except:
  pdb.post_mortem()
  
