# 导入包
import requests

# 定义地址和参数
url = "http://apis.juhe.cn/rubbish/category"
para = {"key": "69d22f4f8f10f5dbbd34345eda9d80e"}

# 使用post请求
r = requests.post(url, data=para)

# 获取json数据
res = r.json()
print(res)
print(res["error_code"])

