import json

import requests

if __name__ == "__main__":
    l = []
    for i in range(1, 301):
        url = 'http://127.0.0.1:8000/usercenter/loadinfo/'
        with open(f"./json/{i}.json", mode="r", encoding="utf-8") as f:
            k = json.loads(f.read())
        data = {
            "conList": k,
            "id": i,
            "token": "d82494f05d6917ba02f7aaa29689ccb444bb73f20380876cb05d1f37537b7892"
        }
        try:
            print(i,end=" ")
            res = requests.post(url=url, json=data)
            print(res)
        except:
            print(f"{i}失败请重试")

