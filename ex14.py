from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask some questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live, {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} to liking me.
You live in {lives}. Not sure where that is... estimated 00:23:00 till gps location lock.
And you have a {computer}. Nice.
""")