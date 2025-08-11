def get_wordcount(book_text):
    words = book_text.split()
    return len(words)


def get_charcount(words_string):
    words_lower = words_string.lower()
    charcount = {}
    for letter in words_lower:
           if letter in charcount:
               charcount[letter] += 1
           else:
               charcount[letter] = 1
    return charcount