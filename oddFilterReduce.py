from functools import reduce 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd = list(filter(lambda x: x % 2 != 0, numbers ))
sum = reduce(lambda a, b: a + b, odd)

print(sum)