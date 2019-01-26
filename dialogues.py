import tkinter as tk

# Search screen
def searchQueryDialogue():
    "Show search query dialogue and return what was entered"

    root = tk.Tk()
    searchScreen = tk.Canvas(root, width = 800, height = 600, bg = 'red')
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
