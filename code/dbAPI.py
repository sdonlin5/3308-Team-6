
"""
This is the datasbase API for the Team Six Project
Last Modifeied: 3/10/2024 By: Patrick Sharp
"""

# Imports
import sqlite3
from datetime import datetime

"""
@Parm db_filename: Name of the database file to open or create
@Return 0, Void Function, But returns 0 when working successfully
This function will connect to the database file given to create Player, Scores, and ___ tables if they do not exist already
Author(s): Patrick Sharp
Last Mofdified: 3/10/2024
"""
def create(db_filename: str):
    if type(db_filename) is not str or not db_filename:
        raise ValueError
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    

    # The date will be stored as an VARCHAR in yy-mm-dd format
    # date will come from datetime.now() and only save the yyyy-mm-dd format as a string
    c.execute("CREATE TABLE IF NOT EXISTS Players (playerID INT, playerName VASRCHAR(3), lastLoginDate VARCHAR(10) );")
    c.execute("CREATE TABLE IF NOT EXISTS Scores (playerID INT, score INT, date VARCHAR(10) );")
    c.execute("CREATE TABLE IF NOT EXISTS Temp (playerID INT, playerEmail VARCHAR(45) );")
    
    conn.commit()
    conn.close()
    return 0


"""
@Parm db_filename: Name of the database file to open or create
@Parm playerID: The playerID connected to the score being added
@Parm score: The players score achieved
@Return 0, Void Function, But returns 0 when working successfully
This function will connect to the database file given to add a players score to the Scores table in the DB
Author(s): Patrick Sharp
Last Mofdified: 3/11/2024
"""
def addScore(db_filename: str, playerID: int, score: int):
    
    # Grab the date and make it a string in the yyyy-mm-dd format
    date = str(datetime.now())
    date = date[0:10] 
    return None