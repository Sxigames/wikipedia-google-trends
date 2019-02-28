import feedparser
import wikipedia
wikipedia.set_lang('pt')
html = open('index.html', 'w', encoding='utf-8')
Trends = feedparser.parse('https://trends.google.com/trends/trendingsearches/daily/rss?geo=BR')

html.write("""<html>
<head></head><body>""")
for trend in Trends.entries:
    wiki_result = wikipedia.summary(trend.title)
    html.write(f"""<p>{wiki_result}</p><br>""")


html.write("""</body></html>""")
html.close()
