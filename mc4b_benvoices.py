#    ____  __  __ _                            __ _   _  _   _           _     _           
#   / __ \|  \/  (_)_ __   ___  ___ _ __ __ _ / _| |_| || | | |__   __ _| |__ (_) ___  ___ 
#  / / _` | |\/| | | '_ \ / _ \/ __| '__/ _` | |_| __| || |_| '_ \ / _` | '_ \| |/ _ \/ __|
# | | (_| | |  | | | | | |  __/ (__| | | (_| |  _| |_|__   _| |_) | (_| | |_) | |  __/\__ \
#  \ \__,_|_|  |_|_|_| |_|\___|\___|_|  \__,_|_|  \__|  |_| |_.__/ \__,_|_.__/|_|\___||___/
#   \____/                                                                                 

import random
from .. import loader, utils


def register(cb):
    cb(ben_voices_mc4b1Mod())


class ben_voices_mc4b1Mod(loader.Module):
    """Be-en!"""

    strings = {'name'           : '''BenVoices''',
               'wrong_input'    : '<b>Такого Бен не говорил...</b>',
               'question'       : '🤔<b>Бен, {}?</b>🤔',
               'reply_answer'   : '<b>Бен говорит:</b>'}

    def __init__(self):
        self.name = self.strings['name']

    @loader.unrestricted
    async def bencmd(self, message):
        """Фразы Бена. Пиши с аргументом <burp/eugh/hehehe/hmhhmhm/hmhm/hoho/hohoho/nananana/ring/answer/drop/yes/no>"""

        reply = await message.get_reply_message()

        option = utils.get_args_raw(message)
        await message.delete()
        try:
            voice = await get_voice(message, option)
            await message.client.send_file(message.chat_id, voice, reply_to=reply)
        except:
            await message.client.send_message(message.chat_id, message=self.strings['wrong_input'])


    @loader.unrestricted
    async def askbencmd(self, message):
        """Задай вопрос Бену. Он точно поможет). Также можно просто реплайем и без вопроса
        
        
        👨‍💻Made by: @Minecraft4babies_GFTG_Modules"""
        reply = await message.get_reply_message()
        question = self.strings['question'].format(utils.get_args_raw(message))
        voice = (random.choice(await message.client.get_messages('@mc4b_files_for_modules', limit=None,
                                                                 search='''Ben's voices: askben'''))).media

        if utils.get_args_raw(message)=='' and reply:
            await message.delete()
            await message.client.send_file(message.chat_id, voice, reply_to=reply, caption=self.strings['reply_answer'])
        elif utils.get_args_raw(message) != '':
            if message.out:
                await message.delete()
                question = await message.client.send_message(message.chat_id, message=question, reply_to=reply)
            else:
                question = await message.client.send_message(message.chat_id, message=question, reply_to=message)
            await message.client.send_file(message.chat_id, voice, reply_to=question)






async def get_voice(message, option):
    voice = (random.choice(await message.client.get_messages('@mc4b_files_for_modules',
                                                             search=f'''Ben's voices: {option}'''))).media
    return voice
