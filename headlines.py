# from flask import Flask
# app = Flask(__name__)
# @app.route("/")
# def get_news():
#     return "no news is good news"
# if __name__ == '__main__':
#     app.run(port=5000, debug=True)


#########################################################################################
# import feedparser
# from flask import Flask,render_template,request,redirect,url_for

# app = Flask(__name__)


# BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

# @app.route("/")
# def get_news():
#     feed = feedparser.parse(BBC_FEED)
#     first_article = feed['entries'][0]
#     return render_template('output.html').format(first_article.get("title"),
#     first_article.get("published"),first_article.get("summary"))

# if __name__ == "__main__":
#     app.run(port=5000, debug=True)
####################################################################################################

import feedparser
from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)
RSS_FEED = {'zee':'http://zeenews.india.com/rss/technology-news.xml',
    'news18':'http://www.news18.com/rss/india.xml',
    'toi':
    'http://timesofindia.indiatimes.com/rssfeeds/4719161.cms'
}
@app.route('/')
@app.route("/zee")
def zee():
    return get_news('zee')
# @app.route("/news18")
# def news18():
#     return get_news('news18')
# @app.route("/toi")
# def toi():
#     return get_news('toi')
@app.route("/<publication>")
#def get_news(publication="bbc"):

def get_news(publication):
    feed = feedparser.parse(RSS_FEED[publication])
    heading= publication.capitalize()
    first_article = feed['entries'][0]
    return render_template('output.html',heading=heading).format(first_article.get("title"),
    first_article.get("published"), first_article.get("summary"))
if __name__=='__main__':
    app.run(debug=True)
###################################################################################################