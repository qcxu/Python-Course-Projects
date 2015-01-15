__author__ = 'jasocarter'
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

SENTIMENT_TYPE = 0
POSITIVE_SENTIMENT_VALUE = 1
NEGATIVE_SENTIMENT_VALUE = 2


def main():
    blob = TextBlob("I love this library", analyzer=NaiveBayesAnalyzer())
    sentiment = blob.sentiment
    print "This word has a", sentiment[SENTIMENT_TYPE], "sentiment the positive value is", sentiment[POSITIVE_SENTIMENT_VALUE],\
        "the negative sentiment value is",  sentiment[NEGATIVE_SENTIMENT_VALUE]

main()