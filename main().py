import os, platform, netifaces

def get_default_gateway():
    # Recuperer les informations de la passerelle par defaut
    gateways = netifaces.gateways()
    # Extraire l'adresse IP de la passerelle par defaut pour IPv4
    default_gateway = gateways.get('default', {}).get(netifaces.AF_INET, [None])[0]
    print(f"La passerelle par defaut est : {default_gateway}")
    return default_gateway

def find_default_getaway(logi):
    match logi:
        case 'Linux':
            return 1
        case 'Darwin':
            return 2
        case 'Windows':
            return get_default_gateway()
        case _:
            return 0
def __main__():
    logi=platform.system()
    plat=os.name
    default_gateaway=find_default_getaway(logi)
    switch=True
    return logi, plat, default_gateaway
__main__()
print(__main__())
