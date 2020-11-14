# python-word-counter
A simple word counter implemented in Python.

The application counts the occurences of each word in a text file.  
The results are written to a CSV file, sorted by count from highest to lowest.

### Requirements

Python 3 must be installed.

### Usage
Run the following command to get a description of how to use the application.
```bash
python word_counter.py -h
```

An example command might look like the following:
```bash
python word_counter.py -i samples/trump_tweets.txt -o samples/trump_tweets_results_limit_1000.csv -l 1000
```
