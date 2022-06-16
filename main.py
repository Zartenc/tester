import requests

appkey="da39dce4f8aa52155677ed8cd23a6470"
url="https://way.jd.com/jisuapi/newSearch?keyword=zar&appkey={}".format(appkey)
res = requests.get(url)
print(res.status_code)
print(res.json())
