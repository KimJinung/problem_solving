def solution(babbling):
    answer = 0
    
    pronunciation = {
        'a': 'ya',
        'y': 'e',
        'w': 'oo',
        'm': 'a'
    }
    
    for word in babbling:
        pass_count = 0
        last_ch = ''
        
        for idx, ch in enumerate(word):
            if pass_count != 0:
                pass_count -= 1
                
                if idx == len(word) - 1 and pass_count == 0:
                    answer += 1
                    
                continue
                
            if last_ch == ch:
                break
            
            try:
                target = pronunciation[ch]
            except:
                break
            
            if (ch == 'a' or ch == 'w') and idx < len(word)-2 and word[idx+1:idx+3] == target:
                pass_count = 2
                
            elif (ch == 'y' or ch == 'm') and idx < len(word)-1 and word[idx+1] == target:
                pass_count = 1
            else:
                break
            
            last_ch = ch
            
    
    return answer
    