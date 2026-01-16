n = int(input())
stack = []

for i in range(n):
    number = int(input())

    if number == 0:
        stack.pop()

    else:
        stack.append(number)


result = 0
for i in stack:
    result += i

print(result)