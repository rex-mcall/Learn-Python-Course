people = 30
cars = 40
trucks = 15


if cars > people:
	print("We should take the cars.")
	
elif cars < people:
	print("We should not take the cars.")
	
else:
	print("We cannot decide.")
	
if trucks > cars:
	print("Thats too many trucks.")
if trucks < cars:
	print("Maybe we should take the trucks.")
else:
	print("We still cannot decide.")
	
if people > trucks:
	print("Alright, let's just take the trucks.")
else:
	print("You know what? Let's just stay home.")