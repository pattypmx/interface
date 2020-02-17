import requests
import re   # 正则

url1 = ""
# 获取session值
r = requests.session()
res1 = r.get(url1)
print(res1)

# 使用正则获取session
session = re.findall(r'', res1.text)
print(session)

url2 = ""
para = {"session": session[0]}
rr = r.post()



