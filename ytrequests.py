import requests
import json
from utils import readfile

def youtubeSearchRequest(query, **kwargs):
    "Make youtube search request and return response"
    maxResults = str(kwargs.get("maxResults") or "3")
    apikey = kwargs.get("apikey")
    
    requestString = "https://www.googleapis.com/youtube/v3/search/?part=snippet&maxResults=" + maxResults + "&q=" + query + "&type=channel&key=" + apikey
    try:
        response = requests.get(requestString).json()
    except:
        response = json.loads(readfile("APIResponses/response_Ninja_.json")) #TODO Return actual error response
    
    return response