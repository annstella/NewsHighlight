class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,id,name,description):
        self.id =id
        self.name = name
        self.description = description

class Source:

    all_sources = []

    def __init__(self,id,name,author,url,description,country,category):
        self.id = id
        self.name = name
        self.author = author
        self.url = url
        self.description = description
        self.country = country
        self.category = category


    def save_source(self):
        Source.all_sources.append(self)


    @classmethod
    def clear_sources(cls):
        Source.all_sources.clear()

    @classmethod
    def get_sources(cls,id):

        response = []

        for source in cls.all_sources:
            if source.id == id:
                response.append(source)

        return response