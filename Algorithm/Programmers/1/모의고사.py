def solution(answers):
    score_list = []

    length = len(answers)

    first_student = [1, 2, 3, 4, 5]
    second_student = [2, 1, 2, 3, 2, 4, 2, 5]
    third_student = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for student in [first_student, second_student, third_student]:
        result = mark(answers, student)

        score_list.append(result)

    highest_score = max(score_list)

    return [idx + 1 for idx in range(3) if score_list[idx] == highest_score]


def mark(answers, student_answer) -> int:
    result = 0
    length_of_student_answer = len(student_answer)

    for i in range(len(answers)):
        if answers[i] == student_answer[i % length_of_student_answer]:
            result += 1

    return result
