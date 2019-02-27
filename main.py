import feedparser

Trends = feedparser.parse('https://trends.google.com/trends/trendingsearches/daily/rss?geo=BR')

trend1 = Trends.entries[0]
trend2 = Trends.entries[1]
trend3 = Trends.entries[2]
trend4 = Trends.entries[3]
trend5 = Trends.entries[4]
