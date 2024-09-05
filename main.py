def main():
    book_link = "books/frankenstein.txt"
    with open(book_link) as f:
        file_contents = f.read()
    print(f"==== Book report for {book_link} ====")
    print_report(file_contents)

def word_count(text):
    return len(text.split())

def letter_count(text):
    letter_dict = {}
    for letter in text:
        if not letter.isalpha():
            continue
        lower_letter = letter.lower()
        if lower_letter in letter_dict:
            letter_dict[lower_letter] += 1
        else:
            letter_dict[lower_letter] = 1
    return letter_dict

def sort_letters(dict):
    def sort_on(dict):
        return dict["count"]

    def dict_to_list(dict):
        new_list = []
        for key in dict.keys():
            new_list.append({"letter": key, "count": dict[key]})
        return new_list
    
    sorted_list = dict_to_list(dict)
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list


def print_report(text):
    print(f"Words found in text: {word_count(text)}")
    print()
    print("Letters found in text:")
    letter_dict = letter_count(text) # { "a": 123, "b": 321, ...}
    letter_list = sort_letters(letter_dict) # [ {"letter": "a", "count": "123"}, {"letter": "b", "count": "321"}, ... ]
    for entry in letter_list:
        print(f"{entry['letter']} was found {entry['count']} times")

main()