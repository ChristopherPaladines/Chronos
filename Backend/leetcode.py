"""
Chronos:
Chronos is a productivity desktop app used to assist users stay focused by restricting their access to unproductive applications that procrastinate and waste precious time.

step 1: Connecting Leetcode data to our code

1. Ask user for their username
2. Get their recent solves
3. Decide locked status vs unlocked
4. Tell the user


Step 2: Lock if no solve within X hours. time limit

step 3: Random problem picker.

step 4: Track how long a problem was worked on

"""


import requests # lets python send web requests aka Leetcode API call
import time # for using time.time() to get current time in seconds
from datetime import datetime # for turning timestamps into reable dates

Base_URL = "https://alfa-leetcode-api.onrender.com"
def welcome_chronos():
    print(f"Welcome to Chronos\n")
    print(f"Your personal productivity game changer\n")


def ask_username():
    username = input("Type your Leetcode username: ").strip() # strip removes accidental spaces
    print(f"Hello {username}!")
    return username # hands the username back to whoever calls this 

def fetch_accepted(username, limit=20):
    url = f"{Base_URL}/{username}/acSubmission?limit={limit}"
    response = requests.get(url, timeout=60)
    response.raise_for_status() # stops with an error if the servers says 404 etc
    data = response.json()
    return data.get("submission", []) #.get() method basically says, "give me this key, or an empty list if it it's not there"


def is_unlocked(submissions, window=3600):
    now = time.time()

    for sub in submissions:
        ts= int(sub["timestamp"]) # converting output timestamp to int
        print(sub["title"], datetime.fromtimestamp(ts))
        if now - ts <= window:
            return True
    return False
    
def main():
    welcome_chronos()

    username = ask_username() 
    subs = fetch_accepted(username)
    if is_unlocked(subs):
        print("Unlocked")
    else:
        print("Still locked. Go solve one")

if __name__ == "__main__":
    main()



