import tkinter as tk
import ytrequests, utils, copy, re, os
from functools import reduce

# Search screen
def searchUI(**kwargs):
    "Show search query dialogue and return what was entered"
    width = kwargs.get("width") or 800
    height = kwargs.get("height") or 600
    font = ("Consolas", "30")
    smallFont = ("Consolas", "19")

    root = tk.Tk()
    root.title("Youtube Channel Search")
    searchScreen = tk.Canvas(root, width = width, height = height, bg = 'red')
    searchScreen.pack()

    searchQuery = tk.StringVar()

    searchScreen.create_window(400, 400, window=tk.Entry(searchScreen, fg = "grey", textvariable = searchQuery, width=30, font=font, justify=tk.CENTER))
    youtubeImage = tk.PhotoImage(file="images/searchbox/youtubeicon.gif")
    searchScreen.create_image(400,175,image=youtubeImage)
    searchScreen.create_text(400,325,text="Tkinter Youtube Channel Browser", font=font, fill="white")
    searchScreen.create_window(720, 400, window= tk.Button(searchScreen, text="Go", command=root.destroy, font=smallFont))

    root.mainloop()
    return searchQuery.get()

def helpUI(message, **kwargs):
    "Show help message"
    width = kwargs.get('width') or 800
    height = kwargs.get('height') or 100
    font = ("Leelawadee", "23")

    root = tk.Tk()
    root.title("Help")
    root.geometry("%dx%d+%d+%d" % (width, height, 0, 0))
    window = tk.Canvas(root, width=width, height=height, bg='white')
    window.pack()

    window.create_text(width//2,height//2,text=message, font=font)

    return root

def detailsUI(channelID, **kwargs):
    "Requests and shows details of specified channel"

    width = kwargs.get('width') or 600
    height = kwargs.get('height') or 600
    font = ("Leelawadee", "27")
    mediumFont = ("Leelawadee", "20")
    smallFont = ("Leelawadee", "16")
    apikey = utils.readfile("apikey.key")

    channelData = ytrequests.youtubeChannelRequest(channelID, apikey=apikey)["items"][0] # Request channel data

    snippet = channelData["snippet"]
    topicDetails = channelData["topicDetails"]
    statistics = channelData["statistics"]

    topics = reduce(lambda acc, url:acc+"\n"+url.split("/")[-1].replace("_", " "), topicDetails["topicCategories"], "")

    root = tk.Toplevel() # Since multiple windows will be opened in paralell
    root.title(snippet["title"])
    window = tk.Canvas(root, width=width, height=height, bg='lightGrey')
    window.pack()

    imageURL = snippet["thumbnails"]["default"]["url"]
    thumbnailImage = ytrequests.requestTkImage(imageURL, width=200, height=200)
    window.create_image(width/2, 120, image=thumbnailImage) # Thumbnail

    window.create_text(width/2, 245, text=snippet["title"], font=font)

    window.create_text(width/10, 275, text="Stats", font=mediumFont, anchor=tk.W) # Stats
    window.create_text(width/10, 300, text="Subscribers: " + statistics["subscriberCount"], font=smallFont, anchor=tk.W)
    window.create_text(width/10, 320, text="Total Views: " + statistics["viewCount"], font=smallFont, anchor=tk.W)
    window.create_text(width/10, 340, text="Videos: " + statistics["videoCount"], font=smallFont, anchor=tk.W)

    window.create_text(width/10, 360, text="Topics", font=mediumFont, anchor=tk.NW)
    window.create_text(width/10, 365, text=topics, font=smallFont, anchor=tk.NW)

    window.create_text(width * 1/2, 275, text=snippet["description"][:200], font=smallFont, anchor=tk.NW, width=width/2) # Description
    
    hyperlink = window.create_text(width * 1/3, 500, text="Click to open in youtube", font=mediumFont, anchor=tk.NW, fill="white") # Hyperlink
    window.tag_bind(hyperlink, "<ButtonPress-1>", lambda e:os.system("start https://www.youtube.com/channel/" + channelData["id"]))

    root.mainloop()

def searchResultsUI(data={}, **kwargs):
    "Show search results with thumbnails and descriptions"

    width = kwargs.get('width') or 500
    height = kwargs.get('height') or 600
    font = ("Leelawadee", "23")
    smallFont = ("Leelawadee", "12")

    resultsNumber = data["pageInfo"]["resultsPerPage"]
    
    resultsHeight = height//resultsNumber
    resultsWidth = width

    imagedata = []
    root = tk.Tk()
    root.title("Results")
    window = tk.Canvas(root, width=width, height=height, bg='white')
    window.pack()

    def onclick_helper(snippet):
        return lambda e:detailsUI(snippet["channelId"])

    for i in range(resultsNumber): # Generate search results
        # Relative x and y for (0,0) in mini-box
        y = i*resultsHeight
        x = 0

        # Result variables
        item = data["items"][i]
        snippet = item["snippet"]
        thumburl = snippet["thumbnails"]["default"]["url"]
        channelName = snippet["title"]
        description = reduce(lambda acc, n: acc+n, list(filter(lambda c:ord(c) in range(65536), list(snippet["description"]))))

        window.create_rectangle(x,y,x+resultsWidth,y+resultsHeight, fill='grey' if i % 2 == 0 else 'white') #Draw frome

        imagedata.insert(i,ytrequests.requestTkImage(thumburl)) # Request thumbnail

        clickableimage = window.create_image(x+resultsWidth/5.5, y+resultsHeight/2, image=imagedata[i]) # Add image
        window.tag_bind(clickableimage, "<ButtonPress-1>", onclick_helper(snippet)) # Bind thumbnail with results ui

        window.create_text(x+resultsWidth/2.5,y+resultsHeight/5,text=channelName, font=font, anchor=tk.W, width=str(resultsWidth/2.5) + "p") # Write channel name

        window.create_text(x+resultsWidth/2.5,y+resultsHeight/1.5,text=description.strip()[:200], font=smallFont, anchor=tk.W, width=str(resultsWidth/2.5) + "p") # Write channel description

    helpUI("To see details for each channel, click the thumbnail")
    root.mainloop()
