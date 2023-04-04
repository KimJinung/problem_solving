def solution(d, budget):
    answer = 0

    sorted_d = sorted(d)

    current_budget = 0

    for team_budget in sorted_d:
        if current_budget + team_budget <= budget:
            current_budget += team_budget
            answer += 1
        else:
            break

    return answer
