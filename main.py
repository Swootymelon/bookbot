def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    count = word_count(book_path)
    print(f"{count} words found in the document")
    print(" ")
#    text = get_book_text(book_path)

    lowered = count_letters(book_path)
    sort_key = "num"
    sorted_dict = dict(sorted(lowered.items(), key=lambda item: item[1][sort_key], reverse=True))
#    lowered.sort(reverse=True, key=sort_on)
    for i in sorted_dict:
        print(f"the {sorted_dict[i]['name']} character was found: {sorted_dict[i]['num']} times")
    
def count_letters(path):
    with open(path) as f:
        lowered_str = (f.read()).lower()
        count_dict = {}
        for c in lowered_str:
            if c.isalpha():
                if c not in count_dict:
                    count_dict[c] = {"name": c, "num": 0}
                count_dict[c]["num"] += 1
        return count_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(path):
    with open(path) as f:
        text = f.read()
        words = text.split()
        return(len(words))

main()