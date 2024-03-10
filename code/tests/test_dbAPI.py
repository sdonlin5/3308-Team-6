"""
This is the unit tests for the datasbase API for the Team Six Project
Last Modifeied: 3/10/2024 By: Patrick Sharp
"""


import sqlite3
import unittest
import os
import sys

# Add the project's root directory to sys.path 
# (This is the only working way I have to grab the dbAPI file, If you know a better way feel free to change)
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, project_root)
import dbAPI

# Global Variables
db_filename = 'testDB'

class dbAPITestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    # Setup by making the db and tables and filling them
    def setUp(self):
        global db_filename
        dbAPI.create(db_filename)

    # Remove the db file
    def tearDown(self):
        try:
            global db_filename
            os.remove(db_filename)
        except:
            print("Error deleting test database")
            
    
    
    """
    This test checks for input errors in the database filename, starting off with ValueTypeErrors
    Author: Patrick Sharp
    Last Modified: 3/10/2024
    """
    def test_create(self):
        with self.assertRaises(ValueError, msg="The database file name given is not a valid option (None)"):
            dbAPI.create(None)
        with self.assertRaises(ValueError, msg="The database file name given is not a valid option (int)"):
            dbAPI.create(7)
        with self.assertRaises(ValueError, msg="The database file name given is not a valid option (float)"):
            dbAPI.create(3.12)
        with self.assertRaises(ValueError, msg="The database file name given is not a valid option (empty list)"):
            dbAPI.create([])
        with self.assertRaises(ValueError, msg="The database file name given is not a valid option (list)"):
            dbAPI.create(['a','b','c'])
        
        # Testing the table creation in the setUp database
        global db_filename
        conn = sqlite3.connect(db_filename)
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
            
        assert tables[0][0] == "Players"
        assert tables[1][0] == "Scores"
        assert tables[2][0] == "Temp"
            
            
if __name__ == '__main__':
    unittest.main()