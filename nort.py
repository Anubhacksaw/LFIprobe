import requests
import time
import lastc
def check(url,payload,tmp,tmp1,s=0):
    iterations = 0
    while iterations < 20:
        iterations += 1
        print("\033[32m[INFO]Trying " + payload + "\033[0m")
        full_url=url+payload
        time.sleep(s)
        response = requests.get(full_url)
        if iterations >=2:
            payload = tmp+payload
        else:
            payload = tmp1+payload
        if response.status_code == 200:
            if lastc.fi(full_url):
                print("\033[1;31m[Success]Path found:{}\033[0m".format(full_url))
                return True
                break
    if response.status_code != 200:
        return False        
def check_ad(di,url,payload,tmp,s=0):
    iterations = 0
    while iterations < 20:
        iterations += 1
        print("\033[32m[INFO]Trying " +di+ payload + "\033[0m")
        full_url=url+di+payload
        time.sleep(s)
        response = requests.get(full_url)
        if iterations >=2:
            di=di+tmp
        if response.status_code == 200:
            if lastc.fi(full_url):
                print("\033[1;31m[Success]Path found:{}\033[0m".format(full_url))
                return True
                break
    if response.status_code != 200:
        return False        