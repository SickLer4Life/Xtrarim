import eel
from random import randint
import pymem
import re


eel.init("web")


@eel.expose
def main():
    print("injected")
    pm = pymem.Pymem('csgo.exe')
    client = pymem.process.module_from_name(pm.process_handle,
                                            'client.dll')

    clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
    address = client.lpBaseOfDll + re.search(rb'\x33\xC0\x83\xFA.\xB9\x20',
                                             clientModule).start() + 4

    pm.write_uchar(address, 2 if pm.read_uchar(address) == 1 else 1)
    pm.close_process()

eel.start("index.html", size=(950, 700), position=(0,0))
