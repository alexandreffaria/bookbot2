def main():
    bookPath = "books/frank.txt"
    text = readBook(bookPath)
    wordsCount = countWords(text)
    counted = countChars(text)
    print(f"--- Begin report of {bookPath.split("/")[1]} ---")
    print(f"{wordsCount} words found in the document")
    print()
    for char, count in sorted(counted.items(), key=lambda item: item[1], reverse=True):
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

def countWords(s):
    words = s.split()
    return len(words)


def readBook(bookPath):
    with open(bookPath, "r") as bookFile:
        return bookFile.read()


def countChars(s):
    chars = {}
    for c in s.lower():
        if c.isalpha():
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
    return chars


main()
