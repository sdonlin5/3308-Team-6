
"""
These are the unit tests for the datasbase API used in the Team Six Project 
Last Modifeied: 3/10/2024 By: Patrick Sharp
"""

# Imports
import sqlite3
from datetime import datetime
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
    This test also checks that the function works as intended
    Author(s): Patrick Sharp
    Last Modified: 3/10/2024
    """
    def test_create(self):
        
        global db_filename
        
        # Test to check for a valid db_filename data types
        invalid_db_filename_data_types = [
            None,
            '',
            7,
            3.14,
            [],
            ['db_filename'],
            {'db_filename':0}
        ]
        
        for dataType in invalid_db_filename_data_types:
            with self.assertRaises(ValueError, msg="The database file name given is not a valid option"):
                dbAPI.create(dataType)
            
        # Test the function returns sucsessfully when given a valid db_filename
        assert (dbAPI.create(db_filename)) == 0, "The create() function failed (did not return a value of 0)"
        
        # Testing the table creation in the global test database
        conn = sqlite3.connect(db_filename)
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        
        # Check that the needed tables are created and named properly
        assert tables[0][0] == "Players", "The create() function did not make a Players table"
        assert tables[1][0] == "Scores", "The create() function did not make Scores table"
        assert tables[2][0] == "Temp", "The create() function did not make a Temp table"
    
    
    
    
    
    """
    This test checks for input errors in the database filename, playerId, and/or score. 
    This test also checks that the function works as intended
    Author(s): Patrick Sharp
    Last Modified: 3/10/2024
    """
    def test_addScore(self):
        
        global db_filename
        playerID = 1
        score = 420
        
        # Test to check for a valid db_filename data types
        invalid_db_filename_data_types = [
            None,
            '',
            7,
            3.14,
            [],
            ['db_filename'],
            {'db_filename':0}
        ]
        
        for dataType in invalid_db_filename_data_types:
            with self.assertRaises(ValueError, msg="The database file name given is not a valid option: {}".format(dataType)):
                dbAPI.addScore(dataType, playerID, score)
            
        # Test tocheck that the playerID is a valid data type (int > 0)
        invalid_playerIDs = [
            None,
            '',
            'playerID',
            3.14,
            [],
            ['playerID'],
            [1],
            0,
            -1,
            {'playerID':1}
        ]
        
        for dataType in invalid_playerIDs:
            with self.assertRaises(ValueError, msg="The playerID given is not a valid option: {}".format(dataType)):
                dbAPI.addScore(db_filename, dataType, score)
            
        # Test to check that the score is a valid data type (int > 0)
        # NOTE: MIGHT WANT TO STORE A SCORE OF ZERO SO REMOVE THAT IF THAT"S THE CASE
        invalid_score = [
            None,
            '',
            '777',
            0,
            -1,
            [],
            [777],
            {'score':7777}
        ]
        
        for dataType in invalid_playerIDs:
            with self.assertRaises(ValueError, msg="The score given is not a valid option: {}".format(dataType)):
                dbAPI.addScore(db_filename, playerID, dataType)
                
        
        # Test the function returns sucsessfully when given a valid db_filename
        assert (dbAPI.addScore(db_filename, playerID, score)) == 0, "The addScore() function failed (did not return a value of 0)"
        
        # Grab the date that should be appened to the Scores table from the call above
        date = str(datetime.now())
        date = date[0:10] 
        
        # Testing if the addScores function used above inserted the supplied values to the Scores table
        conn = sqlite3.connect(db_filename)
        c = conn.cursor()
        c.execute("SELECT * FROM Scores;")
        tables = c.fetchall()
        
        assert tables[-1][0] == 1, "The addScores() function did not append the values to the Scores table with the supplied playerID"
        assert tables[-1][1] == 420, "The addScores() function did not append the values to the Scores table with the supplied score"
        assert tables[-1][2] == date, "The addScores() function did not append the values to the Scores table with the supplied date"
        

            
            
            
if __name__ == '__main__':
    unittest.main()    