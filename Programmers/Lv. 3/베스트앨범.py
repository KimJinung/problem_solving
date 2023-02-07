from collections import defaultdict


def solution(genres, plays):
    answer = []

    genre_total_play_chart = defaultdict(int)
    genre_detail_chart = defaultdict(list)

    for idx, genre in enumerate(genres):
        genre_total_play_chart[genre] += plays[idx]

        genre_detail_chart[genre].append((plays[idx], idx))

    top_genres = sorted(
        genre_total_play_chart.items(), key=lambda x: x[1], reverse=True
    )

    for genre, _ in top_genres:
        rank = sorted(genre_detail_chart[genre], key=lambda x: (-x[0], x[1]))

        for _, uid in rank[:2]:
            answer.append(uid)

    return answer
