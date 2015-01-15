__author__ = 'QiongchengXu'
import sqlite3

TABLE_NAME = "common_phrases"
DATABASE_NAME = "reviews.db"
COLUMN_PHRASE_ID = "phrase_id"
COLUMN_BUSINESS_ID = "business_id"
COLUMN_COMMON_PHRASE = "common_phrase"
COLUMN_FREQUENCY_OF_PHRASE = "frequency_of_phrase"
COLUMN_POS_FREQUENCY_OF_PHRASE = "pos_frequency_of_phrase"
COLUMN_NEG_FREQUENCY_OF_PHRASE = "neg_frequency_of_phrase"


class CommonPhrase:
    def __init__(self, phrase_id, business_id, common_phrase, frequency_of_phrase, pos_frequency_of_phrase, neg_frequency_of_phrase):
        self.phrase_id = phrase_id
        self.business_id = business_id
        self.common_phrase = common_phrase
        self.frequency_of_phrase = frequency_of_phrase
        self.pos_frequency_of_phrase = pos_frequency_of_phrase
        self.neg_frequency_of_phrase = neg_frequency_of_phrase


    def insert(self, word_dictionary):
        conn = sqlite3.connect(DATABASE_NAME)
        for key in word_dictionary:
            #Get frequency in pos reviews
            pos_frequency = word_dictionary[key][0]
            #Get frequency in neg reviews
            neg_frequency = word_dictionary[key][1]
            #The sum of all frequency of the word
            frequency = pos_frequency + neg_frequency
            try:
                conn.execute("INSERT INTO {0} ({1},{2},{3},{4},{5}) VALUES (?,?,?,?,?);".
                     format(TABLE_NAME, COLUMN_BUSINESS_ID, COLUMN_COMMON_PHRASE, COLUMN_FREQUENCY_OF_PHRASE, COLUMN_POS_FREQUENCY_OF_PHRASE, COLUMN_NEG_FREQUENCY_OF_PHRASE),
                     (self.business_id, key, frequency, pos_frequency, neg_frequency))
                conn.commit()
            except Exception, err:
                print "Exception"
        conn.close()


    def get_common_phrase_by_id(self, limit):
        conn = sqlite3.connect(DATABASE_NAME)
        sql = "SELECT common_phrase, frequency_of_phrase FROM common_phrases WHERE business_id = '{0}' AND " \
              "frequency_of_phrase > {1} ORDER BY frequency_of_phrase DESC".format(self.business_id, limit)
        rows = conn.execute(sql)
        common_phrase_list = []
        for row in rows:
            new_common_phrase = CommonPhrase("", self.business_id, row[0], row[1], "", "")
            common_phrase_list.append(new_common_phrase)
        return common_phrase_list

    #Get top n common phrase in pos reviews by business id
    def get_common_phrase_by_id_pos(self, limit):
        conn = sqlite3.connect(DATABASE_NAME)
        sql = "SELECT common_phrase, pos_frequency_of_phrase FROM common_phrases WHERE business_id = '{0}' AND " \
              "pos_frequency_of_phrase > {1} ORDER BY pos_frequency_of_phrase DESC".format(self.business_id, limit)
        rows = conn.execute(sql)
        common_phrase_list = []
        for row in rows:
            new_common_phrase = CommonPhrase("", self.business_id, row[0], "", row[1], "")
            common_phrase_list.append(new_common_phrase)
        return common_phrase_list

    #Get top n common phrase in pos reviews by business id
    def get_common_phrase_by_id_neg(self, limit):
        conn = sqlite3.connect(DATABASE_NAME)
        sql = "SELECT common_phrase, neg_frequency_of_phrase FROM common_phrases WHERE business_id = '{0}' AND " \
              "neg_frequency_of_phrase > {1} ORDER BY neg_frequency_of_phrase DESC ".format(self.business_id, limit)
        rows = conn.execute(sql)
        common_phrase_list = []
        for row in rows:
            new_common_phrase = CommonPhrase("", self.business_id, row[0], "", "", row[1])
            common_phrase_list.append(new_common_phrase)
        return common_phrase_list

    # def get_common_phrase_by_pos(self, limit):
    #     conn = sqlite3.connect(DATABASE_NAME)
    #     sql = "SELECT common_phrase, SUM (pos_frequency_of_phrase) AS sum_pos FROM common_phrases GROUP BY " \
    #           "common_phrase ORDER BY sum_pos DESC limit {0}". format(limit)
    #     rows = conn.execute(sql)
    #     common_phrase_list = []
    #     for row in rows:
    #         new_common_phrase = CommonPhrase("", self.business_id, row[0], "", row[1], "")
    #         common_phrase_list.append(new_common_phrase)
    #     return common_phrase_list
    #
    # def get_common_phrase_by_neg(self, limit):
    #     conn = sqlite3.connect(DATABASE_NAME)
    #     sql = "SELECT common_phrase, SUM (neg_frequency_of_phrase) AS sum_neg FROM common_phrases GROUP BY " \
    #           "common_phrase ORDER BY sum_neg DESC limit {0}". format(limit)
    #     rows = conn.execute(sql)
    #     common_phrase_list = []
    #     for row in rows:
    #         new_common_phrase = CommonPhrase("", self.business_id, row[0], "", "", row[1])
    #         common_phrase_list.append(new_common_phrase)
    #     return common_phrase_list
