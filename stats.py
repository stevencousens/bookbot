def get_num_words(book_text):
    num_words = len(book_text.split())
    return num_words

def count_chars(text):
    lowered_text = text.lower()
    char_counts = {}
    for letter in lowered_text:
        if letter in char_counts:
            char_counts[letter] += 1
        else:
            char_counts[letter] = 1
    return char_counts

def sort_counts(char_counts):

    list_dicts = []

    for key in char_counts:
        list_dicts.append({"char": key, "num": char_counts[key]})
 
    def sort_on(dict):
        return dict["num"]

    list_dicts.sort(reverse=True,key=sort_on)

    return list_dicts
