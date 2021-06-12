from Rfid import Reader
import random
from datetime import datetime
from Utiltes import Utiltes


class Kayit():
    
    def __init__(self, ts, name, card_id, level):
        self.ts = ts
        self.name = name
        self.card_id = card_id
        self.level = level

list_name = ["Ayhan", "Enes", "Busra", "Ayca"]
list_level = ["Admin", "Supervisor", "Regular"]

kayit_one = Kayit("", "", "", "")

name_rd = (random.choice(list_name))
level_rd = (random.choice(list_level))
ts_rd = (datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'))
   
kayit_one.name = name_rd
kayit_one.level = level_rd
kayit_one.ts = ts_rd
card_id = Reader.Reader_card()
kayit_one.card_id = card_id

Utiltes.Json_converter(kayit_one)




