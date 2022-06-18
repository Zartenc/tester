import requests

appkey = "da39dce4f8aa52155677ed8cd23a6470"
url = "https://way.jd.com/jisuapi/newSearch"
params = {"keyword": "zarten",
          "appkey": appkey
          }
# res = requests.get(url,params)
res = requests.post(url, data=params)
print(res.status_code)
print(res.json())
