def solution(cacheSize, cities):
    answer = 0

    cache_dict = {}

    for idx, city in enumerate(cities):
        lowercase_city = city.lower()

        if cache_dict.get(lowercase_city) is not None:
            answer += 1
        else:
            answer += 5

        cache_dict[lowercase_city] = idx

        if len(cache_dict) > cacheSize:
            min_value_key = min(cache_dict, key=cache_dict.get)

            del cache_dict[min_value_key]

    return answer
