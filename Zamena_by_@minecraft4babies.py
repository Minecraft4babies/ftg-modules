#Модуль создан @minecraft4babies по приколу ради себя
import requests
from .. import loader, utils


def register(cb):
    cb(ZamenaMod())
    
class ZamenaMod(loader.Module):
    """Замена с сайта ccte.nau.edu.ua"""
    strings = {'name': 'Замены by @minecraft4babies'}
    
    async def zamenacmd(self, message):
        """"Кидает замены картинкой.\nИспользование: .zamena"""
        await message.edit("Узнаем замены...")
        zamenapng = requests.get(f"http://ccte.nau.edu.ua/images/Zameni.jpg").content
        await message.client.send_file(message.to_id, zamenapng)
        await message.delete()
