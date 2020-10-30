# python-word-counter
A simple word counter implemented in Python.

### Requirements

Python 3 must be installed.

### Usage

Run the app in the command line by the following command:

```
python word_counter.py <input_path> <output_path> [limit]
```

The app counts the unique words in a text file and outputs the results as a csv file, sorted by count from highest to lowest.

The `input_path` argument is required and specifies the path to the input text file.

The `output_path` argument is required and specifies the path to the output CSV file.

The `limit` argument is optional and specifies how many words should be included in the output. If it is ommited, all words are included.

An example command might look as folllows:

```
python word_counter.py samples/trump_tweets.txt samples/trump_tweets_results.csv 100
```
