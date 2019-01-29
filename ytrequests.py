import requests
import json

def youtubeSearchRequest(query, **kwargs):
    "Make youtube search request and return response"
    maxResults = str(kwargs.get("maxResults") or "3")
    apikey = kwargs.get("apikey")
    
    requestString = "https://www.googleapis.com/youtube/v3/search/?part=snippet&maxResults=" + maxResults + "&q=" + query + "&type=channel&key=" + apikey
    return requests.get(requestString).json()