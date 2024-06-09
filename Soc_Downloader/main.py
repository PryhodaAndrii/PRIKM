import telethon
from telethon import TelegramClient, events
from FastTelethon import upload_file

from datetime import datetime

import os

import down_yt
import down_Instaloader
import commands
import get_audio

import logging


from os import environ

FORMAT = '%(asctime)-15s %(name)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logging.basicConfig(level=logging.ERROR, format=FORMAT)
logger = logging.getLogger()



api_id = environ.get("API_ID","define me") 

api_hash = environ.get("API_HASH","define me")

bot_token = environ.get("MAIN_BOT_TOKEN","define me")

logger.info(bot_token)

SAVE_FOLDER = os.path.join(os.path.dirname(__file__), f"_videos/")

logger.info('Bot has been started')
print(bot_token)

try:
    down_Instaloader.inst_login()
    logger.info("Succsess to login instagram")
except:
    logger.error("Failed to login instagram..")


client = TelegramClient('theker', api_id, api_hash).start(bot_token=bot_token)


async def send_and_delete(path2file='', sender_id=None, vid_note=True):
    print(f"Path to file:  {path2file}")
    mes  = await client.send_file(sender_id, file=path2file, video_note=vid_note)
    os.remove(path2file)


from telethon.tl.custom import Button
@client.on(events.NewMessage(pattern='/start'))
async def start_command(event):
    sender_id = event.sender_id
    await client.send_message(event.sender_id, 'сам')


@client.on(events.NewMessage)
async def start_command(event):
    sender_id = event.sender_id
    message = event.raw_text
    print(message)
    if "https://www.instagram.com/reel" in message:
        link = message
        if message.lower().startswith("a "):
            link = message.replace("a ", "")


        file = down_Instaloader.download_reel(link)
        if file == "Wrong url or private instagram pofile":
            await client.send_message(event.sender_id, file)
        
        else:
            file = f"{file}.mp4"
            if message.lower().startswith(commands.COMMAND_AUDIO):
                file = get_audio.teleg_get_audio(file)
            await send_and_delete(path2file=file, sender_id=event.sender_id)


    elif "https://www.youtube.com" in message:
        link = message
        if message.lower().startswith("a "):
            link = message.replace("a ", "")
            
        logger.error(f"mamamam++++ === {link}")
        file = down_yt.ytdl(link)
        if file == "Wrong url or private instagram pofile":
            await client.send_message(event.sender_id, file)
        
        else:
            file = f"{file}"
            if message.lower().startswith(commands.COMMAND_AUDIO):
                file = get_audio.teleg_get_audio(file)
            await send_and_delete(path2file=file, sender_id=event.sender_id)

    else:
        await client.send_message(event.sender_id, ')))')



client.start()
client.run_until_disconnected()


