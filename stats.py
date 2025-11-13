def get_book_word_count(file_contents):
    words = file_contents.split()
    return len(words)

def get_char_count(file_contents: str) -> dict:
    char_dict = {}

    for char in file_contents.lower():
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_on(item):
    return item["num"]

def get_sorted_dict(unsorted_dict: dict) -> list:
    dict_list = []
    for key, value in unsorted_dict.items():
        dict_list.append({"char": key, "num": value})
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list