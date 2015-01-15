__author__ = 'QiongchengXu'
import sqlite3

TABLE_NAME = "yelp_business"
DATABASE_NAME = "reviews.db"
COLUMN_BUSINESS_ID = "business_id"
COLUMN_FULL_ADDRESS = "full_address"
COLUMN_CATEGORIES = "categories"
COLUMN_REVIEW_COUNT = "review_count"
COLUMN_NAME = "name"
COLUMN_LONGITUDE = "longitude"
COLUMN_STATE = "state"
COLUMN_STARS = "stars"
COLUMN_LATITUDE = "latitude"
COLUMN_TYPE = "type"


class Business:
    def __init__(self, business_id, full_address, categories, review_count, name, longitude, state, stars,
                 latitude, type):
        self.business_id = business_id
        self.full_address = full_address
        self.categories = categories
        self.review_count = review_count
        self.name = name
        self.longitude = longitude
        self.state = state
        self.stars = stars
        self.latitude = latitude
        self.type = type

    #Get a list of business id with the given business name
    def get_ids_by_business_name(self):
        conn = sqlite3.connect(DATABASE_NAME)
        sql = "SELECT business_id FROM yelp_business WHERE name = '{0}'".format(self.name)
        rows = conn.execute(sql)
        business_id_list = []
        for row in rows:
            business_id_list.append(row[0])
        return business_id_list


    def get_ids_from_limited_rows(self, limit):
        conn = sqlite3.connect(DATABASE_NAME)
        sql = "SELECT * FROM yelp_business limit {0}".format(limit)
        rows = conn.execute(sql)
        business_id_list = []
        for row in rows:
            business_id_list.append(row[0])
        return business_id_list