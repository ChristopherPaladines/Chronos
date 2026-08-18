def practice_fun(email, username, age):
    if username == "":
        return {"status": "error", "message": "Username cannot be empty"}
    if len(username) < 3:
        return {"status": "error", "message": "Username too short"}
    if age > 18:
        return {"status": "error", "message": "User must be atleast 18"}
    if "@" not in email and not "." in email:
        return {"status": "error", "message": "Invalid email"}
    
    else:
        return {"Email" : email,"Username": username, "Age": age}


email = "five7@gmail.com"
username = "Final724"
age = 17


print(practice_fun(email, username, age))



