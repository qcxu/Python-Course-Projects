__author__ = 'QiongchengXu'
from Review import *
from Sentiment import *
from textblob import *
from textblob.en.sentiments import NaiveBayesAnalyzer
from Stats import *
from Business import *
from CommonPhrase import *

SENTIMENT_TYPE = 0
POSITIVE_SENTIMENT_VALUE = 1
NEGATIVE_SENTIMENT_VALUE = 2
DATABASE_NAME = "reviews.db"


def main():
    #User input business name
    business_name = raw_input("Please enter the name of a business: ")
    #Get a list of business id with the given business name
    business = Business("","","","", business_name,"","","","","")
    business_id_list = business.get_ids_by_business_name()
    #Get option from user input
    option = raw_input(print_instructions())

    while option != '7':

        if option == '1':
            #Get review stats from table review_stats about the business
            for business_id in business_id_list:
                review_stat = Stats(business_id, 0, 0, 0.0, 0.0)
                review_stat = review_stat.get_review_stats()
                #Print review stats
                print "Business id:", review_stat.business_id
                print "Number of positive reviews:", review_stat.number_of_positive_reviews
                print "Number of negative reviews:", review_stat.number_of_negative_reviews
                print "Percentage of positive reviews:", format(review_stat.percentage_of_positive_reviews*100, ".2f") + "%"
                print "Percentage of negative reviews:", format(review_stat.percentage_of_negative_reviews*100, ".2f") + "%"

        if option == '2':
            #Get top 10 common phrases used in reviews
            for business_id in business_id_list:
                commonPhrase = CommonPhrase("", business_id, "", "","", "")
                common_phrase_list = commonPhrase.get_common_phrase_by_id(10)
                #Print common phrases and their frequency
                for com_phrase in common_phrase_list:
                    print com_phrase.common_phrase, com_phrase.frequency_of_phrase

        if option == '3':
            #Get top 10 common phrases for positive reviews with business_id
            for business_id in business_id_list:
                commonPhrase = CommonPhrase("", business_id, "", "","", "")
                common_phrase_list = commonPhrase.get_common_phrase_by_id_pos(10)
                #Print common phrases and their frequency
                for com_phrase in common_phrase_list:
                    print com_phrase.common_phrase, com_phrase.pos_frequency_of_phrase

            # #Get top n common phrases for all positive reviews
            # for business_id in business_id_list:
            #     commonPhrase = CommonPhrase("", business_id, "", "","", "")
            #     common_phrase_list = commonPhrase.get_common_phrase_by_pos(10)
            #     #Print common phrases and their frequency
            #     for com_phrase in common_phrase_list:
            #         print com_phrase.common_phrase, com_phrase.pos_frequency_of_phrase

        if option == '4':
            #Get top 10 common phrases for negative reviews
            for business_id in business_id_list:
                commonPhrase = CommonPhrase("", business_id, "", "","", "")
                common_phrase_list = commonPhrase.get_common_phrase_by_id_neg(10)
                #Print common phrases and their frequency
                for com_phrase in common_phrase_list:
                    print com_phrase.common_phrase, com_phrase.neg_frequency_of_phrase

            # #Get top n common phrases for all positive reviews
            # for business_id in business_id_list:
            #     commonPhrase = CommonPhrase("", business_id, "", "","", "")
            #     common_phrase_list = commonPhrase.get_common_phrase_by_neg(10)
            #     #Print common phrases and their frequency
            #     for com_phrase in common_phrase_list:
            #         print com_phrase.common_phrase, com_phrase.neg_frequency_of_phrase

        if option == '5':
            #Get examples of positive reviews about the business with limit numbers: 5
            get_review_example(business_id_list, "pos", 5)

        if option == '6':
            #Get examples of negative reviews about the business with limit numbers: 5
            get_review_example(business_id_list, "neg", 5)

        option = raw_input(print_instructions())


def print_instructions():
    return "Please choose an option:\n" \
           "1. Show the number of positive and negative reviews, the percentage of positive and negative reviews\n" \
           "2. Show the top n common phrases (n=10)\n" \
           "3. Show the top n common phrases for positive reviews (n=10)\n" \
           "4. Show the top n common phrases for negative reviews (n=10)\n" \
           "5. Show examples of positive reviews\n" \
           "6. Show examples of negative reviews\n" \
           "7. Exit\n"


def get_review_example(business_id_list, sentiment, limit):
    #Get the limit number of reviews from table yelp_review
    for business_id in business_id_list:
        eg_review = Review("", "", "", "", "", "", business_id, "", "", "")
        reviews = eg_review.get_reviews_by_business_id_and_sentiment(sentiment, limit)
        print "Business id:", business_id
        if sentiment == "pos":
            print "Example of positive reviews:"
        else:
            print "Example of negative reviews:"
        for review in reviews:
            print review.text
        print "\n"


main()


