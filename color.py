import requests, os, platform, time

def clear():
    if platform.system().lower().startswith('win'):
        clear = "cls"
    else:
        clear = "clear"
    os.system(clear)

class b:
    G = '\033[92m' #GREEN
    Y = '\033[93m' #YELLOW
    R = '\033[91m' #RED
    W = '\033[0m' #RESET COLOR
    P = '\033[35m' # PURPLE

def BANNER():
    clear()
    print(" ")
    print( f"{b.W}{b.Y}   _______             _        {b.W}{b.G}_____       {b.G}{b.W}")
    print( f"{b.W}{b.Y}  |__   __|           | |      {b.W}{b.G}|_   _|      {b.G}{b.W}")
    print( f"{b.W}{b.Y}     | |_ __ __ _  ___| | __     {b.W}{b.G}| |  _ __  {b.G}{b.W}")
    print( f"{b.W}{b.Y}     | |  __/ _  |/ __| |/ /     {b.W}{b.G}| | |  _ \ {b.G}{b.W}")
    print( f"{b.W}{b.Y}     | | | | (_| | (__|   <     {b.W}{b.G}_| |_| |_) |{b.G}{b.W}")
    print( f"{b.W}{b.Y}     |_|_|  \__,_|\___|_|\_\   {b.W}{b.G}|_____| .__/ {b.G}{b.W}")
    print( f"{b.W}{b.G}                                     | |    {b.G}{b.W}")
    print( f"{b.W}{b.G}                                     |_|    {b.G}{b.W}")
    print( "")
    print( f"           {b.W}{b.Y}Created by {b.W}{b.R}ZeaCeR#5641{b.W} ")
    print(" ")

def HOME():
    BANNER()
    print(f"  {b.W}{b.R}[{b.W}1{b.R}]{b.W} {b.Y}My IP{b.W}")
    print(f"  {b.W}{b.R}[{b.W}2{b.R}]{b.W} {b.Y}Track IP{b.W}")
    print(f"  {b.W}{b.R}[{b.W}3{b.R}]{b.W} {b.Y}Exit{b.W}")
    print(" ")
    mmo = input(f"    {b.W}{b.R}[+] Please Select An Option: {b.W}")
    if mmo == "1":
        TRACK_IP()
    elif mmo == "2":
        submmo = input(f"    {b.W}{b.R}[+] Please enter the IP Address: {b.W}")
        TRACK_IP(submmo)
    elif mmo == "3":
        exit()

def TRACK_IP(ip=""):
    clear()
    BANNER()
    print(f"   {b.W}{b.P}[+] Gathering Information. Please Wait!!{b.W}")
    r = requests.get(f"https://ipapi.co/{ip}/json").json()
    print(f"""
    {b.Y}IP Address{b.W}   :   {b.G}{r["ip"]}{b.W}
    {b.Y}City{b.W}         :   {b.G}{r["city"]}{b.W}
    {b.Y}Region{b.W}       :   {b.G}{r["region"]}{b.W}
    {b.Y}Country{b.W}      :   {b.G}{r["country_name"]}{b.W}

    {b.Y}Latitude{b.W}     :   {b.G}{r["latitude"]}{b.W}
    {b.Y}Longitude{b.W}    :   {b.G}{r["longitude"]}{b.W}
    {b.Y}Time Zone{b.W}    :   {b.G}{r["timezone"]}{b.W}
    {b.Y}UTC Offset{b.W}   :   {b.G}{r["utc_offset"]}{b.W}
    {b.Y}Postal Code{b.W}  :   {b.G}{r["postal"]}{b.W}

    {b.Y}ISP{b.W}          :   {b.G}{r["org"]}{b.W}
    {b.Y}ASN{b.W}          :   {b.G}{r["asn"]}{b.W}

    {b.Y}Country Code{b.W} :   {b.G}{r["country_code"]}{b.W}
    {b.Y}Country TLD{b.W}  :   {b.G}{r["country_tld"]}{b.W}
    {b.Y}Population{b.W}   :   {b.G}{r["country_population"]}{b.W}
    {b.Y}Currency{b.W}     :   {b.G}{r["currency"]}{b.W}
    {b.Y}Currency Name{b.W}:   {b.G}{r["currency_name"]}{b.W}
    {b.Y}Country Area{b.W} :   {b.G}{r["country_area"]}{b.W}
    {b.Y}Languages{b.W}    :   {b.G}{r["languages"]}{b.W}
    {b.Y}Calling code{b.W} :   {b.G}{r["country_calling_code"]}{b.W}

    {b.Y}GOOGLE MAPS{b.W}  :   {b.P}https://maps.google.com/?q={r["latitude"]},{r["longitude"]}  {b.W}

   {b.W}{b.R}[{b.W}1{b.R}]{b.W} {b.Y}Return to Main Menu{b.W}
   {b.W}{b.R}[{b.W}2{b.R}]{b.W} {b.Y}Exit{b.W}
    """)
    smo = input(f"{b.W}{b.R}>> {b.W}")
    if smo == "1":
        HOME()
    elif smo == "2":
        exit()
    else:
        print(f"{b.W}{b.R}[!!] PLEASE ENTER A VALID COMMAND!{b.W}")
        time.sleep(1.5)
        HOME()
    
if __name__ == "__main__":
    HOME()