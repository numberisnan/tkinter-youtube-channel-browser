import requests, json, utils, io
from PIL import ImageTk, Image

def youtubeSearchRequest(query, **kwargs):
    "Make youtube search request and return response"
    maxResults = str(kwargs.get("maxResults") or 3)
    apikey = kwargs.get("apikey")
    
    requestString = "https://www.googleapis.com/youtube/v3/search/?part=snippet&maxResults=" + maxResults + "&q=" + query + "&type=channel&key=" + apikey
    
    try:
        response = requests.get(requestString).json()
    except:
        response = json.loads(utils.readfile("APIResponses/response_Ninja_.json")) #Return test file if there is no internet
    
    return response

def requestTkImage(url, **kwargs):
    "Downloads image, returns tkinter.PhotoImage instance"
    width = kwargs.get("width") or 150
    height = kwargs.get("height") or 150

    try:
        response = requests.get(url)
    except:
        return requestTkImage("http://127.0.0.1:8887/response_Thumbnail_.jpg", width=width, height=height) #Try local source for testing if no internet
    
    return ImageTk.PhotoImage(image=Image.open(io.BytesIO(response.content)).resize((width,height), Image.ANTIALIAS)) # Resize image and return Tk.PhotoImage instance

def youtubeChannelRequest(channelID, **kwargs):
    "Make youtube channel detail request and return response"
    apikey = kwargs.get("apikey")

    requestString = "https://www.googleapis.com/youtube/v3/channels?part=%s&id=%s&key=%s" % ("snippet,statistics,topicDetails", channelID, apikey)

    try:
        response = requests.get(requestString).json()
    except:
        response = json.loads(utils.readfile("APIResponses/response_MrBeast_Channel.json")) #Return test file if there is no internet
    
    return response