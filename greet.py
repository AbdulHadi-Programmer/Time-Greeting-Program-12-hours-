name = input("Enter Your Name: ").title()
time = int(input("\nEnter Present Time: "))
DN = input("Enter AM or PM: ").upper()

def greeting():
	if ( time >= 1 and time <= 6 and DN == "AM" or time > 6 and time <= 11 and DN == "PM" ):
		print("\nGood Night ", name)
		
	elif ( time > 6 and time <= 11 and DN == "AM" ) :
		print("\nGood Morning ", name)
		
	elif (time >= 1 and time <= 6 and DN == "PM"):
		print("\nGood Afternoon ", name)
		
	elif ( time == 12 and DN == "AM" ):
		print("\nGood Night ", name)
		
	elif ( time == 12 and DN == "PM"):
		print("\nGood Afternoon", name)
		
	else:
		print("Invalid input")
greeting()
