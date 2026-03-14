# Telegram Torrent Downloader Bot

A Python-based Telegram bot that allows users to download files from torrents by sending commands directly in Telegram.

The bot listens for commands from users and triggers torrent downloads on the server. It acts as a simple remote interface to manage torrent downloads without directly accessing the machine.

---

## Features

- Download torrents using Telegram commands
- Supports **magnet links**
- Runs as a background service
- Simple command-based interaction
- Automatically downloads files to the configured directory

---

## How It Works

1. A user sends a command to the Telegram bot.
2. The bot receives the command through the Telegram Bot API.
3. The bot parses the command and extracts the torrent link.
4. The Python service starts the torrent download using a torrent client/library.
5. The file is downloaded to the configured storage location.

---

## Requirements

- Python 3.11
- Telegram Bot Token
- Torrent client or torrent library (depending on implementation)

---

## Setup

### 1. Clone the repository

```
git clone https://github.com/RajPatil002/Mirror-Leech-Telegram-Bot.git
cd Mirror-Leech-Telegram-Bot
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Configure environment variables

Create a configuration file or environment variables containing:

```
API_KEY=<token> # Telegram bot token
DOWNLOAD_PATH=<path_to_download_location> # Default ./downloads
DOWNLOAD_PATH_LINK=<url_to_downloads_folder> # Optional
```

---

### 4. Run the bot

```
python main.py
```

The bot will start listening for Telegram commands.

---

## Example Commands

Start the bot

```
/start
```

Download using a magnet link

```
/tm magnet:?xt=urn:btih:...
```

---

## Use Cases

- Remote torrent management
- Downloading torrents on a home server
- Running downloads on a VPS while controlling through Telegram

---

## Notes

- Make sure the bot token is kept private.
- Ensure the server has enough storage for downloaded files.
- Use responsibly and comply with local laws and regulations regarding torrent downloads.
