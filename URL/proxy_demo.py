#!usr/bin/env python
import urllib.request
import random
import urllib.error

url = 'http://www.fishc.com'
iplist = input("add proxy IP, seperate them with ;\nIP:").split(sep=";")
while True:
    ip = random.choice(iplist)
    proxy_support = urllib.request.ProxyHandler({'http': ip})
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent', 'Mozilla/5.0(X11; Ubuntu; Linux x86_64;rv:61.0)Gecko/20100101 Firefox/61.0')]
    # urllib.request.install_opener(opener)
    try:
        print("using IP: %s" % ip)
        response = opener.open(url)
        html = response.read()
        print(html)
    except urllib.error.URLError:
        print("visit error!")
    else:
        print("visit success!")
    if input("continue?(Y/N)") == "N":
        break
# 124.254.57.150:8118
# 211.138.121.38:80