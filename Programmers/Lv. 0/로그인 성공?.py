def solution(id_pw, db):    
    if pw := dict(db).get(id_pw[0]):
        return 'login' if id_pw[1] == pw else 'wrong pw'
    return 'fail'
    
    