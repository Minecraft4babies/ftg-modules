# @Minecraft4babies's module
# В принципе делался для себя. Код ниже берите, если нужен)
from .. import loader, utils
import logging
from telethon import events
from telethon import functions
import os
import ffmpeg
from .. import loader, utils


def register(cb):
    cb(mc4b_togifstickerMod())


@loader.tds
class Mc4bToGifStickerMod(loader.Module):
    """"<b>Модуль для преобразования видео в GIF-стикеры</b>"""
    strings = {"cfg_doc": "Настройка надписей состояния работы",
               "name": "Майнкрафтер. GIF-стикеров мейкер",
               "Downloading": "<b>Котики(🐈‍⬛ и 🐈) скачивают твою штучку...🐾</b>",
               "Converting": "<b>Котик 🐈 шаманит над твоей штучкой...🐾</b>",
               "Sending": "<b>Котик 🐈‍⬛ отправляет твою штучку...🐾</b>",
               "WrongFormatError": "<b>🐈: «Няф, это не нужный нам файлик»</b>",
               "UnexpectedError": "<b>🐈‍⬛: «Миу?!! Что-то не вышло...»</b>",
               "NoFileError": "<b>🐈: «Миу?!! Я не вижу никакого файла...»</b>"}

    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()

    def __init__(self):
        self.config = loader.ModuleConfig("CONFIG_STRING", "hello", lambda m: self.strings("cfg_doc", m))

    @loader.unrestricted
    async def gifstickercmd(self, message):
        """<code>.gifsticker</code> <реплай на видео>"""

        a = """ffmpeg -ss 00:00:00 -i inputfile.mp4 -to 00:00:03 -filter:v "scale=w=512:h=512:force_original_aspect_ratio=decrease,fps=30" -c:v libvpx-vp9 -crf 30 -b:v 900k -an GifSticker.WEBM"""
        try:
            await message.edit(self.strings("Downloading", message))
            reply = await message.get_reply_message()
            if reply:
                if reply.video:
                    await message.client.download_media(reply.media, "inputfile.mp4")
                    await message.edit(self.strings("Converting", message))
                    os.system(a)
                    await message.edit(self.strings("Sending", message))
                    await message.client.send_file(message.to_id, "GifSticker.WEBM", force_document=True, reply_to=reply)
                else:
                    return await message.edit(self.strings("WrongFormatError", message))
                await message.delete()
                os.remove('GifSticker.WEBM')
                os.remove('inputfile.mp4')
            else:
                return await message.edit(self.strings("NoFileError"))
        except:
            await message.edit(self.strings("UnexpectedError", message))
            os.remove('GifSticker.WEBM')
            os.remove('inputfile.mp4')
            return
