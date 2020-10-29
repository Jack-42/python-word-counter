import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python ./word_counter.py <input-path>")
        return
    input_path = sys.argv[1]
    file = open(input_path, "r", encoding="utf8")
    text = file.read()

    text = filter_text(text)
    text = text.lower()
    words = tokenize(text)

    word_counts = count_words(words)
    for word in word_counts:
        print(word + ": " + str(word_counts[word]))


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


if __name__ == "__main__":
    main()
