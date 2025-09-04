import sys


from stats import get_num_words, get_chars_stats


def main():
    input_list = sys.argv
    if len(input_list) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = input_list[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    stat_list = get_chars_stats(text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in stat_list:
        print(f'{c['char']}: {c['num']}')
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()