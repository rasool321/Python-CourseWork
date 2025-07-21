# Correct credentials
correct_username = "admin"
correct_password = "1234"

# Maximum login attempts
attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful!!")
        break
    else:
        attempts -= 1
        print(f"Incorrect credentials. Attempts left: {attempts}")

else:
    print("Too many failed attempts. Access blocked.")