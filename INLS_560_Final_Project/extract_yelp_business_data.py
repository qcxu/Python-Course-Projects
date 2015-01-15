__author__ = 'jasocarter'
import demjson
import sqlite3
import yelp_business
FILE_LOCATION = "yelp/yelp_academic_dataset_business.json"

def main():
    file_contents = read_file()

    number_of_lines = len(file_contents)

    count = 0
    for line in file_contents:
        object = text = demjson.decode(line)

        #, business_id, full_address, categories, city, review_count, name, longitude, state, stars, latitude , type):
        review = yelp_business.Yelp_Business(object.get(yelp_business.COLUMN_BUSINESS_ID),
                                             object.get(yelp_business.COLUMN_FULL_ADDRESS),object.get(yelp_business.COLUMN_CATEGORIES),
                                         object.get(yelp_business.COLUMN_CITY), object.get(yelp_business.COLUMN_REVIEW_COUNT),
                                         object.get(yelp_business.COLUMN_NAME), object.get(yelp_business.COLUMN_LONGITUDE),
                                         object.get(yelp_business.COLUMN_STATE), object.get(yelp_business.COLUMN_STARS),
                                         object.get(yelp_business.COLUMN_LATITUDE), object.get(yelp_business.COLUMN_TYPE))

        review.insert_into_database()
        print (count/number_of_lines) * 100
        count += 1





def read_file():
    in_file = open(FILE_LOCATION, 'r')
    file_contents = in_file.readlines()
    return file_contents

main()
