import os, platform
def find_default_getaway(logi):
    match logi:
        case 'Linux':
            return 1
        case 'Darwin':
            return 2
        case 'Windows':
            return 3
        case _:
            return 0
def __main__():
    logi=platform.system()
    plat=os.name
    default_gateaway=find_default_getaway(logi)
    switch=True
    while switch:
        pass
    
    return logi, plat, default_gateaway
__main__()
print(__main__())
