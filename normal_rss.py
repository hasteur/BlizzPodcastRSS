import feedparser
import feedformatter
from multiprocessing.dummy import Pool as ThreadPool
import time

import pdb

urls = [
'http://abashima.com/30mc?format=rss',
'http://arcanumofazeroth.blogspot.com/feeds/posts/default?alt=rss',
'http://azerothpirateradio.com/feed/',
'http://azerothroundtable.blogspot.com/feeds/posts/default?alt=rss',
'http://battlepets.libsyn.com/rss',
'http://bitterandsalty.com/?feed=podcast',
'http://casuallycasualcast.com/feed/',
'http://convertedpodcast.com/?feed=rss2',
'http://converttoraid.libsyn.com/rss',
'http://eviscerated.net/?feed=gamingpodcast',
'http://gamediplomat.com/category/pet-battle/feed/',
'http://girlsgonewow.net/?feed=rss2',
'http://hearthcast.com/feed.xml',
'http://hordeforlife.libsyn.com/rss',
'http://letswowpodcast.com/feed',
'http://liquidwow.libsyn.com/rss',
'http://middlefingerpodcast.com/feed/',
'http://myepicheals.com/podcasts-only/rss2.aspx',
'http://myepicheals.com/rss2.aspx',
'http://ngeonline.com/podcast/darkmoon-herald/feed/',
'http://pressypodcast.com/?feed=podcast',
'http://realm-maintenance.com/category/realm-maintenance/rm-microcast/feed/',
'https://portal.aie-guild.org/feed/podcast/',
'http://stormridecast.libsyn.com/rss',
'http://theazerothperspective.com/shownotes?format=rss',
'http://thelorewalkers.podbean.com/feed/',
'http://thesundering.net/feed/',
'http://twibshow.squarespace.com/twib/rss.xml',
'http://vote2kick.hipcast.com/rss/vote2kick.xml',
'http://worldofwarcast.com/?feed=rss2',
'http://wow.joystiq.com/category/wow-insider-show/rss.xml',
'http://wowphiles.com/category/podcast/feed/',
'http://wowtcg.libsyn.com/rss',
'http://www.5wowthings.com/?feed=rss2',
'http://www.apaladinstale.com/?post_type=podcast&feed=rss2',
'http://www.auctionhousejunkies.com/feeds/posts/default?alt=rss',
'http://www.bindonequip.com/?feed=rss2',
'http://www.edpodcast.com/feed/',
'http://www.epicpodcast.com/imported-20110407170325/rss.xml',
'http://www.follow-the-leader.net/feed/',
'http://www.gkick.net/category/podcasts/gkick/feed/',
'http://www.gnomeseyeview.com/?feed=podcast',
'http://www.hordehouse.com/feed/',
'http://www.huntingpartypodcast.com/feed/',
'http://www.nordrassilradio.com/feed/',
'http://www.raleighite.com/category/holyshatt/feed/',
'http://www.rivalcastmedia.com/shows/Sheep-moon/rss.xml',
'http://www.stopcast.net/feed.xml',
'http://www.taurenthinktank.com/feed.xml',
'http://www.teamwafflecast.com/RSSGen/podcastgen1.3/feed.xml',
'http://www.thedrunkenmogul.com/feed/podcast/',
'http://www.thetrainingdummies.com/category/podcast/feed/',
'http://www.trollcasts.com/feed/',
'http://realm-maintenance.com/category/realm-maintenance/rm-microcast/feed/',
'http://www.warcraftlounge.com/feed/',
'http://yourwowmoney.com/feed/',
'http://feeds.feedburner.com/YourWowMoneypodcast',
'http://feeds.podtrac.com/6sgIkipC2Sk$',
'http://themeetingstone.com/feed/podcast/',
'http://thedungeonjournal.podomatic.com/rss2.xml',
'http://blizzmaster.com/category/shows/blizzmastershow/feed/',
'http://www.tankingthefloor.com/feed/podcast/',
'http://somethingsuggestive.com/feed/',
'http://www.patchdaycast.com/?feed=podcast',
'http://www.monkcraftpodcast.com/?feed=podcast',
'http://lowpopwow.libsyn.com/rss',
'http://www.lorewalkersroundtable.com/?feed=rss2',
'http://hotscast.twistednether.net/?feed=podcast',
'http://www.gnomeseyeview.com/?feed=podcast',
'http://fel-tron.com/feed/podcast',
'http://CRR.podbean.com/feed/',
'http://closingbell.podomatic.com/rss2.xml',
'http://chaosportalshow.com/episodes/?feed=podcast',
'http://www.blizzconcountdown.com/category/podcast-episodes-podcast-episodes/feed/',
'http://behindtheavatar.podomatic.com/rss2.xml',
'http://aoecast.com/?feed=podcast',
'http://allpetsallowed.podbean.com/feed/',

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
  feed.format_rss2_file('normal.xml')
except:
  pdb.post_mortem()
  
