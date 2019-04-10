import feedparser
import wikipedia
wikipedia.set_lang('pt')
html = open('index.html', 'w', encoding='utf-8')
Trends = feedparser.parse('https://trends.google.com/trends/trendingsearches/daily/rss?geo=BR')

html.write("""<html>
<head></head><body><center><h1>Trends</h1></center><br><br><br>""")
for trend in Trends.entries:
    try:
        wiki_result = wikipedia.summary(trend.title)
        html.write(f"""<center><p>{trend.title}</p></center><br><p>{wiki_result}</p><br><br>""")
    except:
        html.write(f"""<center><p>{trend.title}</p></center><br><p>Não foi possivel  achar resultados sobre {trend.title} na 
        WikiPedia</p><br><br>""")


html.write("""</body></html>""")
html.close()