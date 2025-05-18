from stats import sort_stats
from stats import num_of_characters
from stats import get_word_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit[1]
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)
    word_stats = num_of_characters(book_text)
    sorted_stats = sort_stats(word_stats)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_stats:
        char = char_dict["character"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()
