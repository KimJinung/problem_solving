def solution(score):
    answer = []
    sum_of_each_student_score = list(map(lambda x: sum(x), score))
    sorted_score = sorted(sum_of_each_student_score, reverse=True)
    
    for sum_score in sum_of_each_student_score:
        idx = sorted_score.index(sum_score)
        
        answer.append(idx+1)
    
    return answer