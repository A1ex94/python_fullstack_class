list = [1, 2, 3, 4, 5]
numbers = [str(i) for i in list[list[0]:list[-1]:list[1]]]
print(f"Числа подсписка: {', '.join(numbers)}")