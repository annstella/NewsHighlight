from flask import render_template
from app import app
from .request import get_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
     # Getting business article
    business_articles = get_articles('business')
    sports_articles = get_articles('sports')
    technology_articles = get_articles('technology')

    # print(business_articles)
    title = 'Home - Welcome to The best article Highlights Online'
    return render_template('index.html', title = title, business_articles = business_articles, sports_articles = sports_articles, technology_articles = technology_articles)

@app.route('/article/<int:article_id>')
def article(article_id):

    '''
    View article page function that returns the article details page and its data
    '''
    return render_template('article.html',id = article_id)





   
