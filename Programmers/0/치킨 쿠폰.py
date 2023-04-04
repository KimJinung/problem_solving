def solution(chicken):
    answer = 0
    coupon = chicken

    while coupon > 9:
        service_chicken_count = coupon // 10
        answer += service_chicken_count

        mod = coupon % 10
        coupon = service_chicken_count + mod

    return answer
