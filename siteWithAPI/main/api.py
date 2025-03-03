from http.client import responses
from types import NoneType

import requests


#http://127.0.0.1:8080/api/request?table=users&method=read&id=&username=&uniq_key=&role=0

class API:
    def __init__(self, path):
        self.path = path
        self.query_param = None

    def set_query(self, *args, table=None, method=None):
        for arg in args:
            if not isinstance(arg, tuple):
                return {"err": f"QueryArgs must be tuple not {type(args)}"}
        if table is None or method is None:
            return "API.set_query() must include table and method"
        query_ = "&".join([arg[0]+"="+arg[1] for arg in args])
        query_base = f"request?table={table}&method={method}&"+query_
        self.query_param = query_base + query_
        return True

    def send_request(self):
        if not self.query_param:
            return {"err": f"QueryParam is None. Need to execute set_query() before"}
        response = requests.get("".join([self.path, self.query_param]))
        if response.status_code == 200:
            self.query_param = None
            json_response = response.json()
            return  json_response
        else:
            self.query_param = None
            return {"err": f"Request exit with code {response.status_code}\nErr message: {response.text}"}