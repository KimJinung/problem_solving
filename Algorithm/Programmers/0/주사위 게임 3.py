from collections import Counter


def solution(a: int, b: int, c: int, d: int):
    dice_counter = Counter([a, b, c, d])

    size = len(dice_counter)

    if size == 1:
        return int(str(a) * 4)
    elif size == 2:
        p, q = sorted(dice_counter.keys(), key=lambda x: -dice_counter[x])

        if dice_counter[p] == 2:
            return (p + q) * abs(p - q)
        else:
            return (10 * p + q) ** 2
    elif size == 3:
        q, r = "", ""

        for dice_num, cnt in dice_counter.items():
            if cnt != 2:
                if q == "":
                    q = dice_num
                else:
                    r = dice_num

        return q * r
    else:
        return min(a, b, c, d)
