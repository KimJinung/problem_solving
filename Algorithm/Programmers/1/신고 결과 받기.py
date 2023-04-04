def solution(id_list, report, k):
    answer = [0] * len(id_list)

    report_dict = {user: 0 for user in id_list}

    unique_report = set(report)

    for claim in unique_report:
        reported_user = claim.split()[1]

        report_dict[reported_user] += 1

    for claim in unique_report:
        user, report = claim.split()

        if report_dict[report] >= k:
            answer[id_list.index(user)] += 1

    return answer
