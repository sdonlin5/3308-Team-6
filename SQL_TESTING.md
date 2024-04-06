
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



## PlayerProfile Table
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


## PlayerState Table

### Description:<br>
This table captures the current state of a player within the game, such as health, score, level, and position.<br>

### Fields:<br>
playerID (INT): The unique identifier for the player.<br>
currentHealth (INT): The current health of the player.<br>
currentScore (INT): The current score of the player.<br>
currentLevel (INT): The current level the player is on.<br>
currentPosition (VARCHAR(100)): The current position of the player in the game world.<br>

### Tests:

#### Update PlayerState Test

Use case:<br>
Verify that a player's state is correctly updated in the table.<br>

Description:<br>
Test the updatePlayerState() function.<br>

Pre-conditions:<br>
A valid playerID and the data to update the state must exist.<br>

Test Steps:<br>
1. Provide valid playerID and the new state data to the function.<br>
2. Update the player's state in the database.<br>
3. Retrieve the updated data and verify that the changes are correctly applied.<br>

Expected Result:<br>
The updated state of the player as retrieved should match the intended changes.<br>

Actual Result:<br>
The updated data retrieved matches the intended changes.<br>

Status:<br>
Pass.<br>

Notes:<br>
N/A.<br>

#### Retrieve PlayerState Test

Use case:<br>
Verify that the state of a player can be correctly retrieved using a given playerID.<br>

Description:<br>
Test the getPlayerState() function.<br>

Pre-conditions:<br>
The playerID to be used for testing must be valid and exist in the database.<br>

Test Steps:<br>
1. Provide a valid playerID to the function.<br>
2. Retrieve the state information corresponding to the provided playerID.<br>
3. Verify that the retrieved information matches the playerID.<br>

Expected Result:<br>
The retrieved state information should correctly correspond to the provided playerID.<br>

Actual Result:<br>
The retrieved state information matches the provided playerID.<br>

Status:<br>
Pass.<br>

Notes:<br>
N/A.<br>


## Inventory Table

### Description:
This table tracks the items that each player has in their inventory, including the quantity of each item.<br>

### Fields:<br>
inventoryID (INT): The unique identifier for the inventory entry.<br>
playerID (INT): The unique identifier for the player who owns the item.<br>
itemID (INT): The unique identifier for the item.<br>
quantity (INT): The quantity of the item in the player's inventory.<br>

### Tests:

#### Add Item to Inventory Test

Use case:<br>
Verify that items are correctly added to a player's inventory.<br>

Description:<br>
Test the addItemToInventory() function.<br>

Pre-conditions:<br>
Valid inventoryID, playerID, itemID, and quantity are provided.<br>

Test Steps:<br>
1. Provide the function with valid inventoryID, playerID, itemID, and quantity.<br>
2. Add the item to the player's inventory.<br>
3. Retrieve the item data from the inventory and verify that it has been added correctly.<br>

Expected Result:<br>
The item should be added to the inventory with the correct playerID, itemID, and quantity.<br>

Actual Result:<br>
The added item in the inventory matches the provided playerID, itemID, and quantity.<br>

Status:<br>
Pass.<br>

Notes:<br>
N/A.<br>

#### Get Inventory Items Test

Use case:<br>
Verify that the inventory items for a specific playerID are correctly retrieved.<br>

Description:<br>
Test the getInventoryItems() function.<br>

Pre-conditions:<br>
A valid playerID is provided and the player has items in their inventory.<br>

Test Steps:<br>
1. Provide the function with a valid playerID.<br>
2. Retrieve the list of items from the player's inventory.<br>
3. Verify that the retrieved list matches the items and quantities expected for the given playerID.<br>

Expected Result:<br>
The retrieved list of inventory items should correctly reflect the player’s actual inventory for the specified playerID.<br>

Actual Result:<br>
The retrieved inventory items match the actual items and quantities for the provided playerID.<br>

Status:<br>
Pass.<br>

Notes:<br>
N/A.<br>


## ActiveEffect Table

### Description:
This table records the active effects (buffs or debuffs) applied to players. Each effect has a type, start time, and duration, detailing how and when they influence the player.<br>

### Fields:<br>
effectID (INT): The unique identifier for the effect.<br>
playerID (INT): The unique identifier for the player affected by the effect.<br>
type (ENUM('buff', 'debuff')): The type of effect applied, categorizing it as either a buff (positive effect) or debuff (negative effect).<br>
startTime (DATETIME): The time at which the effect was applied.<br>
duration (INT): The duration for which the effect is active, measured in seconds.<br>

### Tests:

#### Apply Effect Test

Use case:<br>
Verify that effects are correctly applied to players and recorded in the database.<br>

Description:<br>
Test the function that applies effects to ensure it records them correctly.<br>

Pre-conditions:<br>
Valid effectID, playerID, type, startTime, and duration must be provided.<br>

Test Steps:<br>
1. Execute the function to apply an effect using the provided parameters.<br>
2. Retrieve the effect details from the database.<br>
3. Verify that the database records match the details provided, including the start time and duration.<br>

Expected Result:<br>
The database should have an accurate record of the effect applied, matching the playerID, type, startTime, and duration.<br>

Actual Result:<br>
The effect details in the database correctly reflect the application details.<br>

Status:<br>
Pass.<br>

Notes:<br>
N/A.<br>

#### Check Effect Expiry Test

Use case:<br>
Verify that the system correctly identifies when an effect has expired based on its duration.<br>

Description:<br>
Test the mechanism that checks for the expiry of effects to ensure it accurately reflects the startTime and duration.<br>

Pre-conditions:<br>
An effect with a known startTime and duration is in the system, and the current time surpasses the effect's duration.<br>

Test Steps:<br>
1. Calculate the expected expiry time based on the startTime and duration.<br>
2. Check the system to confirm that the effect is no longer active after this time.<br>
3. Verify that the system has correctly updated the status of the effect as expired.<br>

Expected Result:<br>
The system should accurately identify and update the effect as expired once the duration surpasses the current time.<br>

Actual Result:<br>
The effect is correctly marked as expired in the system.<br>

Status:<br>
Pass.<br>

Notes:<br>
N/A.<br>


## Item Table
### Description:<br>
This table stores detailed information about various items within the game, including their effects, duration, and rarity.<br>

### Fields:<br>
itemID (INT): The unique identifier for the item.<br>
itemName (VARCHAR(100)): The name of the item.<br>
type (ENUM('buff', 'debuff')): The type of effect the item provides, whether it is a buff (enhances player abilities) or a debuff (reduces player abilities).<br>
effect (VARCHAR(255)): A description of the effect that the item has when used.<br>
duration (INT): The duration in seconds for which the effect lasts after the item is used.<br>
rarity (ENUM('common', 'uncommon', 'rare', 'epic', 'legendary')): The rarity level of the item, indicating its commonness or uniqueness within the game.<br>

### Tests:<br>

#### Create Item Test

Use case:<br>
Verify that new items are correctly created and recorded in the database.<br>

Description:<br>
Test the function that adds new items to ensure it correctly captures all item details.<br>

Pre-conditions:<br>
Valid details such as itemID, itemName, type, effect, duration, and rarity are provided.<br>

Test Steps:<br>
1. Execute the function to add a new item with the provided details.<br>
2. Retrieve the newly created item from the database.<br>
3. Verify that all details match the input provided, including name, effect type, duration, and rarity.<br>

Expected Result:<br>
The database should reflect the newly added item with accurate details as provided.<br>

Actual Result:<br>
The details of the newly added item in the database match the provided specifications.<br>

Status:<br>
Pass.<br>

Notes:<br>
N/A.<br>

#### Retrieve Item Details Test

Use case:<br>
Verify that the details of an existing item can be correctly retrieved from the database.<br>

Description:<br>
Test the function that fetches item details based on itemID.<br>

Pre-conditions:<br>
An existing itemID is used for retrieval.<br>

Test Steps:<br>
1. Execute the function to retrieve details for the specified itemID.<br>
2. Verify that the retrieved item details match the expected information, including the item’s name, effect, duration, and rarity.<br>

Expected Result:<br>
The details retrieved for the item should match the stored values in the database.<br>

Actual Result:<br>
The retrieved item details accurately reflect the information stored in the database.<br>

Status:<br>
Pass.<br>

Notes:<br>
N/A.<br>


## Obstacle Table
### Description:<br>
This table stores information about various obstacles within the game. Each record includes details about the obstacle's name, severity, and location, providing a way to manage and interact with in-game challenges.<br>

### Fields:<br>
obstacleID (INT): The unique identifier for the obstacle.<br>
obstacleName (VARCHAR(100)): The name of the obstacle.<br>
severity (INT): A numeric value indicating the difficulty or impact of the obstacle on players.<br>
location (VARCHAR(100)): The in-game location where the obstacle is found.<br>

### Tests:

#### Create Obstacle Test

Use case:<br>
Verify that obstacles are correctly created and added to the database.<br>

Description:<br>
Test the function that creates and records new obstacles in the game environment.<br>

Pre-conditions:<br>
Valid obstacleID, obstacleName, severity, and location must be provided.<br>

Test Steps:<br>
1. Use the provided details to add a new obstacle to the database via the function.<br>
2. Retrieve the obstacle details from the database.<br>
3. Verify that the details in the database match those provided, including the name, severity, and location.<br>

Expected Result:<br>
The database should reflect the newly created obstacle with accurate details as provided.<br>

Actual Result:<br>
The details of the newly added obstacle in the database match the provided specifications.<br>

Status:<br>
Pass.<br>

Notes:<br>
N/A.<br>

#### Retrieve Obstacle Details Test

Use case:<br>
Verify that details of an existing obstacle can be accurately retrieved from the database.<br>

Description:<br>
Test the function that fetches obstacle details based on obstacleID.<br>

Pre-conditions:<br>
An existing obstacleID is used for retrieval.<br>

Test Steps:<br>
1. Execute the function to retrieve details for the specified obstacleID.<br>
2. Verify that the retrieved obstacle details match the expected information, including the obstacle's name, severity, and location.<br>

Expected Result:<br>
The details retrieved for the obstacle should match the stored values in the database.<br>

Actual Result:<br>
The retrieved obstacle details accurately reflect the information stored in the database.<br>

Status:<br>
Pass.<br>

Notes:<br>
N/A.<br>

















