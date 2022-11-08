def solution(food):
    answer = ''
    subset_of_answer = ''

    for i in range(1, len(food)):
        count_of_food = food[i] // 2
        
        if count_of_food > 0:
            subset_of_answer += str(i) * count_of_food
    
    answer = subset_of_answer + '0' + subset_of_answer[::-1]
    return answer
