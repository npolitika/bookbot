def get_book_text(filepath):
    with open(filepath) as booktext:
        book_text = booktext.read()
        return book_text

def wordcount(book_text):
    words = book_text.split()
    word_count = 0
    for i in words:
        word_count += 1
    return word_count

def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_text(book_path)
    word_count = wordcount(book_contents)
    print(f'{word_count} words found in the document')

main()