def solution(spell, dic):
    spell.sort()

    for word in dic:
        word_list = sorted(list(word))

        if spell == word_list:
            return 1

    return 2
