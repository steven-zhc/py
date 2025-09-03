arr = [1, 2, 3, 4, 5]
arr.append(6)
print(arr)

squares = [x**2 for x in arr]
print(squares)

filtered = [x for x in arr if x > 2]
print(filtered)


# slicing
