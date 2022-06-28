import json

import requests


class Request_Util():
    s = requests.session()

    def request(self, method, url, data, **kwargs):
        method = str(method).lower()
        res = None
        if method == "get":
            res = self.s.get(url=url, params=data, **kwargs)
        else:
            data = json.dumps(data)
            res = self.s.request(method=method, url=url, params=data, **kwargs)
        return res
