import unittest
from app.models import article
Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('name of the article',)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

