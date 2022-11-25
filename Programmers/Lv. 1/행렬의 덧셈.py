def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        subset = []

        for j in range(len(arr1[0])):
            subset.append(arr1[i][j] + arr2[i][j])

        answer.append(subset)

    return answer
