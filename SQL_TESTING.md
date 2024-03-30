
## Scores Table
### Description: 
This table stores the scores of players for different games.

### Fields:

playerID (INT): The unique identifier for the player.

playerName (CHAR(3)): The name of the player limited to three characters.

date (CHAR(10)): The date when the score was recorded in the format YYYY-MM-DD.

gameID (INT): The unique identifier for the game.

### Tests:

#### Add Score Test

Use case:

    Verify the scores and player info is being added to the table properly

Description: 

    Test the addScore() function in the dbAPI

Pre-conditions: 

    The test is using a valid playerID, playerName, score, and gameID

Test Steps:
    
    1. Verify only valid database filenames, playerIds, playerNames, and scores are given to the function
    2. Add the playerId, playerName, score, date, and gameID to the table from the given database filename.
    3. Retrieve the data from the table in the database.
    4. Verify the playerId, playerName, score, date, and gameID are placed correctly in the table.
    
Expected Result: 

    The added score should match the retrieved score.
    
Actual Result: 

    The added playerId, playerName, score, date, and gameID matches the retrieved values.
    
Status: 

    Pass.
    
Notes: 

    N/A.
    
#### Get Top Ten Scores Test

Use case:

    Verify that the getTOpTenScores() grabs the top ten scores from the table.

Description: 

    Test getTOpTenScores() function.
    
Pre-conditions: 

    We are using a valid playerID and playerName.
    
Test Steps:

    1. Add a list of 10+ scores to the table.
    2. Retrieve the top ten scores from the table.
    3. Verify that it grabed the top ten scores in descending order.
    
Expected Result:

    The retrieved scores should be the top ten scores based on the score value.
    
Actual Result: 

    The retrieved scores are the top ten scores based on fro the list of scores.
    
Status: 

    Pass.
    
Notes:

    N/A.