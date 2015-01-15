__author__ = 'jasocarter'

import sqlite3

TABLE_NAME = "yelp_business"
DATABASE_NAME = "reviews.db"
COLUMN_BUSINESS_ID = "business_id"
COLUMN_FULL_ADDRESS = "full_address"
COLUMN_CATEGORIES = "categories"
COLUMN_CITY = "city"
COLUMN_REVIEW_COUNT = "review_count"
COLUMN_NAME = "name"
COLUMN_LONGITUDE = "longitude"
COLUMN_STATE = "state"
COLUMN_STARS = "stars"
COLUMN_LATITUDE = "latitude"
COLUMN_TYPE = "type"


class Yelp_Business:
    def __init__(self, business_id, full_address, categories, city, review_count, name, longitude, state, stars, latitude , type):
        self.business_id = business_id
        self.full_address = full_address
        self.categories = categories
        self.city = city
        self.review_count = review_count
        self.name = name
        self.longitude = longitude
        self.state = state
        self.stars = stars
        self.latitude = latitude
        self.type = type

    def insert_into_database(self):
          conn = sqlite3.connect(DATABASE_NAME)
          print "INSERT INTO {0} ({1},{2},{3},{4},{5},{6},{7},{8},{9},{10}) VALUES (?,?,?,?,?,?,?,?,?,? );".format(TABLE_NAME, COLUMN_BUSINESS_ID, COLUMN_FULL_ADDRESS,  COLUMN_CITY,
                            COLUMN_REVIEW_COUNT, COLUMN_NAME,
                            COLUMN_LONGITUDE, COLUMN_STATE,
                            COLUMN_STARS, COLUMN_LATITUDE,COLUMN_TYPE ),(self.business_id, self.full_address, self.city, self.review_count, self.name, self.longitude,
                      self.state, self.stars, self.latitude, self.type)

          conn.execute("INSERT INTO {0} ({1},{2},{3},{4},{5},{6},{7},{8},{9},{10}) VALUES (?,?,?,?,?,?,?,?,?,? );".
                     format(TABLE_NAME, COLUMN_BUSINESS_ID, COLUMN_FULL_ADDRESS,  COLUMN_CITY,
                            COLUMN_REVIEW_COUNT, COLUMN_NAME,
                            COLUMN_LONGITUDE, COLUMN_STATE,
                            COLUMN_STARS, COLUMN_LATITUDE,COLUMN_TYPE ),
                     (self.business_id, self.full_address, self.city, self.review_count, self.name, str(self.longitude),
                      self.state, self.stars, str(self.latitude), self.type))
          conn.commit()
          conn.close()

