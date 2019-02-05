import tkinter as tk
import ytrequests

# Search screen
def searchUI():
    "Show search query dialogue and return what was entered"
    width = 800
    height = 600

    root = tk.Tk()
    root.title("Youtube Channel Search")
    searchScreen = tk.Canvas(root, width = width, height = height, bg = 'red')
    searchScreen.pack()

    searchQuery = tk.StringVar()
    font = ("Consolas", "30")
    smallFont = ("Consolas", "19")

    searchScreen.create_window(400, 400, window=tk.Entry(searchScreen,fg = "grey", textvariable = searchQuery, width=30, font=font, justify=tk.CENTER))
    youtubeImage = tk.PhotoImage(file="images/searchbox/youtubeicon.gif")
    searchScreen.create_image(400,175,image=youtubeImage)
    searchScreen.create_text(400,325,text="Tkinter Youtube Channel Browser",font=font, fill="white")
    searchScreen.create_window(720, 400, window= tk.Button(searchScreen, text="Go",command=root.destroy, font=smallFont))

    root.mainloop()
    return searchQuery.get()

def searchResultsUI(data={}):
    width = 500
    height = 600

    resultsNumber = data["pageInfo"]["resultsPerPage"]
    
    resultsHeight = height//resultsNumber
    resultsWidth = width

    imagedata = []
    root = tk.Tk()
    root.title("Results")
    window = tk.Canvas(root, width=width, height=height, bg='white')
    window.pack()

    for i in range(resultsNumber): # Generate search results
        # Relative x and y for (0,0) in mini-box
        y = i*resultsHeight
        x = 0

        # Result variables
        item = data["items"][i]
        thumburl = item["snippet"]["thumbnails"]["default"]["url"]

        window.create_rectangle(x,y,x+resultsWidth,y+resultsHeight, fill='grey' if i % 2 == 0 else 'white') #Draw frome

        # Request thumbnail
        imagedata.insert(i,ytrequests.requestTkImage(thumburl))
        
        print(x, y)
        print(thumburl)
        window.create_image(x+resultsWidth/5.5, y+resultsHeight/2, image=imagedata[i])
    
    
    root.mainloop()
