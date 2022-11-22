def solution(box, n):
    box = list(map(lambda x: x // n, box))

    col = box[0]
    row = box[1]
    height = box[2]

    return col * row * height
