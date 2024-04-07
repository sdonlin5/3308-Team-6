const config = {
    type: Phaser.AUTO, 
    width: 3140, 
    height: 720, 
    backgroundColor: '#87CEEB', 
    physics: {
        default: 'arcade', 
        arcade: {
            gravity: {y: 180}, 
            debug: true
        }
    },
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

const game = new Phaser.Game(config);
var reggie; 
var direction;
var jump;
var ground;
var platforms;
var smallClouds;
var largeClouds;
var platform;
var playerPositionText;
var platformPositionText;

function preload() {
    //this.load.image('sky', './assets/sky.png'); 
    this.load.image("groundTile", "./assets/ground.png"); 
    this.load.image('dog', "./assets/dog.png");
    this.load.image('brick', './assets/brick.png'); 
}

function create() {
    // Ground
    ground = this.physics.add.staticGroup(); 
    ground.create(0, 620, 'groundTile').setOrigin(0,0).setScale(2).refreshBody();
    
    // Platforms
    platforms = this.physics.add.group(); 
    spawnPlatform(4); // Spawn initial platforms

    // Character
    reggie = this.physics.add.sprite(100, 100, 'dog');
    reggie.setBounce(0.2); 
    reggie.setCollideWorldBounds(true);

    // Colliders
    this.physics.add.collider(reggie, ground); 
    this.physics.add.collider(reggie, platforms); 

    // Character movement keys
    direction = this.input.keyboard.createCursorKeys();
    jump = this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.SPACE);
    
    // Camera setup
    this.cameras.main.setBounds(0, 0, Infinity, 720); // Wide bounds to allow sidescrolling
    this.cameras.main.startFollow(reggie, true, 0.1, 0); // Follow the player vertically

    // For debugging
    playerPositionText = this.add.text(16, 16, '', { fontSize: '24px', fill: '#ffffff' }).setScrollFactor(0);
    platformPositionText = this.add.text(16, 700, '', { fontSize: '24px', fill: '#ffffff' }).setScrollFactor(0);
}

// Platform function
function spawnPlatform(numBricks) {
    const brickSpriteWidth = 64; // Brick Sprite width
    const xOffset = 700 + brickSpriteWidth; // Initial x position 
    const initialY = 360; // Needs to be adjusted for height

    for (let i = 0; i < numBricks; i++) {
        const platform = platforms.create(xOffset + i * brickSpriteWidth, initialY, 'brick').setOrigin(0, 0);
        platform.setImmovable(true); // Stops platform from moving on collision
        platform.body.allowGravity = false; // Disable gravity for the platform
}
}

// Update 
function update() {

    // Movement controls
    if (direction.left.isDown)
    {
        reggie.setVelocityX(-160); 
    }
    else if (direction.right.isDown)
    {
        reggie.setVelocityX(160); 
        
        // Update platform when moving right
        const lastBrickSprite = platforms.getLast(true);
        if (lastBrickSprite.x + lastBrickSprite.displayWidth < 0){
            spawnPlatform(1); 
        }
    }

    else 
    {
        reggie.setVelocityX(0); 
    }

    // Player jumps when spacebar is pressed and the body is touching the ground
    if (Phaser.Input.Keyboard.JustDown(jump) && reggie.body.touching.down)
    {
        reggie.setVelocityY(-350); // Set jump velocity
    }

    // Debug text
    playerPositionText.setText('Player Position: ' + reggie.x.toFixed(2) + ', ' + reggie.y.toFixed(2));
    
    if (platforms.getChildren().length > 0) {
        const firstPlatform = platforms.getFirst(true);
        platformPositionText.setText('Platform Position: ' + firstPlatform.x.toFixed(2) + ', ' + firstPlatform.y.toFixed(2));
    }
}