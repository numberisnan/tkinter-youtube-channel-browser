def readfile(location):
    "Reads a file and returns contents as string"
    with open(location, "r") as f:
        text = f.read()
    return text