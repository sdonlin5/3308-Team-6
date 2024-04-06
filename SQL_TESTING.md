
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

&nbsp;&nbsp;&nbsp;&nbsp;Verify the scores and player info is being added to the table properly

Description: 

   &nbsp;&nbsp;&nbsp;&nbsp;Test the addScore() function in the dbAPI

Pre-conditions: 

   &nbsp;&nbsp;&nbsp;&nbsp;The test is using a valid playerID, playerName, score, and gameID

Test Steps:
    
   1. Verify only valid database filenames, playerIds, playerNames, and scores are given to the function
   2. Add the playerId, playerName, score, date, and gameID to the table from the given database filename.
   3. Retrieve the data from the table in the database.
   4. Verify the playerId, playerName, score, date, and gameID are placed correctly in the table.
    
Expected Result: 

   &nbsp;&nbsp;&nbsp;&nbsp;The added score should match the retrieved score.
    
Actual Result: 

   &nbsp;&nbsp;&nbsp;&nbsp;The added playerId, playerName, score, date, and gameID matches the retrieved values.
    
Status: 

   &nbsp;&nbsp;&nbsp;&nbsp;Pass.
    
Notes: 

   &nbsp;&nbsp;&nbsp;&nbsp;N/A.
    
#### Get Top Ten Scores Test

Use case:

   &nbsp;&nbsp;&nbsp;&nbsp;Verify that the getTopTenScores() grabs the top ten scores from the table.

Description: 

   &nbsp;&nbsp;&nbsp;&nbsp;Test getTopTenScores() function.
    
Pre-conditions: 

   &nbsp;&nbsp;&nbsp;&nbsp;We are using a valid playerID and playerName.
    
Test Steps:

   1. Add a list of 10+ scores to the table.
   2. Retrieve the top ten scores from the table.
   3. Verify that it grabed the top ten scores in descending order.
    
Expected Result:

   &nbsp;&nbsp;&nbsp;&nbsp;The retrieved scores should be the top ten scores based on the score value.
    
Actual Result: 

   &nbsp;&nbsp;&nbsp;&nbsp;The retrieved scores are the top ten scores based on fro the list of scores.
    
Status: 

   &nbsp;&nbsp;&nbsp;&nbsp;Pass.
    
Notes:

   &nbsp;&nbsp;&nbsp;&nbsp;N/A



## Scores Table
### Description: 
This table stores the essential profile information of players.

### Fields:
playerID (INT): A unique identifier for the player.<br>
playerName (VARCHAR(50)): The name of the player.<br>
dateCreated (DATE): The date when the player's profile was created.<br>
playEmail (VARCHAR(100)): The player’s email address.<br>

### Tests:

#### Add PlayerProfile Test

Use case:<br>
Verify that the player profile is correctly added to the table.

Description: <br>
Test the addPlayerProfile() function within the database API.

Pre-conditions: <br>
Valid playerID, playerName, dateCreated, and playEmail are used for the test.

Test Steps:<br>
1. Ensure only valid database filenames, playerID, playerName, and playEmail are given to the function.<br>
2. Add the playerID, playerName, dateCreated, and playEmail to the table using the provided database filename.<br>
3. Retrieve the data from the table in the database.<br>
4. Verify that the playerID, playerName, dateCreated, and playEmail are correctly placed in the table.<br>

Expected Result:<br>
The added player profile should match the retrieved profile.<br>

Actual Result:<br>
The added playerID, playerName, dateCreated, and playEmail match the retrieved values.<br>

Status:<br>
Pass.

Notes:<br>
N/A.

#### Retrieve PlayerProfile Test

Use case:<br>
Verify that the player profile can be correctly retrieved using a given playerID.<br>

Description:<br>
Test the getPlayerProfile() function within the database API.<br>

Pre-conditions:<br>
The playerID used for testing must be valid and exist in the database.<br>

Test Steps:<br>
1. Provide a valid playerID to the function.<br>
2. Retrieve the corresponding profile information from the database.<br>
3. Verify that the information retrieved matches the playerID provided.<br>

Expected Result:<br>
The retrieved profile information should correspond to the given playerID.<br>

Actual Result:<br>
The retrieved profile information matches the given playerID.<br>

Status:<br>
Pass.<br>

Notes:<br>
N/A.<br>



































