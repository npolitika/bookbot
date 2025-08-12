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

def sort_on(items_for_sort):
    return items_for_sort['num']

def charcount_dict_to_sorted_list(char_dict):
    new_list = []
    for key, value in char_dict.items():
        new_items = dict(char=key, num=value)
        new_list.append(new_items)

    new_list.sort(reverse=True, key=sort_on)
    return new_list
#print(charcount)

