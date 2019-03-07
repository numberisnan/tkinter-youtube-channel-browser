import ui, ytrequests, utils

query = ui.searchUI() # Open the search UI and store query

apikey = utils.readfile("apikey.key")

searchResults = ytrequests.youtubeSearchRequest(query, apikey=apikey, maxResults=4) # Send query to youtube.com and store results

ui.searchResultsUI(searchResults) # Open searchresults window

