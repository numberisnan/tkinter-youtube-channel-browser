from ui import searchUI
from ytrequests import youtubeSearchRequest
from utils import readfile

query = searchUI()

apikey = readfile("apikey.key")

searchResults = youtubeSearchRequest(query, apikey=apikey, maxResults=3)

#print(repr(searchResults))

