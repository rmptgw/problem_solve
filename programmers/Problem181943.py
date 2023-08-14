def solution(my_string, overwrite_string, s):
    str = ''
    answer = ''
    for i in range(s,s+len(overwrite_string)):
        str = str + my_string[i]
    
    answer = my_string.replace(str, overwrite_string)

    return answer