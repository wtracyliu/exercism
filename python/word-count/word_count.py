def word_count(phrase):
    char_list = list(phrase)
    for i in range(len(phrase)):
        c = char_list[i]
        if c.isalpha() or c.isdigit():
            continue
        if c != "'":
            char_list[i] = " "
        elif (i < (len(phrase) - 1) and char_list[i+1].isalpha()) and (i >1 and char_list[i-1].isalpha()):
            continue
        else:
            char_list[i] = " "
    new_phrase = ''.join(char_list)
    word_list = [word.lower() for word in new_phrase.split()]
    result = {}
    for word in word_list:
        if word not in result:
            result[word] = word_list.count(word)
        else:
            continue
    return result
