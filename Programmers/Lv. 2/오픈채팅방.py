def solution(record):
    answer = []

    users = {}

    for rcd in record:
        log = rcd.split()

        action = log[0]

        if action in ["Enter", "Change"]:
            uid = log[1]
            nickname = log[2]

            users[uid] = nickname

    for rcd in record:
        log = rcd.split()

        action = log[0]
        nickname = users[log[1]]

        if action == "Enter":
            msg = f"{nickname}님이 들어왔습니다."
        elif action == "Leave":
            msg = f"{nickname}님이 나갔습니다."
        else:
            continue

        answer.append(msg)

    return answer
