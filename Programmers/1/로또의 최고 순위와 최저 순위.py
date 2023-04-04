def solution(lottos, win_nums):
    ranking = [6, 6, 5, 4, 3, 2, 1]

    win_count = 0
    zero_count = 0

    for num in lottos:
        if num == 0:
            zero_count += 1
            continue

        if num in win_nums:
            win_count += 1

    max_draw = ranking[win_count + zero_count]
    min_draw = ranking[win_count]

    return [max_draw, min_draw]
