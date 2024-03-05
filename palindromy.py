# funkcja, która sprawdza czy dany wyraz jest palindromem
def palindrom(pal_word):
    if pal_word == pal_word[::-1]:
        is_palindrom = True
    else:
        is_palindrom = False
    return is_palindrom

print(palindrom(""))
        