#sadrazam#9999
import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.MAGENTA + """ 

  | .gg/ngrok |  DİSCORD İD SORGULAMA PANELİ | .gg/ngrok |


""" + Fore.GREEN)
print(banner)
userid = input(" [sadrazam#9999] SORGULANCAK ID : ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n [sadrazam#9999] TOKENININ İLK PARTI : {encodedStr}')
os.system('pause >nul') 
