from app import app
import urllib.request,json
from .models import article

Article = article.Article

#Getting api key
api_key = app.config['ARTICLE_API_KEY']