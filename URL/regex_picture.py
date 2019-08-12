import urllib.request
import re
import os


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0(X11; Ubuntu; Linux x86_64;rv:61.0)Gecko/20100101 Firefox/61.0')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    return html


def get_img(html):
    p = r'img:"([^"]*\.jpg)"'
    imglist = re.findall(p, html)
    # print(html)
    try:
        os.mkdir("newpics")
    except FileExistsError:
        pass  # if the file exist ,then recover it
    os.chdir("newpics")
    for each in imglist:
        # print(imglist)
        each = "https://www.whu.edu.cn/" + each
        print(each)
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each, filename, None)


if __name__ == "__main__":
    url = "http://www.whu.edu.cn"
    get_img(open_url(url))



