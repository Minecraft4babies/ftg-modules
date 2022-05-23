"""
    ____  __  __ _                            __ _   _  _   _           _     _
   / __ \|  \/  (_)_ __   ___  ___ _ __ __ _ / _| |_| || | | |__   __ _| |__ (_) ___  ___
  / / _` | |\/| | | '_ \ / _ \/ __| '__/ _` | |_| __| || |_| '_ \ / _` | '_ \| |/ _ \/ __|
 | | (_| | |  | | | | | |  __/ (__| | | (_| |  _| |_|__   _| |_) | (_| | |_) | |  __/\__ \
  \ \__,_|_|  |_|_|_| |_|\___|\___|_|  \__,_|_|  \__|  |_| |_.__/ \__,_|_.__/|_|\___||___/
   \____/
"""
import io
import requests
import random
from .. import loader, utils


def register(cb):
    cb(pokemonorscp_mc4b1Mod())


class pokemonorscp_mc4b1Mod(loader.Module):
    """Who will you fuck?) Module sends two pics: random pokemon and SCP-object with same number."""

    strings = {'name': 'PokemonOrSCP'}

    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []

    async def pokemonorscpcmd(self, message):
        """Get random pokemon and SCP-object.


        👨‍💻Made by: @Minecraft4babies_GFTG_Modules"""

        await message.edit("<b>Collecting data...</b>")
        randint = (str(random.randint(1,898))).ljust(3, "0")
        reply = await message.get_reply_message()



        scplink = f"https://the-scp.foundation/object/scp-{randint}"
        url = "https://webshot.deam.io/{}/?width=1000&height=1080?type=png"
        file = requests.get(url.format(scplink))
        file = io.BytesIO(file.content)
        file.name = f"scp{randint}fuck.png"
        file.seek(0)

        pokemonpng = requests.get(f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{randint}.png").content
        await message.delete()
        pokemon_msg = await message.client.send_file(message.chat_id, file=pokemonpng, caption=f"Will you fuck pokemon №{randint}...", reply_to=reply)
        or_message = await message.client.send_message(message.chat_id, message="or...", reply_to=pokemon_msg)
        await message.client.send_file(message.chat_id, file, caption="Maybe, SCP-object with this number?)", reply_to=or_message)