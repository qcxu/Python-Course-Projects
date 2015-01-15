__author__ = 'jasocarter'
import demjson

import Review
FILE_LOCATION = "yelp/yelp_academic_dataset_review.json"

def main():
    file_contents = read_file()

    for line in file_contents:
        object = text = demjson.decode(line)
        insert_SQL = "Insert into yelp_review "
        #, user_id, review_id, stars, date, text, type, business_id, votes_funny, votes_useful, votes_cool)
        review = Review.Yelp_Review(object.get(Review.COLUMN_USER_ID), object.get(Review.COLUMN_REVIEW_ID),object.get(Review.COLUMN_STARS),
                                         object.get(Review.COLUMN_DATE), object.get(Review.COLUMN_TEXT), object.get(Review.COLUMN_TYPE),
                                         object.get(Review.COLUMN_BUSINESS_ID), object.get("votes")["funny"], object.get("votes")["useful"],
                                         object.get("votes")["cool"])
        review.insert_into_database()





def read_file():
    in_file = open(FILE_LOCATION, 'r')
    file_contents = in_file.readlines()
    return file_contents

main()
