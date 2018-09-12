import unittest
from app.models import News

class TestNews(unittest.TestCase):
    '''
    Test class to test the behavior of the articles class
    '''
    def setUp(self):
        '''
        Test class to run before other tests
        '''
        self.new_news_source = News('abc','stl','https://abc.com/','abc news is the best source', 'uk', 'general', 'abc-news')
    
    def test_instance(self):
        '''
        '''
        self.assertTrue(isinstance(self.new_news_source,News))
    
    def test_to_check_instance_variables(self):
        '''
        '''
        self.assertEquals(self.new_news_source.name,'abc')
        self.assertEquals(self.new_news_source.author,'stl')
        self.assertEquals(self.new_news_source.url,'https://abc.com/')
        self.assertEquals(self.new_news_source.description,'abc news is the best source')
        self.assertEquals(self.new_news_source.country,'uk')
        self.assertEquals(self.new_news_source.category,'general')
        self.assertEquals(self.new_news_source.id,'abc-news')