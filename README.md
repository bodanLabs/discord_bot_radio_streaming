# Discord Radio Bot

## Overview
This Discord bot allows users to play and stop a radio stream within a voice channel. It's built using the `discord.py` library and the `FFmpeg` library for audio streaming.

## Features
- Play radio stream in a voice channel
- Stop playing the radio stream
- Automatic reconnection to the stream in case of disconnection

## Installation

### Prerequisites
- Python 3.6 or higher
- `discord.py` library
- `FFmpeg` installed and accessible in your system's PATH

### Setup
1. Clone the repository:
```git clone [discord_bot_radio_streaming](https://github.com/bodanLabs/discord_bot_radio_streaming.git)https://github.com/bodanLabs/discord_bot_radio_streaming.git```
2. Install the required Python packages:
```pip install -r requirements.txt```
3. Add your Discord bot token to the script or use an environment variable to keep it secure.

### Running the Bot
Run the bot using Python:
```python bot.py```


## Usage
Once the bot is running and invited to your Discord server, you can use the following commands within any text channel:

- `.play` or `.p` or `.pla`: Connects to your voice channel and starts playing the radio stream.
- `.stop` or `.s` or `.sto`: Stops the radio stream and disconnects the bot from the voice channel.

## Commands
| Command | Alias | Description |
| ------- | ----- | ----------- |
| .play   | .p, .pla | Starts playing the radio stream in the voice channel. |
| .stop   | .s, .sto | Stops the radio stream and disconnects from the channel. |

## Contributing
Contributions to the project are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with descriptive commit messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

Please ensure your code adheres to the project's coding standards and include any necessary tests.

## Acknowledgements
- Thanks to the `discord.py` community for the comprehensive library.
- `FFmpeg` for the audio streaming capabilities.
