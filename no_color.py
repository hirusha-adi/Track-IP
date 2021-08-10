import requests, os, platform, time

def clear():
    if platform.system().lower().startswith('win'):
        clear = "cls"
    else:
        clear = "clear"
    os.system(clear)

def BANNER():
    print(" ")
    print( f"   _______             _       _____       ")
    print( f"  |__   __|           | |     |_   _|      ")
    print( f"     | |_ __ __ _  ___| | __    | |  _ __  ")
    print( f"     | |  __/ _  |/ __| |/ /    | | |  _ \ ")
    print( f"     | | | | (_| | (__|   <    _| |_| |_) |")
    print( f"     |_|_|  \__,_|\___|_|\_\  |_____| .__/ ")
    print( f"                                    | |    ")
    print( f"                                    |_|    ")
    print( "")
    print( f"           Created By ZeaCeR#5641 ")
    print(" ")

def HOME():
    BANNER()
    print("  [1] My IP")
    print("  [2] Track IP")
    print("  [3] Exit")
    print(" ")
    mmo = input("    [+] Please Select An Option: ")
    if mmo == "1":
        TRACK_IP()
    elif mmo == "2":
        submmo = input("    [+] Please enter the IP Address: ")
        TRACK_IP(submmo)
    elif mmo == "3":
        exit()

def TRACK_IP(ip=""):
    clear()
    BANNER()
    print("   [+] Gathering Information. Please Wait!!")
    r = requests.get(f"https://ipapi.co/{ip}/json").json()
    print(f"""
    IP Address   :   {r["ip"]}
    City         :   {r["city"]}
    Region       :   {r["region"]}
    Country      :   {r["country_name"]}

    Latitude     :   {r["latitude"]}
    Longitude    :   {r["longitude"]}
    Time Zone    :   {r["timezone"]}
    UTC Offset   :   {r["utc_offset"]}
    Postal Code  :   {r["postal"]}

    ISP          :   {r["org"]}
    ASN          :   {r["asn"]}

    Country Code :   {r["country_code"]}
    Country TLD  :   {r["country_tld"]}
    Population   :   {r["country_population"]}
    Currency     :   {r["currency"]}
    Currency Name:   {r["currency_name"]}
    Country Area :   {r["country_area"]}
    Languages    :   {r["languages"]}
    Calling code :   {r["country_calling_code"]}

    GOOGLE MAPS  :   https://maps.google.com/?q={r["latitude"]},{r["longitude"]}

   [1] Return to Main Menu
   [2] Exit
    """)
    smo = input(">> ")
    if smo == "1":
        HOME()
    elif smo == "2":
        exit()
    else:
        print("[!!] PLEASE ENTER A VALID COMMAND!")
        time.sleep(1.5)
        HOME()
    
if __name__ == "__main__":
    HOME()