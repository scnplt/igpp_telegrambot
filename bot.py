import os
import asyncio
import requests

from telethon import TelegramClient, events

API_ID = os.environ.get('API_ID', None)
API_HASH = os.environ.get('API_HASH', None)
BOT_TOKEN = os.environ.get('BOT_TOKEN', None)

HEADERS = { 'User-Agent': 'Instagram 219.0.0.12.117 Android' }
BASE_URL = 'https://www.instagram.com/api/v1/users/web_profile_info'
SESSIONS_PATH = 'sessions/session_master'
TEMP_PHOTO_PATH = 'temp.jpg'

WELCOME_MESSAGE = "Hi! Send me an Instagram username (e.g. @cpsertan) and I will send you the account's profile picture."
USERNAME_REGEX = '^@\S{3,}'
WAIT_TIME_SEC = 10

client = TelegramClient(SESSIONS_PATH, API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply(WELCOME_MESSAGE)

@client.on(events.NewMessage(pattern=USERNAME_REGEX))
async def get_profile_picture(event):
    process_message = await event.reply(f'Please wait {WAIT_TIME_SEC} seconds...')
    username = event.raw_text.split('@')[1]

    await asyncio.sleep(WAIT_TIME_SEC)
    req = requests.get(f"{BASE_URL}/?username={username}", headers=HEADERS)

    if req.status_code != 200:
        return await event.reply(f"This user doesn't exist.")

    try:
        photo_url = req.json()['data']['user']['profile_pic_url_hd']
        photo = requests.get(photo_url).content
        with open(TEMP_PHOTO_PATH, 'wb') as f:
            f.write(photo)
        await event.reply(file=TEMP_PHOTO_PATH)
    except Exception as e:
        await event.reply(f"I received an error, please try again later. ({e})")
    finally:
        await process_message.delete()
        os.remove(TEMP_PHOTO_PATH)

if __name__ == '__main__':
    client.run_until_disconnected()
