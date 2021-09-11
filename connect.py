#!/usr/bin/python
import psycopg2
from config import config
import json
import os

def add_column(column,cur):
    commands = (
        """
        ALTER TABLE drug_data ADD COLUMN 
            {column} VARCHAR(255)
        """.format(column=column),
        )
    for command in commands:
        cur.execute(command)
    print("Alter Table Called")

def connect(columns):
    print(type(columns))

    column_one = columns[0]
    #print(column_one)
    #create_table = """CREATE TABLE drug_data ({column_one} VARCHAR(255))""".format(column_one = column_one)
    table_create = ("""
        CREATE TABLE drug_data (
                {column_one} VARCHAR(255)
        )
        """.format(column_one = column_one),)
    
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database..')
        conn = psycopg2.connect(**params)
		

        # create a cursor
        
        cur = conn.cursor()

        for command in table_create:
            print("Executed Commands",command)
            cur.execute(command)

        #for i in range(1,len(uniq_keys)):
            #add_column(uniq_keys[i], cur)
            
       
	# close the communication with the PostgreSQL
        cur.close()

        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    json_dict = json.load(open('data10.json','r'))
    uniq_keys = []
    for _dict in json_dict['results']:
        keys = _dict.keys()
        fin_keys_set = set(uniq_keys).union(set(keys))
        uniq_keys = list(fin_keys_set)
    connect(uniq_keys)
