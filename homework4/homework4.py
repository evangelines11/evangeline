# 3.1 List Operations

foods = ["tofu", "poke", "acai", "innout", "yogurt"]
print(foods[1])
print(foods[-1])
foods.append("fruit")
foods.insert(0, "apple")
foods.remove("acai")
print(len(foods))

for food in foods:
	print(food.upper())

new_foods = foods[:: len(foods) - 1]
print(new_foods)

if "potato" in new_foods:
	print("A potato!")
else:
	print("No potato!")

# 3.2 Slicing and Striding

numbers = list(range(0, 21))

def get_first_15(numbers):
	return numbers[:15]

def get_every_5th(lst):
	return lst[::5]
	
def reverse_and_stride(lst):
	reversed_lst = lst[::-1]
	return reversed_lst[::3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

print(step3)

# 3.3 Nested Lists

numbers = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

# third row
print(numbers[2])

# second item in second row
print(numbers[1][1])

numbers.append([10, 11, 12])
print(numbers)

def sum_nested(nested_list):
	total = 0
	for row in nested_list:
		for num in row:
			total += num
	return total

print(sum_nested(numbers))

# 3.4 Create a 5x5 List

def new_list():
	grid = []
	counter = 1
	for i in range(5):
		row = []
		for j in range(5):
			row.append(counter)
			counter += 1
		grid.append(row)
	return grid

original_grid = new_list()

def multiples_of_three(grid):
	new_grid = []
	for row in grid:
		new_row = []
		for item in row:
			if item % 3 == 0:
				new_row.append("?")
			else:
				new_row.append(item)
		new_grid.append(new_row)
	return new_grid

updated_list = multiples_of_three(original_grid)

def not_equal(grid):
	total_sum = 0
	for row in grid:
		for item in row:
			if item != "?":
				total_sum += item
	return total_sum

final_sum = not_equal(updated_list)

# 4 Dictionaries

ages = {
	"Katie": 30,
	"Mariam": 42,
	"Safia": 25,
	"Mira": 48
}

print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = "52"
del ages["Mariam"]

for name, age in ages.items():
	print(f"{name}: {age}")

# 5.2 Favorite Function
foods = ["tofu", "poke", "acai", "innout", "yogurt"]
print(foods[1])