import io
import requests
import random
from .. import loader, utils


def register(cb):
    cb(trakhich_mc4b1Mod())


class trakhich_mc4b1Mod(loader.Module):
    """Кого трахнешь?)"""

    strings = {'name': 'Trakhich'}

    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []

    async def fuckcmd(self, message):
        """ .fuck"""

        await message.edit("Собираем информацию...")
        randint = (str(random.randint(1,899))).ljust(3, "0")
        reply = await message.get_reply_message()



        scplink = f"http://scpfoundation.net/scp-{randint}"
        url = "https://webshot.deam.io/{}/?width=1000&height=1080?type=png"
        file = requests.get(url.format(scplink))
        file = io.BytesIO(file.content)
        file.name = "scpfuck.png"
        file.seek(0)

        pokemonpng = requests.get(f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{randint}.png").content
        await message.delete()
        await message.client.send_file(message.chat_id, file=pokemonpng, caption="Трахнешь это...", reply_to=reply)
        await message.client.send_message(message.chat_id, message="или, может...")
        await message.client.send_file(message.chat_id, file, caption="это?)")