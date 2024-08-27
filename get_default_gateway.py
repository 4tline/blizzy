import subprocess
import re

def get_default_gateway():#fonction qui sert à recuperer la passerelle par default
    def_get=subprocess.run(['ipconfig'])
    print(def_get)
    return def_get

