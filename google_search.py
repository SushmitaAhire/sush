from googlesearch import search

query = 'how old is samuel l jackson'

## Google Search query results as a Python List of URLs
search_result_list = list(search(query, tld="co.in", num=10, stop=3, pause=1))
