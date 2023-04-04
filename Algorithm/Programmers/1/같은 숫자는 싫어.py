def solution(arr):
    answer = [arr[0]]

    for item in arr[1:]:
        last = answer[-1]

        if item == last:
            continue

        answer.append(item)

    return answer
