"""
1. 차 번호마다 입출차 시각을 리스트에 전부 추가 해준다.
2. 두 번 이상 입차하는 경우 등은 없으므로, 리스트의 개수를 체크해서 홀수면 23:59를 추가해준다.
3. 각 입출차에 대한 계산이 아니라 총 누적시간으로 요금을 계산한다.
"""

import math

from datetime import datetime
from collections import defaultdict


def solution(fees, records):
    answer = []

    fee_dict = defaultdict(list)

    # 1. 각 차량마다 입출차 기록 딕셔너리 생성
    for record in records:
        t, car_number, detail = record.split()

        fee_dict[car_number].append(t)

    # 2. 마지막 출차 기록이 없는 케이스 후처리
    for key, value in fee_dict.items():
        if len(value) % 2 != 0:
            fee_dict[key].append("23:59")

    # 3. 총 누적 시간으로 요금 계산
    for car_number, history in fee_dict.items():
        accumlated_time = get_total_minutes_from_history(history)

        fee = calcul_fee(fees[0], fees[1], fees[2], fees[3], accumlated_time)

        answer.append((car_number, fee))

    answer.sort(key=lambda x: x[0])

    return [fee for _, fee in answer]


def calcul_fee(default_time, default_fee, term, term_fee, accumlated_time) -> int:
    if accumlated_time <= default_time:
        return default_fee

    return default_fee + math.ceil((accumlated_time - default_time) / term) * term_fee


def get_total_minutes_from_history(times: list) -> int:
    minutes = 0

    size = len(times) - 1

    for i in range(size, -1, -2):
        minutes += calcul_time(times[i - 1], times[i])

    return minutes


def calcul_time(start_time: str, end_time: str) -> int:
    st = datetime.strptime(start_time, "%H:%M")
    ed = datetime.strptime(end_time, "%H:%M")

    return int((ed - st).total_seconds() / 60)
