import feedparser
import feedformatter
import time

import pdb

feeds = []

#WoW Uncensored Cleanup
wowunc = feedparser.parse('http://www.rivalcastmedia.com/shows/Wow-uncensored/rss.xml')
for idx, val in enumerate(wowunc["items"]):
    new_title = '[WoW Uncensored]'+wowunc["items"][idx]['title']
    wowunc["items"][idx]['title'] = new_title
feeds.append(wowunc)

#The Starting Zone Cleanup
tsz = feedparser.parse('http://www.emissarypictures.com/tsz/thestartingzone.xml')
for idx, val in enumerate(tsz["items"]):
    new_title = '[thestartingzone.com]'+tsz["items"][idx]['title']
    tsz["items"][idx]['title'] = new_title
feeds.append(tsz)

#Outlandish Cleanup
outlandish = feedparser.parse('http://www.outlandishpodcast.com/podcasts/podcast.xml')
for idx, val in enumerate(outlandish["items"]):
    new_title = '[www.outlandishpodcast.com]'+outlandish["items"][idx]['title']
    outlandish["items"][idx]['title'] = new_title
feeds.append(outlandish)

#DMF Cleanup
dmf = feedparser.parse('http://ngeonline.com/podcast/darkmoon-herald/feed/')
for idx, val in enumerate(dmf["items"]):
    new_title = '[darkmoonherald.com]'+dmf["items"][idx]['title']
    dmf["items"][idx]['title'] = new_title
feeds.append(dmf)

#The Mana Cooler Cleanup
mana = feedparser.parse('http://themanacooler.com/podcasts-only/rss2.aspx')
for idx, val in enumerate(mana["items"]):
    new_title = '[themanacooler.com]'+mana["items"][idx]['title']
    mana["items"][idx]['title'] = new_title
feeds.append(mana)

#The Mana Cooler Cleanup
meh = feedparser.parse('http://myepicheals.com/podcasts-only/rss2.aspx')
for idx, val in enumerate(meh["items"]):
    new_title = '[myepicheals.com]'+meh["items"][idx]['title']
    meh["items"][idx]['title'] = new_title
feeds.append(meh)

#The Instance Cleanup
instance = feedparser.parse('http://www.myextralife.com/ftp/radio/instance_rss.xml')
for idx, val in enumerate(instance["items"]):
    new_title = '[The Instance]'+instance["items"][idx]['title']
    instance["items"][idx]['title'] = new_title
feeds.append(instance)

#Grand Old Podcast Cleanup
gop = feedparser.parse('http://www.rivalcastmedia.com/shows/grand-old-podcast/rss.xml')
for idx, val in enumerate(gop["items"]):
    new_title = '[Grand Old Podcast]'+gop["items"][idx]['title']
    gop["items"][idx]['title'] = new_title
feeds.append(gop)

#Epic Podcast Cleanup
epic = feedparser.parse('http://files.epicpodcast.com/EpicPodcast/Epicpodcast.xml')
for idx, val in enumerate(epic["items"]):
    new_title = '[Epic Podcast]'+epic["items"][idx]['title']
    epic["items"][idx]['title'] = new_title
feeds.append(epic)

#The Angry Chicken Cleanup
epic = feedparser.parse('http://feeds.feedburner.com/amoveradio')
for idx, val in enumerate(epic["items"]):
    new_title = '[Amove Radio]'+epic["items"][idx]['title']
    epic["items"][idx]['title'] = new_title
feeds.append(epic)
#The Angry Chicken Cleanup
epic = feedparser.parse('http://feeds.feedburner.com/theangrychicken')
for idx, val in enumerate(epic["items"]):
    new_title = '[The Angry Chicken]'+epic["items"][idx]['title']
    epic["items"][idx]['title'] = new_title
feeds.append(epic)

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
  feed.format_rss2_file('fixer_feed.xml')
except:
  pdb.post_mortem()
  
