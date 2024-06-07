def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_chars_dict(text):
    chars = {}
    for char in text.lower():
        if not char.isalpha():
            continue
        if char not in chars:
            chars[char] = 0
        chars[char] += 1
    return chars

def print_report(path, word_count, chars_dict):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print()

    for letter in sorted(chars_dict, reverse=True, key=chars_dict.get):
        print(f"The '{letter}' character was found {chars_dict[letter]} times")

    print("--- End report ---")

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = get_word_count(text)
    chars_dict = get_chars_dict(text)
    print_report(path, word_count, chars_dict)
    


if __name__ == '__main__':
    main()