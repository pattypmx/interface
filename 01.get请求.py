import requests

url = "http://apis.juhe.cn/rubbish/category"
para = {"key": "69d22f4f8f10f5dbbd34345eda9d80e1"}

r = requests.get(url, params=para)
res = r.json()
print(res)
print(res["result"])
print(res["result"][0]['id'])
