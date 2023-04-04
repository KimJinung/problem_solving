def solution(rsp):
    cheat_sheet = {"2": "0", "0": "5", "5": "2"}

    return "".join([cheat_sheet[key] for key in rsp])
