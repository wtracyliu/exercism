def is_pangram(sentence):
    s = [i.upper() for i in sentence if i.isalpha()]
    if len(set(s)) == 26:
        return True
    else:
        return False
