

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{count_words(file_contents)} words found in the document")
    print()
    letters = count_letters(file_contents)
    for letter in letters:
        if letter.isalpha():
            print(f"The '{letter}' character was found {letters[letter]} times")
    print("--- End report ---")


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    letters = {}

    for letter in text:
        if letter.lower() in letters:
            letters[letter.lower()] += 1
        else:
            letters[letter.lower()] = 1
    return letters




main()