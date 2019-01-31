import requests
import json
import utils

def youtubeSearchRequest(query, **kwargs):
    "Make youtube search request and return response"
    maxResults = str(kwargs.get("maxResults") or "3")
    apikey = kwargs.get("apikey")
    
    requestString = "https://www.googleapis.com/youtube/v3/search/?part=snippet&maxResults=" + maxResults + "&q=" + query + "&type=channel&key=" + apikey
    try:
        response = requests.get(requestString).json()
    except:
        response = json.loads(utils.readfile("APIResponses/response_Ninja_.json")) #TODO Return actual error response
    
    return response

def downloadImage(url, imageName="untitled.jpg"):
    "Dowloads image, returns status code"
    response = requests.get(url)
    if response.status_code == 200:
        with open("images/_temp/" + imageName, 'wb') as f:
            f.write(response.content)
    
    return response.status_code