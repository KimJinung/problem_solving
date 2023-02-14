def solution(sticker):
    return max(dp(sticker[:-1]), dp(sticker[1:]))


def dp(sticker: list) -> int:
    size = len(sticker)

    dp = [0 for _ in range(size)]
    dp[0] = sticker[0]

    for idx in range(1, size):
        if idx == 1:
            dp[idx] = max(sticker[0], sticker[1])
        else:
            dp[idx] = max(dp[idx - 1], sticker[idx] + dp[idx - 2])

    return dp[-1]
