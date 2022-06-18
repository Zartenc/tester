import requests
import pytest

class TestFirst():
    def test_wayjd(self):
        appkey = "da39dce4f8aa52155677ed8cd23a6470"
        url = "https://way.jd.com/jisuapi/newSearch"
        params = {"keyword": "zarten",
                  "appkey": appkey
                  }
        # res = requests.get(url,params)
        res = requests.post(url, json=params)
        print(res.status_code)
        print(res.json())

    def test_baidu(self):
        url = "https://www.baidu.com"
        res = requests.get(url)
        print(res.status_code)
        print(res.text)

if __name__ == '__main__':
    pytest.main()
