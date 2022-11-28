def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        bin_value = bin(arr1[i] | arr2[i])[2:].rjust(n, "0")

        preprocessed_value = bin_value.replace("1", "#").replace("0", " ")

        answer.append(preprocessed_value)

    return answer
