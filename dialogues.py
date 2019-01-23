import tkinter

# Search screen
def searchQueryDialogue():
    "Show search query dialogue and return what was entered"

    root = tkinter.Tk()
    searchScreen = tkinter.Canvas(root, width = 800, height = 600, bg = 'red')
    searchScreen.pack()

    searchQuery = tkinter.StringVar()
    font = ("Consolas", "30")
    smallFont = ("Consolas", "19")

    searchScreen.create_window(400, 400, window=tkinter.Entry(searchScreen,fg = "grey", textvariable = searchQuery, width=30, font=font, justify=tkinter.CENTER))
    youtubeImage = tkinter.PhotoImage(file="images/searchbox/youtubeicon.gif")
    searchScreen.create_image(400,175,image=youtubeImage)
    searchScreen.create_text(400,325,text="Tkinter Youtube Channel Browser",font=font, fill="white")
    searchScreen.create_window(720, 400, window= tkinter.Button(searchScreen, text="Go",command=root.destroy, font=smallFont))

    root.mainloop()
    return searchQuery.get()
