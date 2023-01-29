'''Exercise 2 : Giphy API #1
Instruction
Hint: For this exercise, check out the documentation of the Giphy API

You will work with this part of the documention

You will use this Gif URL: https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My
Explanation of the Gif URL

q Request Paramater: Search query term or phrase. We are searching for “hilarious” gifs

rating Request Paramater: Filters results by specified rating. We are searching for Level 1 gifs. Check out the ratings documentation

api_key Request Paramater : GIPHY API Key. Our API KEY is hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My
Fetch the giphs from the Gif URL provided above.

Use f-strings and variables to build the URL string we’re using for the fetch.
If the status code is 200 return the result as a JSON object.
Only return gifs which have a height bigger then 100.
Return the length of the object you received in the previous question.
Only return the first 10 gifs. Hint: In the Giphy Documentation, check out the relevant Request Parameters.'''
import json
import requests
from urllib import parse, request
#
# response = requests.get("https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My")
#
# if response.status_code == 200:
#     with open('gyphyobject.json', 'w') as f:
#         print(f"{response.status_code}. JSON file created.")
#
# for line in response:
#     print(line)
#

def giphy_query():

    url = "http://api.giphy.com/v1/gifs/search"
    query_theme = str(input("Please choose the theme for your search: "))
    params = parse.urlencode({
      "q": query_theme,
      "rating": "g",
      "fixed_height": 200,
      "api_key": "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My",
      "limit": "10"
    })

    with request.urlopen("".join((url, "?", params))) as response:
        newurl = "".join((url, "?", params))
        data = json.loads(response.read())
        print(len(data))
        print(newurl)

    with open('gyphyobject.json', 'w') as f:
      json.dump(data, f, indent=4)

giphy_query()