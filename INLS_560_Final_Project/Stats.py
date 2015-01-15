__author__ = 'QiongchengXu'
import sqlite3

TABLE_NAME = "review_stats"
DATABASE_NAME = "reviews.db"
COLUMN_BUSINESS_ID = "business_id"
COLUMN_NO_POS = "number_of_positive_reviews"
COLUMN_NO_NEG = "number_of_negative_reviews"
COLUMN_PER_POS = "percentage_of_positive_reviews"
COLUMN_PER_NEG = "percentage_of_negative_reviews"


class Stats:
    def __init__(self, business_id, number_of_positive_reviews, number_of_negative_reviews,
                 percentage_of_positive_reviews, percentage_of_negative_reviews):
        self.business_id = business_id
        self.number_of_positive_reviews = number_of_positive_reviews
        self.number_of_negative_reviews = number_of_negative_reviews
        self.percentage_of_positive_reviews = percentage_of_positive_reviews
        self.percentage_of_negative_reviews = percentage_of_negative_reviews


    def insert(self):
        conn = sqlite3.connect(DATABASE_NAME)
        conn.execute("INSERT INTO {0} ({1},{2},{3},{4},{5}) VALUES (?,?,?,?,?);".
                     format(TABLE_NAME, COLUMN_BUSINESS_ID, COLUMN_NO_POS, COLUMN_NO_NEG, COLUMN_PER_POS, COLUMN_PER_NEG),
                     (self.business_id, self.number_of_positive_reviews, self.number_of_negative_reviews,
                      self.percentage_of_positive_reviews, self.percentage_of_negative_reviews))
        conn.commit()
        conn.close()


    def get_review_stats(self):
        conn = sqlite3.connect(DATABASE_NAME)
        cur = conn.cursor()
        sql = "SELECT * FROM review_stats WHERE business_id = '{0}'".format(self.business_id)
        cur.execute(sql)
        row = cur.fetchone()
        new_review_stats = Stats(row[0], row[1], row[2], row[3], row[4])
        conn.commit()
        conn.close()
        return new_review_stats