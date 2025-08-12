from stats import (
    get_wordcount as get_num_words,
    get_charcount as get_chars_dict,
    charcount_dict_to_sorted_list as char_dict_sort
)
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 main.py <path_to_book>")
    else:
        book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = char_dict_sort(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)

def get_book_text(filepath):
    with open(filepath) as booktext:
        book_text = booktext.read()
        return book_text
    
def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        char_value = item["char"]
        num_value = item["num"]
        if char_value.isalpha():
            print(f"{char_value}: {num_value}")
    print("============= END ===============")    

if __name__ == '__main__':
    main()