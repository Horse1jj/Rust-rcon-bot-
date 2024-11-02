# Rust-rcon-bot-

# Discord Rust Server Management Bot

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
- `discord.py` library
- Any additional libraries specified in the installation section

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/discord-rust-bot.git
   cd discord-rust-bot
   
**Create a virtual environment (optional but recommended)**:


python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

**Install required packages: Install the necessary Python packages using pip**:


`pip install discord.py`

**Make sure to install any other packages you might need based on your project’s requirements.
Configuration**

Create a config.json file in the root directory:
`
{
    "token": "YOUR_BOT_TOKEN_HERE",
    "prefix": "!",
    "status": {
        "activity": "Playing Rust"
    }
}
` 

Replace "YOUR_BOT_TOKEN_HERE" with your actual Discord bot token.

**Set up roles.json to define admin and mod roles by their IDs**:


`
{
    "admin": ["ROLE_ID_1", "ROLE_ID_2"],
    "mod": ["ROLE_ID_3", "ROLE_ID_4"]
}
`

**Set up servers.json to define your Rust servers**:


`
{
    "rust1": {
        "ip": "YOUR_SERVER_IP",
        "port": "YOUR_SERVER_PORT",
        "rcon_password": "YOUR_RCON_PASSWORD"
    }
}
`

## Usage

Run the bot: Execute the bot.py script to start the bot:


`python bot.py`

Invite the bot: Make sure to invite your bot to your Discord server with the necessary permissions, including sending messages and managing roles.

Interact with the bot: Use the configured command prefix (default is !) followed by commands to interact with the bot. For example, to ban a player, you can use: #

