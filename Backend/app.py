from leetcode import todays_submissions, solved_today

username = input("Enter your Leetcode username:")

# returns message stating problem detected solved or not
print(solved_today(username))

# returns an array of todays solved problems to be displayed
print(todays_submissions(username))