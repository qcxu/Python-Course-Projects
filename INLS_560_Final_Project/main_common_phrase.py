__author__ = 'QiongchengXu'
from Review import *
from Sentiment import *
from textblob import *
from textblob.en.sentiments import NaiveBayesAnalyzer
from Stats import *
from CommonPhrase import *
from Business import *

SENTIMENT_TYPE = 0
POSITIVE_SENTIMENT_VALUE = 1
NEGATIVE_SENTIMENT_VALUE = 2
DATABASE_NAME = "reviews.db"


def main():
    #Insert top 30 business_ids' common phrase into database
    insert_common_phrase()


def insert_common_phrase():
    #Get top 30 business_ids
    business = Business("","","","","","","","","","")
    business_id_list = business.get_ids_from_limited_rows(10)
    #print business_id_list
    for business_id in business_id_list:
        #Initial word_dictionary to store words and their frequency as a dictionary
        word_dictionary = dict()

        #Get positive reviews of business_id
        new_review = Review("", "", "", "", "", "", business_id, "", "", "")
        reviews = new_review.get_all_reviews_by_business_id_and_sentiment("pos")
        if reviews:
            for review in reviews:
                #Split each review into words
                review_text = review.text
                word_list = review_text.split(' ')

                for word in word_list:
                    #Remove punctuation of word
                    word = escape_word(word)
                    #Update the frequency of word in pos reviews into the dictionary
                    if word != "":
                        if word not in word_dictionary:
                            word_dictionary[word] = [1, 0]
                        else:
                            word_dictionary[word][0] += 1


        #Get negative reviews of business_id
        new_review = Review("", "", "", "", "", "", business_id, "", "", "")
        reviews = new_review.get_all_reviews_by_business_id_and_sentiment("neg")
        if reviews:
            for review in reviews:
                #Split each review into words
                word_list = review.text.split(' ')
                for word in word_list:
                    #Remove punctuation of word
                    word = escape_word(word)
                    #Update frequency of word in neg reviews into the word_dictionary
                    if word != "":
                        if word not in word_dictionary:
                            word_dictionary[word] = [0, 1]
                        else:
                            word_dictionary[word][1] += 1

        #Insert common phrase into database
        common_phrase = CommonPhrase("",business_id,"","","","")
        common_phrase.insert(word_dictionary)


#Remove punctuation of a word
def escape_word(word):
    word = word.lower()
    word = word.replace(',', '')
    word = word.replace('.', '')
    word = word.replace('<', '')
    word = word.replace('>', '')
    word = word.replace('(', '')
    word = word.replace(')', '')
    word = word.replace(' ', '')
    word = word.replace('"', '')
    word = word.replace('-', '')
    word = word.replace('!', '')
    word = word.replace('?', '')
    word = word.replace(';', '')
    word = word.replace(':', '')
    word = word.replace('*', '')
    word = word.strip()
    return word


main()