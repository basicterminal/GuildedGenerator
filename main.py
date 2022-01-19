import random
import requests
import time, os


with open("GuildedGenerator/Proxies.txt", "r") as generator:
     Proxies = []
     Proxies += [proxy.strip() for proxy in generator.readlines()]     

class GuildedGenerator:
            _Headers = {
                'authority'           : 'www.guilded.gg',
                'method'              : 'POST',
                'path'                : '/api/users?type=email',
                'scheme'              : 'https',
                'accept'              : 'application/json, text/javascript, */*; q=0.01',
                'accept-encoding'     : 'gzip, deflate, br',
                'accept-language'     : 'en-US,en;q=0.9',
                'content-type'        : 'application/json',
                'origin'              : 'https://www.guilded.gg',
                'sec-ch-ua'           : 'Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96',
                'sec-ch-ua-mobile'    : '?0',
                'sec-ch-ua-platform'  : 'Windows',
                'sec-fetch-dest'      : 'empty',
                'sec-fetch-mode'      : 'cors',
                'sec-fetch-site'      : 'same-origin',
                'user-agent'          : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
                'x-requested-with'    : 'XMLHttpRequest',
                'guilded-client-id'   : 'f1a162c9-8992-468c-afdd-de50fd3fd428',
                'guilded-stag'        : '90156f8d1cc4886a65e92aded2861869',
                'guilded-device-id'   : '537b5c96c662685a3c6a9cf97b15fafe68ca4eb5141254ac908d08f4460218cc',
            }
            _Path = "GuildedGenerator/Sessions.txt"

#-------------#
User = input(" [@] Username > ")
Pass = input(" [@] Password > ")
Amount = input(" [@] Amount   > ")
print("#--------------------------#\n")

for account in range(int(Amount)):
    Email = "{}@avalanche.lol".format(random.randint(100000, 999999))
    Payload = {
              'extraInfo' : {'platform' : 'desktop'},
              'email'     : Email,
              'fullName'  : User,
              'name'      : User,
              'password'  : Pass
    }

    Proxy_Payload = {
         "http": 'http://%s' % random.choice(Proxies)
    }

    r = requests.post(
        "https://www.guilded.gg/api/users?type=email", 
        headers = GuildedGenerator._Headers, json = Payload,
        proxies = Proxy_Payload
    )

    if r.status_code in [200, 201, 203, 204]:
       Login_Payload = {'getMe' : True, 'email' : Email, 'password' : Pass}
       user = requests.post(
              "https://www.guilded.gg/api/login",
              json = Login_Payload,
              proxies = Proxy_Payload
       )

       with open(GuildedGenerator._Path, "a+") as Guilded:
            try:
               Guilded.write("\n{}".format(user.cookies['hmac_signed_session']))
               print(" [!] Fetched Cookie :: {}".format(user.cookies['hmac_signed_session']))
            except:
               print(" [$] Could not fetch cookie")

