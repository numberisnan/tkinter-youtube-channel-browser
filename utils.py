def readfile(location):
    textFile = open(location, "r")
    text = textFile.read()
    textFile.close()
    return text