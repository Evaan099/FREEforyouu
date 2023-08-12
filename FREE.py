import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from REAL import bot.main
    bot.main()
elif bit == '32bit':
    from REAL32 import bot.main
    bot.main()
