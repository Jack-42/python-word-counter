# python-word-counter
A simple word counter implemented in Python.

### Requirements

Python 3 must be installed.

### Usage

Run the app in the command line by the following command:

```
python word_counter.py <input-file> [limit]
```

The app prints a list of the unique words and their count, sorted from highest to lowest count.

The `input-file` argument is required and specifies the path to a text file.

The `limit` argument is optional and specifies how many words should be printed. If it is ommited, all words are printed.

An example command might look as folllows:

```
python word_counter.py samples/trump_tweets.txt 100
```
