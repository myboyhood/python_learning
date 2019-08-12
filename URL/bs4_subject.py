import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup
import json


def main():
    keyword = input("please input your keyword")
    keyword = urllib.parse.urlencode({"word": keyword})
    response = urllib.request.urlopen("http://baike.baidu.com/search/word?%s" % keyword)
    html = response.read()
    html_decode = html.decode('utf-8')
    print(html_decode)
    # target = json.loads(html_decode)
    # print(target)
    # print(html)
    soup = BeautifulSoup(html, "html.parser")

    for each in soup.find_all(href=re.compile("view")):
        content = ''.join([each.text])
        url2 = ''.join(["http://baike.baidu.com", each["href"]])
        response2 = urllib.request.urlopen(url2)
        html2 = response2.read()
        soup2 = BeautifulSoup(html2, "html.parser")
        if soup2.h2:
            content = ''.join([content, soup2.h2.text])
            content = ''.join(content, "->", url2)
            print(content)


if __name__ == "__main__":
    main()

