def readfile(location):
    "Reads a file and returns contents as string"
    textFile = open(location, "r")
    text = textFile.read()
    textFile.close()
    return text