value1 = int(input())
value2 = input()

result = [val * value1 for val in list(map(int, value2))[::-1]]

result.append(value1 * int(value2))


for num in result:
    print(num)
