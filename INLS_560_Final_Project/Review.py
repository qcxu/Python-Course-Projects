__author__ = 'jasocarter'
import sqlite3

TABLE_NAME = "yelp_review"
DATABASE_NAME = "reviews.db"
COLUMN_USER_ID = "user_id"
COLUMN_REVIEW_ID = "review_id"
COLUMN_STARS = "stars"
COLUMN_DATE = "date"
COLUMN_TEXT = "text"
COLUMN_TYPE = "type"
COLUMN_BUSINESS_ID = "business_id"
COLUMN_VOTES_FUNNY = "votes_funny"
COLUMN_VOTES_USEFUL = "votes_useful"
COLUMN_VOTES_COOL = "votes_cool"


class Review:
    def __init__(self, review_id, user_id, stars, date, text, type, business_id,
                 votes_funny, votes_useful, votes_cool):
        self.review_id = review_id
        self.user_id = user_id
        self.stars = stars
        self.date = date
        self.text = text
        self.type = type
        self.business_id = business_id
        self.votes_funny = votes_funny
        self.votes_useful = votes_useful
        self.votes_cool = votes_cool

    def get_reviews_by_business_id(self):
        conn = sqlite3.connect(DATABASE_NAME)
        sql = "SELECT review_id, text FROM yelp_review WHERE business_id = '{0}'".format(self.business_id)
        rows = conn.execute(sql)
        review_list = []
        for row in rows:
            review_id = row[0]
            text = row[1]
            new_review = Review(review_id, "", "", "", text, "", self.business_id, "", "", "")
            review_list.append(new_review)
        conn.commit()
        conn.close()
        return review_list

    #For option 1
    #Get limit number of reviews from yelp_review table
    def get_reviews(self, limit):
        conn = sqlite3.connect(DATABASE_NAME)
        sql = "SELECT review_id, business_id, text FROM yelp_review limit {0};".format(limit)
        rows = conn.execute(sql)
        review_list = []
        for row in rows:
            review_id = row[0]
            business_id = row[1]
            text = row[2]
            new_review = Review(review_id, "", "", "", text, "", business_id, "", "", "")
            review_list.append(new_review)
        conn.commit()
        conn.close()
        return review_list

    #For option 2-4
    #Get all reviews of a sentiment type associated with business id
    def get_all_reviews_by_business_id_and_sentiment(self, sentiment):
        conn = sqlite3.connect(DATABASE_NAME)
        cur = conn.cursor()
        sql = "SELECT R.text FROM yelp_review AS R INNER JOIN sentiment AS S ON R.review_id = S.review_id " \
              "WHERE S.business_id = '{0}' AND S.sentiment = '{1}'".format(self.business_id, sentiment)
        cur.execute(sql)
        #row = cur.fetchall()
        rows = cur.fetchall()
        sentiment_review_list = []
        for row in rows:
            new_review = Review("", "", "", "", row[0], "", "", "", "", "")
            sentiment_review_list.append(new_review)
        conn.commit()
        conn.close()
        return sentiment_review_list



    #For Option 5, 6
    #Get examples of reviews of a sentiment type associated with business name with a limit number
    def get_reviews_by_business_id_and_sentiment(self, sentiment, limit):
        conn = sqlite3.connect(DATABASE_NAME)
        sql = "SELECT R.text FROM yelp_review AS R INNER JOIN sentiment AS S ON R.review_id = S.review_id " \
              "WHERE S.business_id = '{0}' AND S.sentiment = '{1}' limit {2}".format(self.business_id, sentiment, limit)
        review_texts = conn.execute(sql)
        sentiment_review_list = []
        for text in review_texts:
            new_review = Review("", "", "", "", text[0], "", "", "", "", "")
            sentiment_review_list.append(new_review)
        conn.commit()
        conn.close()
        return sentiment_review_list

