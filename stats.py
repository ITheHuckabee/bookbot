def get_word_count(book_text):
    num_words = len(book_text.split())
    return num_words

def num_of_characters(book_text):
    chars = {}
    text = book_text.lower()
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_stats(char_counts):
    chars_list = []
    for char, count in char_counts.items():
        chars_list.append({"character": char, "count": count})
    
    def sort_on(dict_item):
        return dict_item["count"]

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
