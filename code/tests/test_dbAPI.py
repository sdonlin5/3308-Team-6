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


class addProductTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    # Setup by making the db and tables and filling them
    def setUp(self):
        db_filename = 'testDB'

    # Remove the db file
    def tearDown(self):
        try:
            os.remove("testDB")
        except:
            print("Error deleting test database")
            
    
    
    """
    This test check for input errors in the database filename, starting off with ValueTypeErrors
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
            
            
if __name__ == '__main__':
    unittest.main()