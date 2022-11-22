def solution(polynomial):
    polynomial_dict = {'x': 0, 'num': 0}
    
    for item in polynomial.split():
        if item == '+':
            continue
        
        if 'x' == item[-1]:
            if item.isalpha():
                item = '1' + item
            
            polynomial_dict['x'] += int(item[:-1])
        else:
            polynomial_dict['num'] += int(item)
            
    
    polynomial_list = []
    
    if x_value := polynomial_dict.get('x'):
        if x_value == 1:
            x_value = ''
        polynomial_list.append(str(x_value)+'x')
    
    if num_value := polynomial_dict.get('num'):
        polynomial_list.append(str(num_value))
        
    return ' + '.join(polynomial_list)
 