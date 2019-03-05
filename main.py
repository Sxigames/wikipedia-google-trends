import feedparser
import wikipedia


def get_wiki_results(feed_geo, wiki_lang):
    wikipedia.set_lang(wiki_lang)
    trends = feedparser.parse(f'https://trends.google.com/trends/trendingsearches/daily/rss?geo={feed_geo}')
    wiki_results = []
    for trend in trends.entries:
        try:
            wiki_result = wikipedia.summary(trend.title)
            result = {trend.title, wiki_result}
            wiki_results.extend([result])
        except:
            result = {trend.title, "No Result."}
            wiki_results.extend([result])
    return wiki_results


def generate_html():
    html = open('index.html', 'w', encoding='utf-8')
    html.write("""<html>
    <head></head><body><center><h1>Trends</h1></center><br><br><br>""")
    for result in get_wiki_results('BR', 'pt') :
        try:
            html.write(f"""<center><p>{result.title}</p></center><br><p>{result.wiki_result}</p><br><br>""")
        except:
            html.write(f"""<center><p>{result.title}</p></center><br><p>Não foi possivel  achar resultados sobre {result.title} na
            Wikipedia</p><br><br>""")
    html.write("""</body></html>""")
    html.close()


generate_html()
