import requests
import pytest
from yaml_util import YamlUtil

class Test_Driven:
    @pytest.mark.parametrize("params",[{"keyword":"zarten","appkey":"da39dce4f8aa52155677ed8cd23a6470"}])
    def test_wayjd(self,params):
        url = "https://way.jd.com/jisuapi/newSearch"
        res = requests.get(url, params)
        # res = requests.post(url, json=params)
        assert res.status_code == 200

    @pytest.mark.parametrize("caseinfo",YamlUtil().read_case_yaml("first_case.yaml"))
    def test_baidu(self,caseinfo):
        url = caseinfo["request"]["url"]
        res = requests.get(url)
        YamlUtil().write_asso_yaml({"baidu": res.status_code})
        assert res.ok == True


if __name__ == '__main__':
    pytest.main(["test_data_driven.py"])
