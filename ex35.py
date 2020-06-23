from sys import exit

def gold_room():
	print("This room is full of gold. How much do you take?")
	
	choice = input('> ')
	if '0' in choice or '1' in choice:
		how_much = int(choice)
	else:
		dead("Man, learn how to type a number.")
	if how_much < 50:
		print("Nice, you're not greedy, you win!")
		exit(0)
	else:
		print("You greedy bastard!")
		
		
def bear_room():
	print("There is a bear here.\nThe bear has a bunch of honey.\nThe fat bear is in front of a door.\nHow are you going to move the bear?\n(Hint: Kill or be killed)")
	choice = input("> ")
	if "kill" in choice:
		print("The bear is now dead and you can go through the door. You open the door and find that...")
		gold_room()
	else:
		dead("You died because you did not take my advice and kill the bear.")

		
def cthulu_room():
	print("Here you see the great evil Cthulu.")
	print("He, it, whatever, stares at you and you go insane.")
	print("Do you flee for your life or eat your own head?")
	
	choice = input('> ')
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well, that was tasty!")
	else:
		cthulu_room()
def dead(why):
	print(why, "Good Job!")
	exit(0)
	
def start():
	print("You are in a dark room.")
	print("There is a door to your left and a door to your right.")
	print("Which do you choose?")
	
	choice = input("> ")
	
	if choice == "left":
		bear_room()
	if choice == "right":
		cthulu_room()
	else:
		dead("You stumble around the room until you starve.")
		
start()