try:
    username = input("Username: ")
    password = input("Password: ")
    if username != "admin":
        raise Exception
    print("Login Successful")
except Exception:
    print("Invalid Username ,enter the correct the username")
