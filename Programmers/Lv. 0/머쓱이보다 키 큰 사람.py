def solution(array, height):
    return len([friend for friend in array if height < friend])
