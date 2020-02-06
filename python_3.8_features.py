Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello",name := input("Enter your name : "))
Enter your name : Ravi
Hello Ravi
>>> name
'Ravi'
>>> while (msg := input("Enter msg : ")) != "bye":
	if msg == "hello":
		print("Hello user")
	elif msg == "bye":
		print("Bye user")
	else:
		print("Invalid msg")

		
Enter msg : hello
Hello user
Enter msg : hi
Invalid msg
Enter msg : bye
>>> 
