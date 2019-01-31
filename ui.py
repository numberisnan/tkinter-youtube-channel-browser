import tkinter as tk
import ytrequests

# Search screen
def searchUI():
    "Show search query dialogue and return what was entered"
    width = 800
    height = 600

    root = tk.Tk()
    searchScreen = tk.Canvas(root, width =width, height =height, bg = 'red')
    searchScreen.pack()

    root.title("Youtube Channel Search")

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
    resultsNumber = data["pageInfo"]["resultsPerPage"] #Get number of results
    resultsHeight = height//resultsNumber
    
    root = tk.Tk()
    window = tk.Canvas(root, width=width, height=height, bg='white')
    window.pack()

    root.title("Results for " + )

    for i in range(resultsNumber):
        item = data["items"][i]

        # Add corrosponding results
        window.create_rectangle(0,i*resultsHeight,width,(i+1)*resultsHeight, fill='grey' if i % 2 == 0 else 'white') #Draw box

        # Request image url
        url = item["snippet"]["thumbnails"]["default"]["url"]
        ytrequests.downloadImage(url,"test.jpg")
    
    root.mainloop()
