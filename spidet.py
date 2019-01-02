from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen(
    "https://news.163.com/19/0102/11/E4GUB4D80001875N.html"
).read().decode('GBK')
print(html)
