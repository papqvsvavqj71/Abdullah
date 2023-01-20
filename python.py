import time
import requests
import webbrowser
import sys as n
import random
import webbrowser
import threading
print("""\033[1;33m
 _____  __  __
|  ___| \ \/ /
| |_     \  / 
|  _|    /  \ 
|_|     /_/\_\ """)
#=======
rhaby2 = int(5)#عدد الحرف ليوزر اذا تريد سوي خماسي خلي رقم 5
#========
ask = input("""
=========================
        𝑼𝑺𝑬𝑹𝑵𝑨𝑴𝑬     .
[1] FIVE 
[2] SIX
[3] SEVEN
[4] EIGHT
[5] THREE (T_X_6)

      𝑩𝑶𝑻 𝑼𝑺𝑬𝑹𝑵𝑨𝑴𝑬     .
    
[6] THREE BOT
[7] TWO BOT
=========================
[+] CHOICE ONE OPTION » """)
rhaby = int(1)
ruksI='IdMN1w9spls'
rg = 'D'
ruks_ = '\033[1;36m'
ruks__ = '\033[1;36m'
jruks = '\033[1;37m'
_ruks  = '\033[1;31m'
BGreen='\033[1;32m'
BRed ='\033[1;31m'

N =0
R =('━'*60)
print('')
rukS = input('[+] TOKEN BOT : ')
print('')
Ruks = input('[+] ID TELE : ')
print(R)
def ruks():
	global N
	global rukS
	global Ruks
if ask == "3":
	tuks1 = 'poiuytrewqasdfghjklmnbvcxz1234567890'
	t ='poiuytrewqasdfghjklmnbvcxz1234567890'
	ruKs = requests.session()
	try:	
		while True:
		    N +=1
		    rhaby1 = str("".join(random.choice(t)for i in range(1)))
		    email =  str("".join(random.choice(tuks1)for i in range(2)))
		    for password in range(rhaby):
		        password = ''
		        for item in range(rhaby2):
		             rhaby3 = ''
		        for item in range(rhaby2):
		            rhaby3 += random.choice(rhaby1)	        
		        user = (rhaby3+email)
		        url = f"https://t.me/{user}"
		        req = ruKs.get(url)
		        if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:	
		        	print(jruks+'['+BGreen+f'{N}'+jruks+'] ✅'+BGreen+f' [{user}]') 
		        	GUG_Y= f'https://api.telegram.org/bot{rukS}/sendMessage?chat_id={Ruks}&text=𝑯𝑰 𝑵𝑬𝑾 𝑼𝑺𝑬𝑹 𝑩𝒀 𝑭𝑿 \n= = = = = = = = = = = = = = =\n𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝚄𝚂𝙴𝚁 : @{user}\n= = = = = = = = = = = = = = =\nBy : @FX205 | @T_X_6'
		        	req = ruKs.post(GUG_Y)
		        	
		        else:
		        	print(jruks+'['+BRed+f'{N}'+jruks+'] ❌'+BRed+f'-[{user}]')
	except:
		print(' 𝐓𝐞𝐥𝐞 :@T_X_6 ☆ ')       	
thread = []
for i in range(100):
	thread1 =threading.Thread(target=ruks)
	thread1.start()
	thread.append(thread1)
for thread2 in thread:
	thread2.join
#-------------------------------
if ask == "2":
	tuks1 = 'poiuytrewqasdfghjklmnbvcxz1234567890'
	t ='poiuytrewqasdfghjklmnbvcxz1234567890'
	ruKs = requests.session()
	try:	
		while True:
		    N +=1
		    rhaby1 = str("".join(random.choice(t)for i in range(2)))
		    email =  str("".join(random.choice(tuks1)for i in range(1)))
		    for password in range(rhaby):
		        password = ''
		        for item in range(rhaby2):
		             rhaby3 = ''
		        for item in range(rhaby2):
		            rhaby3 += random.choice(rhaby1)	        
		        user = (rhaby3+email)
		        url = f"https://t.me/{user}"
		        req = ruKs.get(url)
		        if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:	
		        	print(jruks+'['+BGreen+f'{N}'+jruks+'] ✅'+BGreen+f' [{user}]') 
		        	GUG_Y= f'https://api.telegram.org/bot{rukS}/sendMessage?chat_id={Ruks}&text=𝑯𝑰 𝑵𝑬𝑾 𝑼𝑺𝑬𝑹 𝑩𝒀 𝑭𝑿 \n= = = = = = = = = = = = = = =\n𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝚄𝚂𝙴𝚁 : @{user}\n= = = = = = = = = = = = = = =\nBy : @FX205 | @T_X_6'
		        	req = ruKs.post(GUG_Y)
		        	
		        else:
		        	print(jruks+'['+BRed+f'{N}'+jruks+'] ❌'+BRed+f'-[{user}]')
	except:
		print(' 𝐓𝐞𝐥𝐞 :@T_X_6 ☆ ')       	
thread = []
for i in range(100):
	thread1 =threading.Thread(target=ruks)
	thread1.start()
	thread.append(thread1)
for thread2 in thread:
	thread2.join	
if ask == "1":
	tuks1 = 'poiuytrewqasdfghjklmnbvcxz1234567890'
	t ='poiuytrewqasdfghjklmnbvcxz1234567890'
	ruKs = requests.session()
	try:	
		while True:
		    N +=1
		    rhaby1 = str("".join(random.choice(t)for i in range(3)))
		    email =  str("".join(random.choice(tuks1)for i in range(0)))
		    for password in range(rhaby):
		        password = ''
		        for item in range(rhaby2):
		             rhaby3 = ''
		        for item in range(rhaby2):
		            rhaby3 += random.choice(rhaby1)	        
		        user = (rhaby3+email)
		        url = f"https://t.me/{user}"
		        req = ruKs.get(url)
		        if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:	
		        	print(jruks+'['+BGreen+f'{N}'+jruks+'] ✅'+BGreen+f' [{user}]') 
		        	GUG_Y= f'https://api.telegram.org/bot{rukS}/sendMessage?chat_id={Ruks}&text=𝑯𝑰 𝑵𝑬𝑾 𝑼𝑺𝑬𝑹 𝑩𝒀 𝑭𝑿 \n= = = = = = = = = = = = = = =\n𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝚄𝚂𝙴𝚁 : @{user}\n= = = = = = = = = = = = = = =\nBy : @FX205 | @T_X_6'
		        	req = ruKs.post(GUG_Y)
		        	
		        else:
		        	print(jruks+'['+BRed+f'{N}'+jruks+'] ❌'+BRed+f'-[{user}]')
	except:
		print(' 𝐓𝐞𝐥𝐞 :@T_X_6 ☆ ')       	
thread = []
for i in range(100):
	thread1 =threading.Thread(target=ruks)
	thread1.start()
	thread.append(thread1)
for thread2 in thread:
	thread2.join
if ask == "4":
	tuks1 = 'poiuytrewqasdfghjklmnbvcxz1234567890'
	t ='poiuytrewqasdfghjklmnbvcxz1234567890'
	ruKs = requests.session()
	try:	
		while True:
		    N +=1
		    rhaby1 = str("".join(random.choice(t)for i in range(1)))
		    email =  str("".join(random.choice(tuks1)for i in range(3)))
		    for password in range(rhaby):
		        password = ''
		        for item in range(rhaby2):
		             rhaby3 = ''
		        for item in range(rhaby2):
		            rhaby3 += random.choice(rhaby1)	        
		        user = (rhaby3+email)
		        url = f"https://t.me/{user}"
		        req = ruKs.get(url)
		        if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:	
		        	print(jruks+'['+BGreen+f'{N}'+jruks+'] ✅'+BGreen+f' [{user}]') 
		        	GUG_Y= f'https://api.telegram.org/bot{rukS}/sendMessage?chat_id={Ruks}&text=𝑯𝑰 𝑵𝑬𝑾 𝑼𝑺𝑬𝑹 𝑩𝒀 𝑭𝑿 \n= = = = = = = = = = = = = = =\n𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝚄𝚂𝙴𝚁 : @{user}\n= = = = = = = = = = = = = = =\nBy : @FX205 | @T_X_6'
		        	req = ruKs.post(GUG_Y)
		        	
		        else:
		        	print(jruks+'['+BRed+f'{N}'+jruks+'] ❌'+BRed+f'-[{user}]')
	except:
		print(' 𝐓𝐞𝐥𝐞 :@T_X_6 ☆ ')       	
thread = []
for i in range(100):
	thread1 =threading.Thread(target=ruks)
	thread1.start()
	thread.append(thread1)
for thread2 in thread:
	thread2.join
	
	
	

if ask == "6":
	tuks1 = 'poiuytrewqasdfghjklmnbvcxz1234567890'
	t ='poiuytrewqasdfghjklmnbvcxz1234567890'
	ruKs = requests.session()
	try:	
		while True:
		    N +=1
		    rhaby1 = str("".join(random.choice(t)for i in range(3)))
		    email =  str("".join(random.choice(tuks1)for i in range(3)))
		    for password in range(rhaby):
		        password = ''
		        for item in range(rhaby2):
		             rhaby3 = ''
		        for item in range(rhaby2):
		            rhaby3 += random.choice(rhaby1)	        
		        user = (rhaby1+'bot')
		        url = f"https://t.me/{user}"
		        req = ruKs.get(url)
		        if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:	
		        	print(jruks+'['+BGreen+f'{N}'+jruks+'] ✅'+BGreen+f' [{user}]') 
		        	GUG_Y= f'https://api.telegram.org/bot{rukS}/sendMessage?chat_id={Ruks}&text=𝑯𝑰 𝑵𝑬𝑾 𝑼𝑺𝑬𝑹 𝑩𝒀 𝑭𝑿 \n= = = = = = = = = = = = = = =\n𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝚄𝚂𝙴𝚁 : @{user}\n= = = = = = = = = = = = = = =\nBy : @FX205 | @T_X_6'
		        	req = ruKs.post(GUG_Y)
		        	
		        else:
		        	print(jruks+'['+BRed+f'{N}'+jruks+'] ❌'+BRed+f'-[{user}]')
	except:
		print(' 𝐓𝐞𝐥𝐞 :@T_X_6 ☆ ')       	
thread = []
for i in range(100):
	thread1 =threading.Thread(target=ruks)
	thread1.start()
	thread.append(thread1)
for thread2 in thread:
	thread2.join
	
	
if ask == "7":
	tuks1 = 'poiuytrewqasdfghjklmnbvcxz1234567890'
	t ='poiuytrewqasdfghjklmnbvcxz1234567890'
	ruKs = requests.session()
	try:	
		while True:
		    N +=1
		    rhaby1 = str("".join(random.choice(t)for i in range(2)))
		    email =  str("".join(random.choice(tuks1)for i in range(3)))
		    for password in range(rhaby):
		        password = ''
		        for item in range(rhaby2):
		             rhaby3 = ''
		        for item in range(rhaby2):
		            rhaby3 += random.choice(rhaby1)	        
		        user = (rhaby1+'bot')
		        url = f"https://t.me/{user}"
		        req = ruKs.get(url)
		        if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:	
		        	print(jruks+'['+BGreen+f'{N}'+jruks+'] ✅'+BGreen+f' [{user}]') 
		        	GUG_Y= f'https://api.telegram.org/bot{rukS}/sendMessage?chat_id={Ruks}&text=𝑯𝑰 𝑵𝑬𝑾 𝑼𝑺𝑬𝑹 𝑩𝒀 𝑭𝑿 \n= = = = = = = = = = = = = = =\n𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝚄𝚂𝙴𝚁 : @{user}\n= = = = = = = = = = = = = = =\nBy : @FX205 | @T_X_6'
		        	req = ruKs.post(GUG_Y)
		        	
		        else:
		        	print(jruks+'['+BRed+f'{N}'+jruks+'] ❌'+BRed+f'-[{user}]')
	except:
		print(' 𝐓𝐞𝐥𝐞 :@T_X_6 ☆ ')       	
thread = []
for i in range(100):
	thread1 =threading.Thread(target=ruks)
	thread1.start()
	thread.append(thread1)
for thread2 in thread:
	thread2.join
	
	
	
if ask == "5":
	h ='poiuytrewqasdfghjklmnbvcxz1234567890'
	tuks1 = 'poiuytrewqasdfghjklmnbvcxz1234567890'
	t ='poiuytrewqasdfghjklmnbvcxz1234567890'
	ruKs = requests.session()
	try:	
		while True:
		    N +=1
		    rhaby1 = str("".join(random.choice(t)for i in range(1)))
		    email =  str("".join(random.choice(tuks1)for i in range(1)))
		    for password in range(rhaby):
		        password = ''
		        for item in range(rhaby2):
		             rhaby3 = ''
		        for item in range(rhaby2):
		            rhaby3 += random.choice(rhaby1)	        
		    rhaby9 = str("".join(random.choice(h)for i in range(1)))
		    user = (rhaby9+'_'+rhaby1+'_'+email)
		    url = f"https://t.me/{user}"
		    req = ruKs.get(url)
		    if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:	
		        	print(jruks+'['+BGreen+f'{N}'+jruks+'] ✅'+BGreen+f' [{user}]') 
		        	GUG_Y= f'https://api.telegram.org/bot{rukS}/sendMessage?chat_id={Ruks}&text=𝑯𝑰 𝑵𝑬𝑾 𝑼𝑺𝑬𝑹 𝑩𝒀 𝑭𝑿 \n= = = = = = = = = = = = = = =\n𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝚄𝚂𝙴𝚁 : @{user}\n= = = = = = = = = = = = = = =\nBy : @FX205 | @T_X_6'
		        	req = ruKs.post(GUG_Y)
		        	
		    else:
		        	print(jruks+'['+BRed+f'{N}'+jruks+'] ❌'+BRed+f'-[{user}]')
	except:
		print(' 𝐓𝐞𝐥𝐞 :@T_X_6 ☆ ')       	
thread = []
for i in range(100):
	thread1 =threading.Thread(target=ruks)
	thread1.start()
	thread.append(thread1)
for thread2 in thread:
	thread2.join
