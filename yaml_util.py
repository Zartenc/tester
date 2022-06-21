import os
import yaml

class YamlUtil:
    def read_asso_yaml(self,key):
        with open(os.getcwd()+"/asso.yaml",mode="r",encoding="utf-8") as f:
            value =yaml.load(stream=f,Loader=yaml.FullLoader)
            return value[key]

    def write_asso_yaml(self,data):
        with open(os.getcwd()+"/asso.yaml",mode="w",encoding="utf-8") as f:
            yaml.dump(data=data,stream=f,allow_unicode=True)