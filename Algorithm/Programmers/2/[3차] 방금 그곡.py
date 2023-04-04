import re
from datetime import datetime


def solution(m, musicinfos):
    result = []

    memory_of_neo = re.findall("\w#?", m)

    for idx, info in enumerate(musicinfos):
        start_time, end_time, title, sample_music_paper = info.split(",")

        playtime = get_play_time(start_time, end_time)

        sample_music_paper = get_padded_music_paper(playtime, sample_music_paper)

        if is_valid_music_paper(memory_of_neo, sample_music_paper):
            result.append((idx, playtime, title))

    if result:
        result.sort(key=lambda x: (x[1], -x[0]), reverse=True)

        title = result[0][-1]

        return title

    return "(None)"


def is_valid_music_paper(memory_of_neo: list, sample_music_paper: list) -> bool:
    candidate_idx = []

    start_note = memory_of_neo[0]

    size_of_memory = len(memory_of_neo)

    for idx, note in enumerate(sample_music_paper):
        if note == start_note:
            candidate_idx.append(idx)

    for idx in candidate_idx:
        if sample_music_paper[idx : idx + size_of_memory] == memory_of_neo:
            return True

    return False


def get_padded_music_paper(size: int, sample_music_paper: str) -> list:
    music_paper = re.findall("\w#?", sample_music_paper)

    length_of_music_paper = len(music_paper)

    if length_of_music_paper > size:
        return music_paper[:size]

    for i in range(length_of_music_paper, size):
        idx = i % length_of_music_paper

        music_paper.append(music_paper[idx])

    return music_paper


def get_play_time(start_time: str, end_time: str) -> int:
    st = datetime.strptime(start_time, "%H:%M")
    ed = datetime.strptime(end_time, "%H:%M")

    return int((ed - st).total_seconds() // 60)
