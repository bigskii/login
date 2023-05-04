from replit import db
import getpass
import time
reglog = int(input("Do you want to log in or register?\n[1] Register\n[2] Log in\nYour answer: "))
if reglog == 1:
	reguser = input("Set your username: ")
	regpasswd = getpass.getpass("Enter password: ")
	conpasswd = getpass.getpass("Confirm your password: ")
	if regpasswd != conpasswd:
		print("Passwords do not match.")
		exit()
	db[reguser] = regpasswd
	time.sleep(1)
	print("Thank you for registering and welcome to .")
	db[reguser,"logins"] = 0
elif reglog == 2:
	user = input('Enter your username: ')
	passwd = getpass.getpass('Enter your password: ')
	if db[user] == passwd:
		print("Welcome.")
		
		
	else:
		print("Incorrect password/username combination.")
		exit()

	