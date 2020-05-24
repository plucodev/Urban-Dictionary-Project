import requests, os, sys

# Retrieve your API credentials from the .env file
if os.getenv("API_KEY") is None or os.getenv("API_KEY") == "":
    print("ERROR Make sure you have created your .env file with your API credentials (look for the .evn.example as an example and replace it with your own API credentials that you got from RapidAPI)")
    exit(1)

# Get credentials from the .env file
API_HOST = os.getenv("API_HOST")
API_KEY = os.getenv("API_KEY")

# continue with your application here
import requests
# word = ""
# if len(sys.argv) ==1:
#     word = input("What term do you want to look for?")
# else:
#     word = sys.argv[1]
url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define" 
print("****", len(sys.argv))
querystring = {"term":"car"}

headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "b110728a3amsh7b576f78b098297p1905c1jsnecb143f82a7d"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())