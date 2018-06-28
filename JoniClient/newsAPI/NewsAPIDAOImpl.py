# import the class that allows us to have abstract classes
from abc import ABCMeta, abstractmethod

# import interface
from newsAPIDAO import NewsAPIDAO
from objects.user import User

#import requests library to communicate with Server API
import requests
# import shutil
import json

#BASE_URL = 'http://192.168.137.1:3000/'
BASE_URL = 'http://4e9c9328.ngrok.io/'
CATEGORIES_PATH = 'categories/'
NEWS_PATH = 'news/'
USERS_PATH = 'users/'
AUDIOS_PATH = 'media/audio/'

NEWS_AUDIO_PATH = AUDIOS_PATH+"news/"
NEWS_TITLES_AUDIO_PATH = NEWS_AUDIO_PATH+"titles/"
NEWS_DESCRIPTIONS_AUDIO_PATH = NEWS_AUDIO_PATH+"descriptions/"

CATEGORIES_AUDIO_PATH = AUDIOS_PATH+"categories/"

AUDIOS_FORMAT = ".mp3"

newsList = []
categoriesList = []

class NewsAPIDAOImpl(NewsAPIDAO):
    __metaclass__ = ABCMeta

    # class constructor
    # nothing
    def __init__(self):
        super(NewsAPIDAO, self).__init__()
        print ("NewsAPIDAO constructor") #debug

    # to string method
    def toString( self ):
        return ("The only NewsAPIDAOImpl")

    def getUserPreferredCategories(self,user):

        url = BASE_URL+CATEGORIES_PATH
        audio = []
        categoriesList = []

        # Chiama api e ottieni JSON con categories
        req = requests.get(url+str(user.userId))
        if req.status_code == 200:
            for category in req.json():
                categoriesList.append(category)
            for category in categoriesList:
                u = url+category['name']+'/audio'
                # path storage audio locale
                path = CATEGORIES_AUDIO_PATH+category['name']+AUDIOS_FORMAT
                # path aggiunto al json locale
                category['nameAudioPath'] = path
                # scarica audio
                audio = requests.get(u, stream=True)
                # salva l'audio
                open(path, 'wb').write(audio.content)
        return categoriesList


    def getNewsTitlesByCategory(self,user,category):
        url = BASE_URL+NEWS_PATH
        audio = []

        # Chiama api e ottieni JSON con lista news
        req = requests.get(url+str(user.userId)+"/"+category+"/latest")
        if req.status_code == 200:
            for news in req.json():
                newsList.append(news)

            # Cicla sugli id delle news per ottenere audio dei titoli
            for news in req.json():
                newsId = news['newsId']
                u = url+str(user.userId)+"/"+newsId+"/title"
                path = NEWS_TITLES_AUDIO_PATH+newsId+AUDIOS_FORMAT
                news['titleAudioPath'] = path
                audio = requests.get(u)
                open(path, 'wb').write(audio.content)

        return req.json()

    def getNewsByNewsId(self,user,newsId):
        url = BASE_URL+NEWS_PATH
        audio = []

        # Chiama api e ottieni JSON della news
        ## json gia' preso quando vegono scaricati i titoli
        ## non serve ottenere di nuovo json
        # req = requests.get(url+str(user.userId)+"/"+newsId)
        # if req.status_code == 200:
        #     for news in req.json():
        #         tmp.append(news['newsId'])

        for news in newsList:
            if news['newsId'] == newsId:
                tmp = news

        # Ottieni audio della news
        id = tmp['newsId']
        u = url+str(user.userId)+"/"+id+"/description"
        path = NEWS_DESCRIPTIONS_AUDIO_PATH+newsId+AUDIOS_FORMAT
        newsDescriptionPath = path
        audio = requests.get(u)
        open(path, 'wb').write(audio.content)
        return tmp


    def updatePreferredNewsCategories(self, user, categories):
        url = BASE_URL+USERS_PATH
        cat = []
        cat = categories
        # chiama API per aggiornare categorie preferite utente
        u = url
        r = requests.post(url, json = {"userId": user.userId, "categories": categories})
        return True
