dot_dict = {
    1: (0, 0),
    2: (1, 0),
    3: (2, 0),
    4: (0, 1),
    5: (1, 1),
    6: (2, 1),
    7: (0, 2),
    8: (1, 2),
    9: (2, 2),
    0: (1, 3),
    "*": (0, 3),
    "#": (2, 3),
}


def solution(numbers, hand):
    answer = ""

    current_left_hand = "*"
    current_right_hand = "#"

    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"

            current_left_hand = num

        elif num in [3, 6, 9]:
            answer += "R"

            current_right_hand = num

        else:
            distance_from_left_hand = get_distance(current_left_hand, num)
            distance_from_right_hand = get_distance(current_right_hand, num)

            if distance_from_left_hand == distance_from_right_hand:
                if hand == "right":
                    distance_from_right_hand -= 1
                else:
                    distance_from_left_hand -= 1

            if distance_from_left_hand < distance_from_right_hand:
                answer += "L"

                current_left_hand = num

            elif distance_from_left_hand > distance_from_right_hand:
                answer += "R"

                current_right_hand = num

    return answer


def get_distance(current_hand_position, target: int) -> int:
    X = abs(dot_dict[current_hand_position][0] - dot_dict[target][0])
    Y = abs(dot_dict[current_hand_position][1] - dot_dict[target][1])

    return X + Y
