# import the class that allows us to have abstract classes
from abc import ABCMeta, abstractmethod
from objects.user import User

class NewsAPIDAO:
    __metaclass__ = ABCMeta

    # class constructor
    # nothing
    def __init__(self):
        print ("NewsAPIDAO constructor") #debug

    # to string method
    def toString( self ):
        return ("The only NewsAPIDAOImpl")

    @abstractmethod
    def getUserPreferredCategories(user):
        # Chiama api e ottieni JSON con categories
        # cicla sull'array per ottenere gli audio di ciascuna categoria
        pass

    @abstractmethod
    def getNewsTitlesByCategory(user, category):
        # Chiama api e ottieni JSON con lista news(id, titolo)
        # cicla sull'array per ottenere gli audio di ciascun titolo
        pass

    @abstractmethod
    def getNewsByNewsId(user, news):
        pass

    @abstractmethod
    def updatePreferredNewsCategories( categories ):
        pass
