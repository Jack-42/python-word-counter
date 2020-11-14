import argparse
from operator import itemgetter
import csv


def main():
    parser = argparse.ArgumentParser(description="Count words in a text file and output results to CSV file")
    parser.add_argument("-i", "--input_path", type=str, required=True, help="Path to the input text file")
    parser.add_argument("-o", "--output_path", type=str, required=True, help="Path to the output CSV file")
    parser.add_argument("-l", "--limit", type=int, required=False,
                        help="The number of words to include in the output (all by default)")
    args = parser.parse_args()

    input_path = args.input_path
    output_path = args.output_path
    limit = args.limit

    with open(input_path, "r", encoding="utf8") as file:
        text = file.read()

    text = filter_text(text)
    text = text.lower()
    words = tokenize(text)
    word_counts = count_words(words)
    sorted_word_counts = sort_by_count(word_counts)

    if limit is None:
        limit = len(sorted_word_counts)

    write_csv_file(output_path, sorted_word_counts, limit)


def filter_text(text):
    filtered_text = text
    invalid_chars = "0123456789,;.:-_^!\"§$%&/()=?{[]}\\'+*~"
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


def write_csv_file(path, sorted_word_counts, limit):
    with open(path, "w", encoding="utf8", newline="") as file:
        writer = csv.writer(file)
        header = ["Rank", "Word", "Count"]
        writer.writerow(header)
        for i in range(0, limit):
            rank = i + 1
            word = sorted_word_counts[i][0]
            count = sorted_word_counts[i][1]
            row = [str(rank), word, str(count)]
            writer.writerow(row)


if __name__ == "__main__":
    main()
