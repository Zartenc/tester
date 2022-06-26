import os
import yaml

class YamlUtil:
    def read_asso_yaml(self):
        with open(os.getcwd()+"/asso.yaml",mode="r",encoding="utf-8") as f:
            value =yaml.load(stream=f,Loader=yaml.FullLoader)
            return value

    def write_asso_yaml(self,data):
        with open(os.getcwd()+"/asso.yaml",mode="a",encoding="utf-8") as f:
            yaml.dump(data=data,stream=f,allow_unicode=True)

    def clear_asso_yaml(self):
        with open(os.getcwd()+"/asso.yaml",mode="w",encoding="utf-8") as f:
            f.truncate()

    def read_case_yaml(self,yaml_name):
        with open(os.getcwd()+"/"+yaml_name,mode="r",encoding="utf-8") as f:
            value =yaml.load(stream=f,Loader=yaml.FullLoader)
            return value
