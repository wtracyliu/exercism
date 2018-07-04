def is_isogram(string):
    l = [i.upper() for i in string if i!= ' ' and i !='-' ]
    result = True
    for i in l:
        if l.count(i) > 1:
            result = False
            break
    return result


