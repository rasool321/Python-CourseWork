email,pwd = 'xyz@gmail.com','xyz'
max_att = 3
while max_att>0:
    useremail,password = input().split()
    if useremail == email and password == pwd:
        print("Login successful!!")
        break
    else:
        print("Invalid reattempt!")
    max_att-=1
else:
    print("Try after sometime...")