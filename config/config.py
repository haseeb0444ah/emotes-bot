class config:
    # Basic configuration: If you are unsure how to obtain the Bot ID, simply start the bot and it will be logged in the console.
    prefix = '/'
    botID = '647de80cd0163e6dd3f3449c'
    botName = 'SycoBot'
    ownerName = '_HaseeB_'
    roomName = 'Cheap Grabs'
    coordinates = {
        'x': 17.5,
        'y': 0.10000000149011612,
        'z': 10.5,
        'facing': 'FrontRight'
    }


class loggers:
    # The following settings are related to events. Each event log can be enabled or disabled. Note that turning these off will not affect their usage in the game.
    SessionMetadata = True
    messages = True
    whispers = True
    joins = True
    leave = True
    tips = True
    emotes = False
    reactions = False
    userMovement = False


class messages:
    # The following are optional and serve as a basic usage example for calling messages and replacing variables.
    invalidPosition = "Your position could not be determined."
    invalidPlayer = "{user} is not in the room."
    invalidUser = "User {user} is not found."
    invalidUsage = "Usage: {prefix}{commandName}{args}"
    invalidUserFormat = "Invalid user format. Please use '@username'."


class permissions:
    # You can add as many IDs as you want, for example: ['id1', 'id2'].
    owners = ['636a7d9ecc79c4ca4f7da5ef','64c1e24c02e13e95a9374521','64c98e95c9b672a10bfd2405']
    moderators = ['636a7d9ecc79c4ca4f7da5ef','64c1e24c02e13e95a9374521','64c98e95c9b672a10bfd2405']


class authorization:
    # To obtain your token, visit https://highrise.game/ and log in. Then, go to the settings and create a new bot. Accept the terms and generate a token.
    # To obtain your room ID, go to the game and navigate to the top right corner where the player list is displayed. Click on "Share this room" and copy the ID.
    room = '65130b5dbf60263900835226'
    token = 'e0b1d9fc1cf8fcea5bd95a65f029576fd1e0a873c70771549c3d454d9db005f9'
