# 3.1 Say Goodbye
def say_goodbye(name):
	name = "Evangeline"
	print("Goodbye,", name)
say_goodbye("Evangeline")
# 3.2 Area of a Circle
def area_circle(radius):
pi = 3.14
radius = 4
area = pi * (radius ** 2)
print(area)

# 4.1 Subtract, Multiply, and Divide
def subtract(a, b):
	return a-b
print(subtract(6, 4))
def multiply(a, b):
	return a*b
print(multiply(6, 4))
def divide(a, b):
	return a/b
print(divide(6, 4))

# 5.1 What Should I Wear?
def high_low_temps(temps):
	return (min(temps), max(temps))
print (high_low_temps([64, 81, 75, 68, 79, 96, 84]))

# 5.2 Check if it's the Weekend
def is_weekend(day):
	if day == 6 or day == 7:
		return True
	else:
		return False
print(is_weekend(1))

# 5.3 Fuel Efficiency Calculator
def fuel_efficiency(distance, fuel_used):
# calculates car fuel efficiency in miles per gallon
	return distance / fuel_used
print(fuel_efficiency(10, 1))

# 5.4 Secret Code
def encrypt_data(num):
	return num
num = 12345
last_digit = num % 10
remaining = num // 10
print (encrypt_data(12345))

# 6.1 Oski Stole Your Power
def power(x, y):
	result = 1
	for i in range (y):
		result *= x
	return result

# 6.2.1 For Loops
def minimum(numbers):
	numbers = [1, 2, 3, 4, 5, 6]
	min_num = numbers [0]
for i in numbers:
	if i < min_num:
		min = i
return min_num

def maximum(numbers):
	max_num = numbers[0]
for i in numbers:
	if i > max_num:
		max_num = i
	return max_num

# 6.2.2 While Loops
def min_while(numbers):
	numbers: [1, 2, 3, 4, 5, 6]
min_num = numbers[0]
i = 0
# Got confused.
# Favorite Function

def high_low_temps(temps):
	temps = [64, 81, 75, 68, 79, 96, 84]
	return (min(temps), max(temps))
print (high_low_temps("The result of what should I wear 5.1 with temps 64, 81, 75, 68, 79, 96, 84, is" temps))



