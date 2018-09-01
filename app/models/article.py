class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,id,name,title,description,url,urlToImage,publishedAt):
        self.id =id
        self.name = name
        self.title = title
        self.description = description
        self.url = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.urlToImage = urlToImage
        self.publishedAt =publishedAt