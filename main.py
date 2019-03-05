import ui, ytrequests, utils

query = ui.searchUI()

apikey = utils.readfile("apikey.key")

searchResults = ytrequests.youtubeSearchRequest(query, apikey=apikey, maxResults=4)

ui.searchResultsUI(searchResults)

