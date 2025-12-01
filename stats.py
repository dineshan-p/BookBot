def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def get_word_count(book_str):
    word_list = book_str.split()
    return len(word_list)
    
def get_char_count(book_str):
    char_dict = {}
    for char in book_str:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
        
    return char_dict

def sort_char_dict(char_dict):
    sorted_list = []
    for entry in char_dict:
        if entry.isalpha():
            new_dict = {"char": entry, "num": char_dict[entry]}
            sorted_list.append(new_dict)
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(items):
    return items["num"]