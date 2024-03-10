"""
This is the datasbase API for the Team Six Project
Last Modifeied: 3/10/2024 By: Patrick Sharp
"""

# Imports
import sqlite3



"""
@Parm db_filename: Name of the database file to open or create
@Return 0, Void Function, But returns 0 when working successfully
This function will connect to the database file given to create Player, Scores, and ___ tables if they do not exist already
Author: Patrick Sharp
Last Mofdified: 3/10/2024
"""
def create(db_filename):
    if type(db_filename) is not str:
        raise ValueError
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    
    """
    For the date it will be stored as an INT as Unix Time, 
    the number of seconds since 1970-01-01 00:00:00 UTC, and use functions outlined in: 
    https://www.sqlite.org/lang_datefunc.html to covert to a date format if needed
    Also, see: https://www.sqlite.org/datatype3.html for more info on data types in sqlite and info on dates
    """
    c.execute("CREATE TABLE IF NOT EXISTS Players (playerID INT, playerName VASRCHAR(3), lastLoginDate INT );")
    c.execute("CREATE TABLE IF NOT EXISTS Scores (playerID INT, score INT, date INT );")
    c.execute("CREATE TABLE IF NOT EXISTS Temp ( playerID INT, playerEmail VARCHAR(45));")
    
    conn.commit()
    conn.close()
    return 0

