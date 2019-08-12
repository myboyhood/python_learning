#!usr/bin/env python
import urllib.request
import urllib.parse
import json

content = input("please input your content")
# delete "translate_o" to be "translate"
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionForm=http://www.youdao.com/"
head = {}
head['Referer'] = "http://fanyi.youdao.com"
head['User-Agent'] = 'Mozilla/5.0(X11; Ubuntu; Linux x86_64;rv:61.0)Gecko/20100101 Firefox/61.0'
data = {}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['xmlVersion'] = '1.6'
data['keyframe'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['typeResult'] = 'true'
data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url, data, head)
response = urllib.request.urlopen(req)
html = response.read()
html = html.decode("utf-8")
target = json.loads(html)
# print(html)
print("the result: %s" % (target['translateResult'][0][0]['tgt']))
