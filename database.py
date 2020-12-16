import psycopg2 as postgres 
import uuid
from datetime import datetime
import logging
import traceback 
import csv

connection = postgres.connect(host="localhost", database="client_app_dev", user="postgres", password="postgres")
cursor =  connection.cursor()

def read_csv(): 
    global connection
    global cursor
    with open("C:/buzz_api_poc/sales_data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        # csv_reader = csv_reader[:200000]
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                insert_query = """insert into sales (id, date, product, region, sales, inserted_at, updated_at) values (%s, %s, %s, %s, %s, %s, %s)"""                                
                actual_values = (line_count, datetime.strptime(row[2], '%Y-%m-%d').date(), row[1], row[0], float(row[3]), datetime.now(), datetime.now())
                try: 
                    cursor.execute(insert_query, actual_values)
                    connection.commit()
                    line_count += 1

                except Exception as e: 
                    logging.error(traceback.format_exc())
                    print("Errora")
                    break

read_csv()


cursor.close()
connection.close()
