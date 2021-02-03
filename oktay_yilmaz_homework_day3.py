#Question 1
user_name = "oktay"
password ="oktay123"
user_name1 =input("Please enter your user name: ")
password1= input("Please enter your password: ")
if (user_name != user_name1 and password == password1):
    print("Invalid user name")
elif (user_name==user_name1 and password != password1):
    print("Invalid Password")
elif (user_name != user_name1 and password!= password1):
    print("Invalid user name and password")
else:
    print("You are now logged in...")

#Question 1 (Extra using with dictionary)
users = {"user_name":"oktay", "password":"oktay123"}
#print(users)
user_name1 =input("Please enter your user name: ")
password1= input("Please enter your password: ")
if (users.get("user_name") != user_name1 and users.get("password") == password1):
    print("Invalid user name")
elif (users.get("user_name")==user_name1 and users.get("password") != password1):
    print("Invalid Password")
elif (users.get("user_name") != user_name1 and users.get("password")!= password1):
    print("Invalid user name and password")
else:
    print("You are now logged in...")

