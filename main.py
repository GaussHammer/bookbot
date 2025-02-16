import sys

def main():
    book_path = sys.argv[1]
    with open(book_path) as f:
        file_contents = f.read()
    print(return_total_words(file_contents))
    print(total_chars(file_contents))
    total_letters(total_chars(file_contents))

def return_total_words(text):
    total_words = text.split()
    return len(total_words)

def sort_on(dict):
     return dict["num"]

def total_chars(text):
    chars_count = {}
    text = text.lower()
    for i in range(len(text)):
            if text[i] not in chars_count:
                chars_count[text[i]] = 1
            else:
                chars_count[text[i]] += 1
    return chars_count

def total_letters(chars_count):
    only_letters = []
    for key in chars_count:
         if key.isalpha():
              value = chars_count.get(key)
              only_letters.append({"name" : key, "num": value})
    only_letters.sort(reverse=True, key=sort_on)

    for i in range(len(only_letters)):
         print(f"The {only_letters[i]["name"]} character was found {only_letters[i]["num"]} times")
          

main()