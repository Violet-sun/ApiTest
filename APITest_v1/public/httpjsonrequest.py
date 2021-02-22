import requests

from utils.get_case_conf import GetCaseParm


class HttpJsonRequest:

    def __init__(self,var,case):
        p = GetCaseParm()
        self.data = p.json_parse(var,case)

    def send_requet(self):
        send = getattr(requests,self.data["method"])
        rp = send(self.data["url"],self.data)
        return rp.json


