# IG PP Telegram Bot
A simple Telegram bot to get Instagram user profile photo.

## Usage

### Step 1.

Go to ["API development tools"](https://my.telegram.org/apps) and fill out the form then create an app and get `API_ID` and `API_HASH` code.

### Step 2.

Create a bot with [@BotFather](https://telegram.me/BotFather) and get `token`.

### Step 3.

Run a container:

```bash
docker run -d \
--name igpp_telegrambot \
-e API_ID=YOUR_API_ID \
-e API_HASH=YOUR_API_HASH \
-e BOT_TOKEN=YOUR_BOT_TOKEN \
scnplt/igpp_telegrambot:v0.0.1
```

### Step 5.

To check, send a message as `/start` to your bot. If you receive a reply, send an Instagram username (e.g. `@cpsertan`).
