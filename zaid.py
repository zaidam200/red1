import requests
from bs4 import BeautifulSoup
import random
import string
import json
import console
import time
from concurrent.futures import ThreadPoolExecutor
import warnings

# ------- SSL hata ayıklaması için
# Yani konsoldan gizlemek için 
def handle_warning(message, category, filename, lineno, file=None, line=None):
    if category == requests.packages.urllib3.exceptions.InsecureRequestWarning:
        pass

warnings.showwarning = handle_warning

with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

#(0.0, 0.6, 1.0)
print("""
________              ______              
___  __ \_____ __________  /__ 
__  / / /  __ `/_  ___/_  //_/ 
_  /_/ // /_/ /_  /   _  ,<   
/_____/ \__,_/ /_/    /_/|_|""")
print("")
#(1.0, 0.5, 0.0)
print("                        ENZA")
#(1.0, 0.0, 1.0)
print("    Gemiler battı diye")
#(0.6, 0.0, 0.8)
print("     Acırmı denizin canı..")
print("")
#()

#(0.6, 0.0, 0.8)
print("Created By TG: @dark_enza")
print("")
#()

#(0.0, 0.6, 1.0)
print("RedBull eSIM 100MB Generator")
print("")
#()


device_id = '-'.join(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)) for _ in range(5))  # Rastgele bir deviceId oluştur
kullan = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))

name = ''.join(random.choice(string.ascii_letters) for _ in range(6))  # Rastgele bir name oluştur (6 karakter)

url1 = "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1"
headers1 = {
    'Host': 'www.1secmail.com'
}
res1 = requests.get(url1, headers=headers1, verify=False)
sonuc1 = res1.json()
eposta = str(sonuc1).strip("['']")
#(0.0, 1.0, 0.0)
print("[@]Eposta belirlendi:",eposta)
login = eposta
isim, domain = login.split('@')

# hesap oluşturmak
url = "https://wndr.azurewebsites.net/api/v1/auth/registration/email"
headers = {
    "X-Device-Model": "iPhone13,2",
    "Connection": "keep-alive",
    "X-Device-ID": device_id,
    "X-Device-Type": "iOS",
    "X-Accept-Version": "1.1",
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "X-App-Version": "1.3.0",
    "Host": "wndr.azurewebsites.net",
    "Accept-Language": "en",
    "User-Agent": "RBM%20data/84 CFNetwork/1390 Darwin/22.0.0",
    "Accept": "*/*"
}


data = {
    "deviceId": device_id,
    "name":  name ,
    "email": eposta,
    "password": "zsezsert55"
}
response = requests.post(url, headers=headers, json=data)
try:
	sonuc = response.json() == {}
	#(0.0, 1.0, 0.0)
	print("[+]Eposta Eklendi 🟢")
except:
	#(1.0, 0.0, 0.0)
	print("[-]Başarısız Admine ulaş TG: @dark_enza")
	raise SystemExit()
	

time.sleep(5)
urlx = "https://www.1secmail.com/api/v1/?action=getMessages&login="+isim+"&domain="+domain
headersx = {
    'Host': 'www.1secmail.com'
}
resx = requests.get(urlx, headers=headersx, verify=False)
x = resx.json()[0]["id"]

url11 = "https://www.1secmail.com/api/v1/?action=readMessage&login=" + isim + "&domain=" + domain + "&id=" + str(x)
res11 = requests.get(url11, verify=False)
sonuc11 = res11.json()['body']
soup = BeautifulSoup(sonuc11, 'html.parser')
link = soup.find('a', class_='btn-link')
href_deger = link.get('href')
try:
	res11_1 = requests.get(href_deger, verify=False)
	sonuc11_1 = res11_1.status_code == 200
	#(0.0, 1.0, 0.0)
	print("[+]Eposta Doğrulandı")
except:
	#(1.0, 0.0, 0.0)
	print("[-]Eposta Doğrulanamadı")

url2 = "https://wndr.azurewebsites.net/api/v1/auth/login/email"
headers2 = {
    "X-Device-Model": "iPhone13,2",
    "Connection": "keep-alive",
    "X-Device-ID": device_id,
    "X-Device-Type": "iOS",
    "X-Accept-Version": "1.1",
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "X-App-Version": "1.3.0",
    "Host": "wndr.azurewebsites.net",
    "Accept-Language": "en",
    "User-Agent": "RBM%20data/84 CFNetwork/1390 Darwin/22.0.0",
    "Accept": "*/*"
}

data2 = {
    "email": eposta,
    "password": "zsezsert55"
}

response2 = requests.post(url2, headers=headers2, json=data2)
sonuc2 = response2.json()
try:
	sonuc2 = response2.json()["accessToken"]
	#(0.0, 1.0, 0.0)
	print("[+]Token Çekildi 🟢")
except:
	#(1.0, 0.0, 0.0)
	print("[-]Token Çekilemedi Tekrar Dene🔴")
	raise SystemExit()



url3 = "https://wndr.azurewebsites.net/api/v1/packages/subscriber"
headers3 = {
    "X-Device-Model": "iPhone13,2",
    "Connection": "keep-alive",
    "Authorization": "Bearer " + sonuc2,
    "X-Device-Type": "iOS",
    "X-Accept-Version": "1.1",
    "X-Device-ID": device_id,
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "X-App-Version": "1.3.0",
    "Host": "wndr.azurewebsites.net",
    "Accept-Language": "en",
    "User-Agent": "RBM%20data/84 CFNetwork/1390 Darwin/22.0.0",
    "Accept": "*/*"
}
response3 = requests.post(url3, headers=headers3)
sonuc3 = response3.json()["subscriber_reference"]


url4 = f"https://wndr.azurewebsites.net/api/v1/packages/subscriber/{sonuc3}"
headers4 = {
        "X-Device-Model": "iPhone13,2",
        "Connection": "keep-alive",
        "Authorization": "Bearer " + sonuc2,
        "X-Device-Type": "iOS",
        "X-Accept-Version": "1.1",
        "X-Device-ID": device_id,
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "X-App-Version": "1.3.0",
        "Host": "wndr.azurewebsites.net",
        "Accept-Language": "en",
        "User-Agent": "RBM%20data/84 CFNetwork/1390 Darwin/22.0.0",
        "Accept": "*/*"
    }

response4 = requests.get(url4, headers=headers4)
sonuc4 = response4.json()

if 'simcard' in sonuc4 and 'smdp_address' in sonuc4['simcard'] and 'matching_id' in sonuc4['simcard']:
	smdp_address = sonuc4['simcard']['smdp_address']
	matching_id = sonuc4['simcard']['matching_id']
	#(0.0, 1.0, 0.0)
	print("")
	print("SM+DP:")
	print(smdp_address)
	print("")
	print("Etkinleştirme kodu:")
	print(matching_id)
	#(1.0, 0.0, 1.0)
	print("")
	print("Dark Enza Bol kullanımlar diler..")