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
    #Get reviews with sentiment of top 30 business_id from yelp_business and insert into table sentiment
    insert_sentiment_by_business_id(10)
    #Get review stats according to table sentiment
    insert_all_review_stats()


#Get reviews from table yelp_review of the top 30 business_id from yelp_business, using TextBlob to determine review
# sentiment and insert data into table sentiment
def insert_sentiment_by_business_id(limit):
    #Get top 30 business_ids
    business = Business("","","","","","","","","","")
    business_id_list = business.get_ids_from_limited_rows(limit)

    for business_id in business_id_list:
        #Call constructor
        review = Review("", "", "", "", "", "", business_id, "", "", "")
        #Get the reviews of the business_id from table yelp_review
        reviews = review.get_reviews_by_business_id()
        #Using TextBlob to determine review sentiment
        for a_review in reviews:
            blob = TextBlob(a_review.text, analyzer=NaiveBayesAnalyzer())
            text_sentiment = blob.sentiment
            #text_sentiment will either be pos (for positive) or neg (for negative)
            text_sentiment = text_sentiment[SENTIMENT_TYPE]

            #Create Sentiment instance
            sentiment = Sentiment(a_review.review_id, a_review.business_id, text_sentiment)
            #Insert information into the sentiment table
            sentiment.insert()


#Get information from table sentiment and insert review stats into table review_stats
def insert_all_review_stats():
    #Select the number of positive reviews by business_id
    business_pos_stats = count_review("pos")
    #Select the number of negative reviews by business_id
    business_neg_stats = count_review("neg")

    #Get a dictionary to store review stats with the key of business id
    review_stats = get_review_stats(business_pos_stats, business_neg_stats)

    #Insert information into table review_stats according to the dictionary
    for business in review_stats:
        #business_id is the key of dictionary
        business_id = business
        #Review stats are the values associated with the key
        number_of_positive_reviews = review_stats[business][0]
        number_of_negative_reviews = review_stats[business][1]
        number_of_reviews = number_of_positive_reviews + number_of_negative_reviews
        percentage_of_positive_reviews = float(number_of_positive_reviews) / number_of_reviews
        percentage_of_negative_reviews = float(number_of_negative_reviews) / number_of_reviews

        #Create Stats object
        business_stat = Stats(business_id, number_of_positive_reviews, number_of_negative_reviews,
                            percentage_of_positive_reviews, percentage_of_negative_reviews)
        #Insert a record of review_stats
        business_stat.insert()


#Get the count of reviews of the sentiment type into a dictionary. business_id is the key, count is the value.
def count_review(sentiment):
    conn = sqlite3.connect(DATABASE_NAME)
    #Select the number of reviews of the sentiment type by business_id
    sql = "SELECT business_id, COUNT (*) AS number_of_positive_reviews FROM sentiment WHERE sentiment = '{0}' " \
        "GROUP BY business_id".format(sentiment)
    rows = conn.execute(sql)
    #Get a dictionary of number of reviews of the sentiment type associated with business_id
    business_stats = dict()
    for row in rows:
        business_id = row[0]
        number_of_positive_reviews = row[1]
        business_stats[business_id] = number_of_positive_reviews
    conn.commit()
    conn.close()
    return business_stats


#Get a dictionary to store review stats associated with business_id
def get_review_stats(business_pos_stats, business_neg_stats):
    #Create a dictionary to store review stats associated with business_id
    review_stats = dict()
    #Insert business_id as key in the dictionary, values are a list of review stats associated with business_id.
    # The list includes the number of pos/neg reviews, the percentage of pos/neg reviews
    for business in business_pos_stats:
        #Initiate a list as value of the key (business_id).
        #stats_record = [number of pos reviews, number of neg reviews, percentage of pos reviews, percentage of neg reviews]
        stats_record = [0, 0, 0, 0]
        #Update number of pos reviews
        stats_record[0] = business_pos_stats[business]
        #Update the dictionary with this business_id
        review_stats[business] = stats_record

    #Update the number of neg reviews into the dictionary
    for business in business_neg_stats:
        #If business_id is already in the dictionary, update the number of neg reviews
        if business in review_stats:
            review_stats[business][1] = business_neg_stats[business]
        #If not, insert business_id as a new key, and insert the number of neg reviews
        else:
            stats_record = [0, 0, 0, 0]
            stats_record[1] = business_neg_stats[business]
            review_stats[business] = stats_record
    return review_stats


main()