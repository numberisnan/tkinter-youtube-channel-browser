import requests, json, utils, io
from PIL import ImageTk, Image

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

def requestTkImage(url):
    "Downloads image, returns tkinter.PhotoImage instance"
    try:
        response = requests.get(url)
    except:
        return requestTkImage("http://127.0.0.1:8887/response_Thumbnail_.jpg") #Try local source for testing if no internet TODO Add actual error handling
    
    return ImageTk.PhotoImage(image=Image.open(io.BytesIO(response.content)).resize((150,150), Image.ANTIALIAS))