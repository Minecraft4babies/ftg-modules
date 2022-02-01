# @Minecraft4babies's module
# It doesn't work fine with all except tiktok urls
import logging
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
import asyncio
from .. import loader, utils

def register(cb):
    cb(mc4b_ttdlMod())

@loader.tds
class mc4b_ttdlMod(loader.Module):
    """"<b>Скачиваю видео из TikTok, YouTube(нет), Pinterest(возможно), Instagram(нет) через @allsaverbot</b>"""
    strings = {"cfg_doc": "Настройка надписей состояния работы",
               "name": "Майнкрафтер. ТикТок загрузчик",
               "NoArgs": "<b>🐈‍⬛: «Миу? Что ты хочешь сделать? Я жду ссылку..»</b>",
               "Working": "<b>Котики(🐈‍⬛ и 🐈) сохраняют твою штучку...🐾</b>",
               "BlockedBotError": "🐈: «Няф, разблокируй, пожалуйста, @allsaverbot!»",
               "TimeoutError": "Кися не смогла тебе помочь, извини. Бот молчит...🐾"}

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
    async def мурcmd(self, message):
        """<code>.мур</code> <b><ссылка/реплай></b>"""

        try:
            text = utils.get_args_raw(message)
            reply = await message.get_reply_message()
            chat = "@allsaverbot"
            if not text and not reply:
                await message.edit(self.strings("NoArgs", message))
                return
            if text:
                await message.edit(self.strings("Working", message))
                async with message.client.conversation(chat) as conv:
                    try:
                        response = conv.wait_event(events.NewMessage(incoming=True, from_users=804576054))
                        await message.client.send_message(chat, text)
                        response = await response
                    except YouBlockedUserError:
                        await message.reply(self.strings("BlockedBotError", message))
                        return
                    await message.delete()
                    await message.client.send_file(message.chat_id, response.media)
            else:
                await message.edit(self.strings("Working", message))
                async with message.client.conversation(chat) as conv:
                    try:
                        response = conv.wait_event(events.NewMessage(incoming=True, from_users=804576054))
                        await message.client.send_message(chat, reply)
                        response = await response
                    except YouBlockedUserError:
                        await message.reply(self.strings("BlockedBotError", message))
                        return
                    await message.delete()
                    await message.client.send_file(message.chat_id, response.media, reply_to=reply)
        except TimeoutError:
            return await message.edit(self.strings("TimeoutError", message))
