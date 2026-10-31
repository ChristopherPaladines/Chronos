import requests # lets python send web requests

Base_URL = "ttps://alfa-leetcode-api.onrender.com/{username}/acSubmission?limit=20"

def ask_username():
    username = input("Type your Leetcode username: ").strip() # strip removes accidental spaces
    print(f"Hello {username}!")
    return username # hands the username back to whoever calls this 

def fetch_accepted(username, limit=20):
    url = f"{Base_URL}/{username}/acSubmission?limit={limit}"
    response = requests.get(url, timeout=60)
    response.raise_for_status() # stops with an error if the servers says 404 etc
    data = response.json()
    return data.get("submission, []") #.get() method basically says, "give me this key, or an empty list if it it's not there"

username = ask_username()

for sub in fetch_accepted(username):
    print(sub["title"], sub["timestamp"])

