import time

password = input("What is the password? ")

while password not in ["Open Sesame"]: 
	print()
	print("That is not the password, try again.")
	print()
	time.sleep(1)
	password = input("What is the password? ")

print()
print("That's the password, welcome!")