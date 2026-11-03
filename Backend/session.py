import time
import requests
from app import ask_username, fetch_accepted       # your LeetCode code (its main() does NOT run on import)
from enforcer import load_blocked_apps, close_apps  # your app-closing code

CHECK_APPS_EVERY = 3        # seconds between closing blocked apps (fast)
CHECK_LEETCODE_EVERY = 180  # seconds between LeetCode checks (slow, so we don't hit the rate limit)


def solved_since(submissions, start_time):
    # True if any accepted solve happened AFTER the session started
    for sub in submissions:
        if int(sub["timestamp"]) > start_time:
            return True
    return False


def run_session():
    username = ask_username()
    blocked = load_blocked_apps()  # read ONCE, so editing the file mid-session doesn't unlock anything
    start_time = time.time()
    last_leetcode_check = 0        # 0 = "never checked yet", so the first check happens right away

    print("Session started. Blocking:", blocked)
    print("Solve one LeetCode problem to unlock. (Ctrl+C to quit early)")

    while True:  # keep going until we hit "break"
        # job 1: close any blocked app that got opened
        closed = close_apps(blocked)
        if len(closed) > 0:
            print("Closed:", closed)

        # job 2: every few minutes, ask LeetCode if they've solved something
        seconds_since_check = time.time() - last_leetcode_check
        if seconds_since_check >= CHECK_LEETCODE_EVERY:
            last_leetcode_check = time.time()
            try:
                subs = fetch_accepted(username)
                if solved_since(subs, start_time):
                    print("Solved one! Apps unlocked. Nice work.")
                    break  # exit the while loop = session over
                print("No new solve yet. Checking again in a few minutes.")
            except requests.RequestException:
                print("Couldn't reach LeetCode. Staying locked, will try again.")

        time.sleep(CHECK_APPS_EVERY)  # pause so we don't max out the CPU


if __name__ == "__main__":
    run_session()