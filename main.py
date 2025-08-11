from stats import get_wordcount, get_charcount

def get_book_text(filepath):
    with open(filepath) as booktext:
        book_text = booktext.read()
        return book_text
    
def main():

    book_path = "books/frankenstein.txt"
    book_contents = get_book_text(book_path)
    wordcount = get_wordcount(book_contents)
    print(f'{wordcount} words found in the document')
    charactercount = get_charcount(book_contents)
    print(charactercount)

main()