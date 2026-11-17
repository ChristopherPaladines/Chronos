
# Chronos

Chronos is a focus tool that blocks distracting apps until you solve a LeetCode problem. Start a session, and any app on your blocklist gets closed as soon as it opens. Once you submit an accepted LeetCode solution, the session ends and your apps are unlocked.

**Current status:** In progress. The core blocking and unlock loop works from the command line. The GUI is under development.

# How it works

- Enter your LeetCode username to start a session.
- Every 3 seconds, Chronos checks running processes (using `psutil`) and closes anything on your blocklist.
- Every 3 minutes, it checks your recent accepted LeetCode submissions through the community [alfa-leetcode-api](https://github.com/alfaarghya/alfa-leetcode-api). The slower interval keeps it from hitting the API's rate limits.
- When it finds an accepted submission newer than the session start time, it unlocks your apps and ends the session.

If LeetCode can't be reached, Chronos stays locked and tries again on the next check.

#  Requirements

Python 3 and a public LeetCode profile.

# Setup

```bash
git clone https://github.com/ChristopherPaladines/Chronos.git
cd Chronos
pip install -r requirements.txt
```

Edit `blocked_apps.txt` to list the apps you want blocked, one per line. Names aren't case-sensitive, and `.exe` is optional:

```
Discord
Steam
CrunchyRoll
```

Run the session file from the repo root so Chronos can find `blocked_apps.txt`:

```bash
python Backend/session.py
```

Press `Ctrl+C` to end a session early.

## Features left to add

- [ ] Desktop GUI
- [ ] Dashboard showing the last problem solved
- [ ] Configurable number of solves to unlock (alternative)
- [ ] Streak tracking, with early exits logged on the dashboard (maybe)
- [ ] Notes field to fill in after each solved problem (maybe)
- [ ] AI-assisted check for whether an open app is productive
