from tkinter import *

# Search screen
def searchQueryDialogue():
    "Show search query dialogue and return what was entered"

    root = Tk()
    searchScreen = Canvas(root, width = 800, height = 600, bg = 'red')
    searchScreen.pack()

    searchQuery = StringVar()
    font = ("Consolas", "30")
    smallFont = ("Consolas", "19")

    serchbar = searchScreen.create_window(400, 400, window=Entry(searchScreen,fg = "grey", textvariable = searchQuery, width=30, font=font, justify=CENTER))
    youtubeImage = PhotoImage(file="images/searchbox/youtubeicon.gif")
    youtubeIcon = searchScreen.create_image(400,175,image=youtubeImage)
    title = searchScreen.create_text(400,325,text="Tkinter Youtube Channel Browser",font=font, fill="white")
    searchButton = searchScreen.create_window(720, 400, window= Button(searchScreen, text="Go",command=root.destroy, font=smallFont))

    root.mainloop()
    return searchQuery.get()
