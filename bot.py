import os
import time
import requests

from constants import *
from telethon import TelegramClient, events

API_ID = os.environ.get('API_ID', None)
API_HASH = os.environ.get('API_HASH', None)
BOT_TOKEN = os.environ.get('BOT_TOKEN', None)

client = TelegramClient(SESSIONS_PATH, API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    sender = await event.get_sender()
    await client.send_message(sender.id, WELCOME_MESSAGE)

@client.on(events.NewMessage(pattern=USERNAME_REGEX))
async def get_profile_picture(event):
    sender = await event.get_sender()
    await client.send_message(sender.id, f"Please wait {WAIT_TIME} seconds...")
    time.sleep(WAIT_TIME)

    username = event.raw_text.split('@')[1]
    req = requests.get(f"{BASE_URL}/?username={username}", headers=HEADERS)

    if req.status_code != 200:
        return await client.send_message(sender.id, f"Error: {req.status_code}")

    try:
        picture_url = req.json()['data']['user']['profile_pic_url_hd']
        photo = requests.get(picture_url).content
        with open(TEMP_PHOTO_PATH, 'wb') as f:
            f.write(photo)
        await client.send_file(sender.id, TEMP_PHOTO_PATH)
    except:
        await client.send_message(sender.id, 'I received an error, please try again later.')

if __name__ == '__main__':
    client.run_until_disconnected()
