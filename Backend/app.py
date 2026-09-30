# Chronos Welcome Screen
def welcome_chronos():
    print(f"Welcome to Chronos\n")
    print(f"Your personal productivity game changer\n")

   
# User writes their username.

def user_name(): # This function stores the usernames
    print(f"Please enter your Leetcode Username.")
    LC_username = input()
    return LC_username



welcome_chronos() # welcome call

print("Program will say: ",user_name()) #user_name call



