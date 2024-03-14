# funkcja, która sprawdza czy dany wyraz jest palindromem
def palindrom(pal_word):
    return(pal_word == pal_word[::-1])

print(palindrom(""))
        