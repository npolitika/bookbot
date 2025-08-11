def get_book_text(filepath):
    with open(filepath) as booktext:
        return booktext.read()

def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_text(book_path)
    print(book_contents)

main()