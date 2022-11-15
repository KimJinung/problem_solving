def solution(X, Y):
    default_dict = {str(num): 0 for num in range(10)}
    
    x_dict = default_dict.copy()
    y_dict = default_dict.copy()

    for num in X:
        x_dict[num] += 1
        
    for num in Y:
        y_dict[num] += 1
        
    
    intersection_list = []
    
    for num in range(9, -1, -1):
        key = str(num)
        
        x_count = x_dict[key]
        y_count = y_dict[key]
        
        repeat = min(x_count, y_count)
            
        for _ in range(repeat):
            intersection_list.append(key)
    
    if not intersection_list:
        return "-1"
    
    answer = ''.join(intersection_list)
    
    for num in range(9, 0, -1):
        if str(num) in answer:
            return answer
    
    return "0"
