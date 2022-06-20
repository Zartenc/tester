import requests
import pytest


@pytest.fixture(scope="function")
def conn_sql():
    print("start connect sql...")
    yield
    print("end connect sql...")


class TestFirst():
    def setup(self):
        print("it's executed--------------")

    def test_wayjd(self):
        appkey = "da39dce4f8aa52155677ed8cd23a6470"
        url = "https://way.jd.com/jisuapi/newSearch"
        params = {"keyword": "zarten",
                  "appkey": appkey
                  }
        res = requests.get(url, params)
        # res = requests.post(url, json=params)
        print(res.status_code)
        print(res.json())

    def test_baidu(self):
        url = "https://www.baidu.com"
        res = requests.get(url)
        print(res.status_code)

    def test_qq(self, conn_sql):
        url = "https://www.qq.com"
        res = requests.get(url)
        print(res.status_code)


if __name__ == '__main__':
    pytest.main([])
