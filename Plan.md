# Project Enforcer: LeetCode Productivity Lock

## 1. System Ecosystem & Data Flow
This application acts as a bridge between the local operating system, a local database, a web user interface, and the external LeetCode platform.

[ User UI Input ] ---> [ Flask Server ] ---> [ OS Process Monitor (Enforcer) ]
                              |
                              +---------> [ Local Database (State/History) ]
                              |
                              +---------> [ Unofficial LeetCode API ]

## 2. Object-Oriented Programming (OOP) Design

### Class: UserProfile
*This object holds the configuration and identity of the person using the software.*
* **Attributes (What it knows):**
  * `leetcode_username` (String): The target public handle to query.
  * `current_problem` (String): The problem currently assigned (Defaults to "Two Sum").
  * `is_locked` (Boolean): Flag tracking if the system is currently enforcing productivity mode.
* **Methods (What it does):**
  * `load_profile()`: Reads saved configuration data from the local storage.
  * `update_current_problem(problem_name)`: Changes the active target goal.

### Class: SystemEnforcer
*This object interacts directly with the computer's operating system to monitor and close apps.*
* **Attributes (What it knows):**
  * `blacklisted_keywords` (List of Strings): Low-hanging fruit apps (e.g., "spotify", "steam", "netflix").
* **Methods (What it does):**
  * `get_running_processes()`: Queries the OS for a list of all active application names.
  * `analyze_productivity(process_name)`: Uses a local rule engine (or AI classifier) to determine if an unknown app is distracting.
  * `terminate_process(process_id)`: Forces a distracting application to close immediately.

### Class: LeetCodeTracker
*The engine responsible for verifying real-world progress without requiring user login.*
* **Attributes (What it knows):**
  * `api_base_url` (String): The connection endpoint for the community API.
* **Methods (What it does):**
  * `fetch_recent_activity(username)`: Hits the external API to get the last 20 submissions.
  * `verify_status(username, problem_name)`: Scans the submission list. Returns `True` only if the target problem status is "Accepted".

## 3. Core Logic & Workflow (Step-by-Step)
1. **Startup:** Flask web server starts and automatically launches a local browser window to the landing page.
2. **State Check:** Flask reads the database. If it's a new user, it sets `current_problem` to "Two Sum". If it's a returning user, it displays their last unfinished problem.
3. **Lockdown Phase:** The script flips `UserProfile.is_locked` to `True`. A background loop triggers every 5 seconds, running `SystemEnforcer`. Any application matching the distraction criteria is killed.
4. **Verification Phase:** The user clicks "Completed Problem" on the Flask UI page.
5. **API Check:** `LeetCodeTracker` queries the public profile. 
   * *If verified:* `is_locked` becomes `False`, app termination loops stop, and the database updates the problem as completed.
   * *If not verified:* The UI displays an error message ("Nice try! Problem not completed yet.") and the lock remains active.

## 4. Critical Design Challenges & Loopholes
* **The 5-Minute Window Loophole:** If the background loop only runs on a timer, a user can open a game, play for 4 seconds, close it, and repeat. 
  * *Tweak:* Instead of a sleeping timer, look into OS event-driven monitoring (like `psutil` callbacks) that flags apps the exact millisecond they launch.
* **The AI Classification Cost/Speed:** Querying a cloud-based AI classifier every 5 seconds for every running background process will be incredibly slow and expensive.
  * *Tweak:* Use a strict local text-match file first (the "Always Block" list). Only pass completely *new* or unrecognized process names to your classifier system, and remember/save the AI's answer locally so you never have to ask about the same app twice.
