def solution(n):
    dp = [1, 1]

    for i in range(2, n + 1):
        number_of_case = dp[i - 2] + dp[i - 1]

        dp.append(number_of_case)

    return dp[n] % 1234567
