import requests
from .. import loader, utils


def register(cb):
    cb(WeatherMod())
    
class WeatherMod(loader.Module):
    """Погода з сайту wttr.in"""
    strings = {'name': 'Weather'}
    
    async def pwcmd(self, message):
        """"Дає погоду картинкою.\nВикористання: .pw <місто>/нічого."""
        args = utils.get_args_raw(message).replace(' ', '+')
        args = utils.get_args_raw(message).replace('1', 'Вишгород')
        await message.edit("Миколина погода працює...")
        city = requests.get(f"https://wttr.in/{args if args != None else ''}.png?lang=uk").content
        await message.client.send_file(message.to_id, city)
        await message.delete()


    async def awcmd(self, message):
        """Дає погоду ascii-артом.\nВикористання: .aw <місто>; нічого."""
        city = utils.get_args_raw(message)
        await message.edit("Миколина погода працює...")
        r = requests.get(f"https://wttr.in/{city if city != None else ''}?0?q?T&lang=uk")
        await message.edit(f"<code>Місце: {r.text}</code>")
