import feedparser
import wikipedia
wikipedia.set_lang('pt')

Trends = feedparser.parse('https://trends.google.com/trends/trendingsearches/daily/rss?geo=BR')

for trend in Trends.entries:
    wiki_result = wikipedia.summary(trend.title)
