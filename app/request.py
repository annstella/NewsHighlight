import urllib.request,json
from .models import Article, Source

#Getting api key
api_key = None

# Getting the article base url
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['ARTICLE_API_KEY']
    base_url = app.config['ARTICLE_API_BASE_URL']

def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['sources']:
            article_results_list = get_articles_response['sources']
            article_results = process_results(article_results_list)


    return article_results

def process_results(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    '''
    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        name = article_item.get('name')
        description = article_item.get('description')
       
        if id:
            article_object = Article(id,name,description)
            article_results.append(article_object)

    return article_results

def get_source(id):

    get_source_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_source_details_url) as url:
        source_details_data = url.read()
        source_details_response = json.loads(source_details_data)

        source_object = None

        if source_details_response:
            id = source_details_response.get('id')
            name = source_details_response.get('original_name')
            description = source_details_response.get('description') 

            source_object = Source(id,name,     author,url,description,country,category)

            return source_object

def process_source(source_list):
    '''
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        author = source_item.get('author')
        url = source_item.get('url')
        description = source_item.get('description')
        country = source_item.get('country')
        category = source_item.get('category')


            
    return source_results