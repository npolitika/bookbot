from stats import get_wordcount, get_charcount, charcount_dict_to_sorted_list as char_dict_sort

def get_book_text(filepath):
    with open(filepath) as booktext:
        book_text = booktext.read()
        return book_text
    
def main():
    print("============ BOOKBOT ============")
    book_path = "books/frankenstein.txt"
    print(f"Analyzing book found at {book_path}...")
    book_contents = get_book_text(book_path)
    wordcount = get_wordcount(book_contents)
#    print(f'{wordcount} words found in the document')
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    charactercount = get_charcount(book_contents)
#    print(charactercount)
    print("--------- Character Count -------")
    sorted = char_dict_sort(charactercount)
    for item in sorted:
        char_value = item["char"]
        num_value = item["num"]
        if char_value.isalpha():
            print(f"{char_value}: {num_value}")
    print("============= END ===============")

main()