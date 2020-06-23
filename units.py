#Simple practice of skills so far, basic units conversion program.

conversion = input('Type the input unit, followed by "to", then the output unit.  > ')
input_number = input('Please type the input number (Do not include any units!).  > ')

def in_cm(number):
	number = number * 2.54
	print(number)
	
def cm_in(number):
	number = number / 2.54
	print(number)
	
if conversion == "Inch to Centimeter":
	in_cm(input_number)
	
elif conversion == "Centimeter to Inch":
	cm_in(input_number)
else:
	print("Error 214")