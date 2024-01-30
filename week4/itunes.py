import json
import requests
import sys  # Ability to use command-line arguments

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term" + sys.argv[1])

o = response.json()
for each result in o["results"]:
    print(result["trackName"])
