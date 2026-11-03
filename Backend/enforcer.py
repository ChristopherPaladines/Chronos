import psutil  # lists and closes running programs; same code works on Mac and Windows


def normalize(name):
    # make names match no matter the device: "Discord.exe" and "DISCORD" both become "discord"
    name = name.lower()            # all lowercase
    if name.endswith(".exe"):      # Windows adds .exe, Mac doesn't
        name = name[:-4]           # chop off the last 4 characters (".exe")
    return name


def find_running(app_names):
    # step 1: clean up the banned names
    targets = []
    for n in app_names:
        targets.append(normalize(n))

    # step 2: check every running program against the banned list
    found = []
    for proc in psutil.process_iter(["name"]):  # psutil hands us each running program, one at a time
        name = proc.info["name"]                # that program's name, like "Discord"
        if name is None:                        # some system processes have no name, so skip them
            continue
        if normalize(name) in targets:          # THE FILTER: is it on the banned list?
            found.append(proc)                  # yes, grab it

    # step 3: hand back everything we grabbed
    return found


def close_apps(app_names):
    closed = []
    for proc in find_running(app_names):
        try:
            proc.terminate()                # politely ask it to quit, like clicking the X
            closed.append(proc.info["name"])
        except psutil.NoSuchProcess:        # it already quit on its own
            pass
        except psutil.AccessDenied:         # the computer won't let us close it
            pass
    return closed


def load_blocked_apps(path="blocked_apps.txt"):
    apps = []
    with open(path) as file:        # open the file; "with" closes it for us when we're done
        for line in file:           # read it one line at a time
            line = line.strip()     # remove extra spaces and the invisible "new line" character
            if line == "":          # skip blank lines
                continue
            apps.append(line)
    return apps


if __name__ == "__main__":
    blocked = load_blocked_apps()
    print("Blocking:", blocked)
    print("Closed:", close_apps(blocked))