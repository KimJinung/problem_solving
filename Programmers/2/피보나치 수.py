def solution(n):
    fibonacci = [0, 1]

    for num in range(2, n + 1):
        fibonacci.append(fibonacci[num - 1] + fibonacci[num - 2])

    return fibonacci[n] % 1234567
