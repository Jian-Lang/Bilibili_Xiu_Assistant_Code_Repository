# encoding:utf-8
import json

import requests

response1 = requests.get(
    'https://api.bilibili.com/x/relation/followings?vmid=34243853')
# 获取用户所关注用户的api
print(response1.json())

response2 = requests.get(
    'https://api.bilibili.com/x/web-interface/search/type?&page=1&keyword=每日新闻&search_type=bili_user&order=fans')
user_dict = json.loads(response2.content.decode())
for num in range(0,len(user_dict['data']['result'])):
    print(user_dict['data']['result'][num]['uname'])
    print(user_dict['data']['result'][num]['usign'].replace('\n', ''))

response3 = requests.get('https://api.bilibili.com/x/space/arc/search?pn=1&ps=100&keyword=&mid=1935882')
print(response3.json())

response = requests.get('http://api.bilibili.com/x/web-interface/view?bvid=BV117411r7R1')
print(response.json())


