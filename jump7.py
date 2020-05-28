import requests

def getinfo(url):
    try:
        kv={'kw':'Python'}
        r=requests.get(url,params=kv)
        r.encoding=r.apparent_encoding
        r.raise_for_status()
        return r.text[:500]
    except:
        return "Error"
def main():
    url = 'http://baidu.com/s'
    text=getinfo(url)
    print(text)
if __name__== '__main__':
    main()
