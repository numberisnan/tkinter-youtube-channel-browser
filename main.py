import ui
import ytrequests
import utils

query = ui.searchUI()

apikey = utils.readfile("apikey.key")

searchResults = ytrequests.youtubeSearchRequest(query, apikey=apikey, maxResults=3)

ui.searchResultsUI(searchResults)

