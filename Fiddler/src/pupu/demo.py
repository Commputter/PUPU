import requests
import json
import datetime
from time import strftime, sleep
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 头部
headers = {'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat'}
# 地址
url = 'https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/c2bbd3a4-7fce-46c3-949a-0cf95f99c9bb'
# 发起请求
response = requests.get(url=url, headers=headers)
text = response.text
# 转换成json格式
jsonbj = json.loads(text)

# 商品名字
name = jsonbj['data']['name']
# 打折前价格
market_price = (jsonbj['data']['market_price']/100)
# 打折后价格
price = (jsonbj['data']['price']/100)
# 规格
spec = jsonbj['data']['spec']
# 详情
sub_title = (jsonbj['data']['sub_title'])

print("--------------" + name + "----------")
print("规格：" + spec)
print("价格" + str(price))
print("原价/折扣价：" + str(price) + "/" + str(market_price))
print("详细内容：" + sub_title)
print("\n\n--------------" + name + "的价格波动----------")

# 获取时间
print(datetime.datetime.now())

while (1):
    response = requests.get(url=url, headers=headers, verify=False)
    text = response.text
    # 转换成json格式
    jsonbj = json.loads(text)
    price = (jsonbj['data']['price']/100)
    # 获取时间
    time = datetime.datetime.now()
    print(str(time) + "价格为" + str(price))
    # 间隔一段时间
    sleep(3)