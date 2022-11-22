def solution(money):
    couple_of_tea = money // 5500

    return [couple_of_tea, money - 5500 * couple_of_tea]
