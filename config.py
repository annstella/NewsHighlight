import os
class Config:
    '''
    General configuration parent class
    '''
    ARTICLE_API_BASE_URL='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    SOURCE_API_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    NEWS_API




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

Config_options = {
    'development':Devconfig,
    'production': ProdConfig
}