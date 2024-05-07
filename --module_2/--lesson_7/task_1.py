line = 'Hello World'
line_2 = line.split()
reverse = []
for word in line_2: reverse.append(word[::-1])
print(reverse)