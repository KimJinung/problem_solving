from string import ascii_lowercase as alphabet


def solution(myString):
    return "".join(map(domain_filter, myString))


def domain_filter(ch: str) -> str:
    """
    if character's index smaller than l,
    convert it to l
    :return: str
    """
    ref = alphabet.index("l")

    if alphabet.index(ch) < ref:
        return "l"

    return ch
