import sys
from operator import itemgetter


def main():
    if len(sys.argv) < 2:
        print("Usage: python ./word_counter.py <input-path> [limit]")
        return
    input_path = sys.argv[1]
    limit = None
    if len(sys.argv) >= 3:
        limit = int(sys.argv[2])

    file = open(input_path, "r", encoding="utf8")
    text = file.read()

    text = filter_text(text)
    text = text.lower()
    words = tokenize(text)

    word_counts = count_words(words)
    sorted_word_counts = sort_by_count(word_counts)

    if limit is None:
        limit = len(sorted_word_counts)

    for i in range(0, limit):
        item = sorted_word_counts[i]
        print(item[0] + ": " + str(item[1]))


def filter_text(text):
    filtered_text = text
    invalid_chars = ",;.:-_^!\"§$%&/()=?{[]}\\'+*~"
    for char in invalid_chars:
        filtered_text = filtered_text.replace(char, "")
    return filtered_text


def tokenize(text):
    words = []
    lines = text.splitlines()
    for line in lines:
        curr_words = line.split()
        words.extend(curr_words)
    return words


def count_words(words):
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    return word_counts


def sort_by_count(word_counts):
    return sorted(word_counts.items(), key=itemgetter(1), reverse=True)


if __name__ == "__main__":
    main()
