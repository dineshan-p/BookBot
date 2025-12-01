import sys

from stats import *

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book_text)} total words")
    print("--------- Character Count -------")
    descending_char_dict = sort_char_dict(get_char_count(book_text))
    for pair in descending_char_dict:
        print(f"{pair["char"]}: {pair["num"]}")


    
if __name__ == "__main__":
    main()

