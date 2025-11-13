from stats import get_book_word_count, get_char_count, get_sorted_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_string = get_book_text(book_path)
    word_count = get_book_word_count(book_string)
    #print(f"{word_count} words found in the document")
    char_dict = get_char_count(book_string)
    sorted_char_list = get_sorted_dict(char_dict)

    print("============ BOOKBOT ============\n" +
          f"Analyzing book found at {book_path}...\n" +
          "----------- Word Count ----------")
    print(f"Found {word_count} total words\n" + 
          "-------- Character Count -------")
    for item in sorted_char_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    

main()