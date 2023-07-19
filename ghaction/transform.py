import requests
import json

url = 'https://raw.githubusercontent.com/histcat/friends/main/friends.json'
r = requests.get(url)

r_list = json.loads(r.content)

list_all = []

for item in r_list:
    list = []
    if(item['title'] == "交换友链"):
        continue
    list.append(item['title'])
    list.append(item['link'])
    list.append(item['image'])
    list_all.append(list)

ob_all = {
    "friend": list_all
}


with open('transformed.json', 'w', encoding="Utf-8") as f:
    json.dump(ob_all, f,ensure_ascii=False , indent=4)
