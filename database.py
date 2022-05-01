from mysql import connector
from config import *
import hashlib, random
import time

#connect To The Database
my_db = connector.connect (
    	user = USERNAME,
    	password = PASSWORD,
    	host = HOST,
    	database = DATABASE
	)
mycursor = my_db.cursor()

def storedMessage(ip, msg):
    sql = f"""
            INSERT INTO messages (ip, message, messagetime) values ("{ip}", "{msg}", {int(time.time())})
            """
    mycursor.execute(sql)
    my_db.commit()