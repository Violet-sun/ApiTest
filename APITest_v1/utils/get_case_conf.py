import json
import re

from utils.read_ini import ReadIni

class GetCaseParm:


    def json_parse(self,var,case): # file_conf,file_var
        cp = ReadIni(var)
        #with open("../case/test001.json", 'r') as f:
        with open(case) as f:
            json_str = f.read()
            r = re.findall("\\$\\$\\{(.+?)\\}",json_str)
            for i in r:
                json_str = json_str.replace("$${"+i+"}",cp.get_value("Node1",i))
        print(json.loads(json_str))
        return json.loads(json_str)
