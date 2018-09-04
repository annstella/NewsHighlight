from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_articles,get_source
from ..models import Source

# Views
@main.route('/')
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

@main.route('/article/<int:article_id>')
def article(article_id):

    '''
    View article page function that returns the article details page and its data
    '''
    article = get_article(id)
    title = f'{article.title}'
    return render_template('article.html', title = title,id = article_id)





   
