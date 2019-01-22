from dialogues import searchQueryDialogue
from ytrequests import youtubeSearchRequest
from utils import readfile

query = searchQueryDialogue()

apikey = readfile("apikey.key")

searchResults = youtubeSearchRequest(query, apikey=apikey, maxResults=3)

#print(repr(searchResults))

