def verify(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    x = 0
    for i,j in enumerate(isbn):
        if i != (len(isbn) - 1) and j == 'X':
            return False
        elif j == 'X':
            x += 10
        else:
            try:
                j = int(j)
            except:
                return False
            x += (10 - i) * j
    return  x % 11 == 0

