# nums = [1, 2, 3, 4, 5]

# squares = [x*x for x in nums]
# even_numbers = [x for x in nums if x % 2 == 0]
# print(squares)
# print(even_numbers)

# name = "Diwakar"

# upper_letters = [char.upper() for char in name]
# print(upper_letters)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# flattened = [num for row in matrix for num in row]
# print(flattened)

transpose = [[row[i] for row in matrix] for i in range(3)]
print(transpose)