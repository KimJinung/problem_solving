def solution(n, words):
    prev_word = words[0]
    used_words = {prev_word: True}

    loser = -1

    for idx, word in enumerate(words[1:]):
        if prev_word[-1] != word[0]:
            loser = idx + 1
            break

        if used_words.get(word):
            loser = idx + 1
            break
        else:
            used_words[word] = True

            prev_word = word
    else:
        return [0, 0]

    return [loser % n + 1, loser // n + 1]
