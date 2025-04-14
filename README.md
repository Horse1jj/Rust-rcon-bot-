# Rust-rcon-bot-

This is a Discord bot designed to manage Rust community servers using RCON commands. It allows users with appropriate roles to execute various server commands directly from Discord.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Commands](#commands)

## Features

- Execute server commands (ban, kick, mute, etc.)
- Manage server settings (change server name, set weather conditions)
- Help command to list available commands
- Multi-server support

## Requirements

- Python 3.8 or higher
- Any additional libraries specified in the installation section

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/Horse1jj/Rust-rcon-bot-
cd Rust-rcon-bot-
```
   
## Create a virtual environment (optional but recommended)


python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

## Install required packages: 

`pip install -r requirements.txt`

## Create a config.json file in the root directory:

``` json
{
    "token": "YOUR_BOT_TOKEN_HERE",
    "prefix": "!",
}

``` 

Replace "YOUR_BOT_TOKEN_HERE" with your actual Discord bot token.

## Set up roles.json to define admin and mod roles by their IDs 


```json

{
    "admin": ["ROLE_ID_1", "ROLE_ID_2"],
    "mod": ["ROLE_ID_3", "ROLE_ID_4"]
}

```

## Set up servers.json to define your Rust servers


```json
{
    "rust1": {
        "ip": "YOUR_SERVER_IP",
        "port": "YOUR_SERVER_PORT",
        "rcon_password": "YOUR_RCON_PASSWORD"
    }
}

```

## Usage

Run the bot: Execute the bot.py script to start the bot:


`python bot.py`

Invite the bot: Make sure to invite your bot to your Discord server with the necessary permissions, including sending messages and managing roles.

Interact with the bot: Use the configured command prefix (default is !) followed by commands to interact with the bot. For example, to ban a player, you can use: #


## Command List/FAQ

### Admin Commands
- `!ban <username> <server>`  
  Bans a player from the specified server.  
  **Example**: `!ban q-player rust1`

- `!kick <username> <server>`  
  Kicks a player from the specified server.  
  **Example**: `!kick q-player rust1`

- `!mute <username> <server>`  
  Mutes a player in-game, disabling their chat capabilities.  
  **Example**: `!mute q-player rust1`

- `!unmute <username> <server>`  
  Unmutes a previously muted player, allowing them to chat again.  
  **Example**: `!unmute q-player rust1`

- `!giveitem <player_name> <item_name> <server>`  
  Gives a specified item to a player on the specified server.  
  **Example**: `!giveitem q-player "Wooden Bow" rust1`

- `!quit`  
  Saves everything and stops the server.  
  **Example**: `!quit`

- `!weather.fog`  
  Sets the fog weather on the server.  
  **Example**: `!weather.fog`

- `!weather.wind`  
  Sets the wind weather on the server.  
  **Example**: `!weather.wind`

- `!weather.rain <value>`  
  Sets the rain weather on the server to the specified value.  
  **Example**: `!weather.rain 0.5`

### Mod Commands
- `!mute <username> <server>`  
  Mutes a player in-game chat, preventing them from speaking.  
  **Example**: `!mute q-player rust1`

- `!unmute <username> <server>`  
  Unmutes a player in-game chat, allowing them to speak again.  
  **Example**: `!unmute q-player rust1`

### General Commands
- `!players <server>`  
  Displays the current players on the specified server.  
  **Example**: `!players rust1`

- `!servers`  
  Lists all available servers that the bot can manage.  
  **Example**: `!servers`

- `!serverinfo <server>`  
  Displays information about the specified server.  
  **Example**: `!serverinfo rust1`

- `!help`  
  Displays a list of all available commands along with their descriptions.  
  **Example**: `!help`


