"""
This is the datasbase API for the Team Six Project
Last Modifeied: 3/10/2024 By: Patrick Sharp
"""

# Imports
import sqlite3



"""
@Parm db_filename: Name of the database file to open or create
@Return 0, Void Function, But returns 0 when working successfully
This function will connect to the database file given to create Store, Store_Product, Product, and Category tables if they do not exist already
Author: Patrick Sharp
Last Mofdified: 3/10/2024
"""
def create(db_filename):
    return None