import hashlib
import re

from rest_framework.response import Response
from rest_framework.views import APIView

from UserCenter import models
from UserCenter.serializer import Worker_Serializer
from UserCenter.settings import *


def check(str, tags):
    for tag in tags:
        if tag in str:
            return True
    if len(str) == 11 and tags == Phone_number:
        for i in str:
            if i < '0' or i > '9':
                return False
        return True
    return False


def birthdata(str):
    if re.match(regex, str):
        return True
    return False


def idx(str):
    for k in range(0, len(str)):
        if str[k] in {'：', ':'}:
            return k + 1
    return -1


def hash_token(Person):
    hash_code = ""
    hash_code += Person["worker_name"] \
                 + Person["sex"] \
                 + Person["age"] \
                 + Person["phone_number"] \
                 + Person["e_mail"] \
                 + Person["statue"]
    Hash_tool = hashlib.sha256()
    Hash_tool.update(hash_code.encode('utf-8'))
    return Hash_tool.hexdigest()


def check_has(hash_code):
    return models.Worker.objects.filter(hash_code=hash_code).first()


class loadUserInfo(APIView):
    def post(self, request):
        # Worker 字段字典
        Person = {
            "view": 2,
            "worker_name": "",
            "sex": "男",
            "age": "",
            "phone_number": "",
            "e_mail": "",
            "location": "",
            "edu_school": "",
            "edu_level": "",
            "work_year": 0,
            "statue": "群众",
            "hash_code": ""
        }
        # 用于分析的字段
        anaPerson = {
            "id": 0,
            "skills": "",
            "jobHunt": "",
            "self": "",
            "award": ""
        }

        param = request.data
        # 匹配字段
        for i in range(0, len(param)):
            str = param[i]["words"]
            if i == 0:
                Person["worker_name"] = str
            flag = idx(str)
            res = str[flag:]
            no_match = True
            if check(str, Names) and len(res) <= 4 and len(str) <= 7 and not check(str, Noname):
                Person["worker_name"] = str if flag == -1 else res
                no_match = False
            if check(str, Sex):
                Person["sex"] = str if flag == -1 else res
                no_match = False
            if check(str, Age) or birthdata(str):
                Person["age"] = str if flag == -1 else res
                no_match = False
            if check(str, Phone_number):
                if len(str) >= 11:
                    Person["phone_number"] = str if flag == -1 else res
                no_match = False
            if check(str, E_mail):
                Person["e_mail"] = str if flag == -1 else res
                no_match = False
            if check(str, Location) and not check(str, Edu_school | Award) and len(str) <= 13:
                Person["location"] = str if flag == -1 else res
                no_match = False
            if check(str, Edu_school) and len(str) <= 13:
                Person["edu_school"] = str if flag == -1 else res
                no_match = False
            if check(str, Edu_level):
                str = str if flag == -1 else res
                if len(str) > 2:
                    for tag in Edu_level:
                        if tag in str:
                            str = tag
                            if str == "专科":
                                str = "大专"
                            break
                Person["edu_level"] = str
                no_match = False
            if check(str, Statue):
                str = str if flag == -1 else res
                if len(str) > 2:
                    for tag in Statue:
                        if tag in str:
                            str = tag
                            break
                Person["statue"] = str
                no_match = False
            if check(str, Skills) and not check(str, Award):
                anaPerson["skills"] += str if flag == -1 else res
                anaPerson["skills"] += "，" if anaPerson["skills"][-1] not in {':', '：'} else ""
                no_match = False
            if check(str, JobHunt):
                anaPerson["jobHunt"] = str if flag == -1 else res
                no_match = False
            if check(str, Award) and not check(str, Skills | Action):
                anaPerson["award"] += str if flag == -1 else res
                anaPerson["award"] += "，" if anaPerson["award"][-1] not in Flag else ""
                no_match = False
            if check(str, Action) or no_match and len(str) >= 3 and check(str, Flag) == False:
                anaPerson["self"] += str
                anaPerson["self"] += "，" if anaPerson["self"][-1] not in Noneed else ""

        # 计算该 worker 的 hash_code
        hash_code = hash_token(Person)
        # 查询是否存在 Worker
        Worker = check_has(hash_code)
        if Worker:
            Person["hash_code"] = hash_code
            anaPerson["id"] = Worker.wid
        else:
            Person["hash_code"] = hash_code
            # 将 Person 序列化
            Worker = Worker_Serializer(Person)
            # 插入一条 Worker 记录
            models.Worker.objects.create(**Worker.data)
            anaPerson["id"] = check_has(hash_code).wid

        return Response(
            {
                "Person": Person,
                "anaPerson": anaPerson
            }
        )
