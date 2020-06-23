name = 'Rex McAllister'
age = 14 #years old
height = 67 #inches
weight = 119 #pounds
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'
new_height = height * 2.54 #height in centimeters

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall, or about {round(new_height)} centimeters tall.")
print(f"He's {weight} pounds heavy.")
print("Actually, that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending or not he just ate an Oreo.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")