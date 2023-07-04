from rest_framework.response import Response
from rest_framework.views import APIView

from UserCenter.models import mycol
from UserCenter.serializer import *
from UserCenter.tools import *


class loadUserInfo(APIView):
    def post(self, request):
        # Worker 字段字典
        Person = tools_person
        # 用于分析的字段
        anaPerson = tools_anaperson
        token = request.data["token"]

        userid = confirmUser(token)
        if userid == -1:
            return Response({
                "error": "user token not existed"
            })

        Person["fileid"] = request.data["id"]
        param = request.data["conList"]
        # 匹配字段
        for i in range(0, len(param)):
            str = param[i]["words"]
            if i == 0:
                Person["worker_name"] = str
            flag = idx(str)
            res = str[flag:]
            no_match = True
            if check(str, Names) and len(res) <= 4 and 2 <= len(str) <= 7 and not check(str, Noname):
                if flag == -1:
                    Person["worker_name"] = str
                else:
                    if 2 <= len(res) <= 4:
                        Person["worker_name"] = res
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
                if len(str) > 5:
                    Person["e_mail"] = str if flag == -1 else res
                no_match = False
            if check(str, Location) and not check(str, Edu_school | Award) and len(str) <= 13:
                Person["location"] = str if flag == -1 else res
                no_match = False
            if check(str, Edu_school) and len(str) <= 13 and not check(str, Noschool):
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
                no_match = False
            if check(str, JobHunt):
                anaPerson["jobHunt"] = str if flag == -1 else res
                no_match = False
            if check(str, Award) and not check(str, Skills | Action):
                anaPerson["award"] += str if flag == -1 else res
                no_match = False
            if check(str, Action) or no_match and len(str) >= 3 and check(str, Flag) == False:
                anaPerson["self"] += str

        Person["age"] = calculate_age(Person["age"])
        print(Person)
        # 计算该 worker 的 hash_code
        hash_code = hash_token(Person)
        # 查询是否存在 Worker
        Worker = check_has(hash_code)
        if Worker:
            return Response({
                "error": "worker existed"
            })
        else:
            Person["hash_code"] = hash_code
            # 将 Person 序列化
            Worker = Worker_Serializer(Person)
            # 插入一条 Worker 记录
            models.Worker.objects.create(**Worker.data)
            wid = check_has(hash_code).wid
            anaPerson["id"] = wid
            have = {
                "uid": userid,
                "wid": wid
            }
            # 将关系序列化
            Have = Have_Serializer(have)
            models.Have.objects.create(**Have.data)
            # 将 anaPerson 存入 MongoDB
            mycol.insert_one(anaPerson)

        # return Response(
        #     {
        #         "Person": Person,  # 返回信息
        #         "anaPerson": anaPerson
        #     }
        # )
        return Response({
            "success": "ok"
        })


class addWorkNeed(APIView):
    def post(self, request):
        param = request.data
        hash_code = hash_work(param)
        Work = check_work(hash_code)
        Job = {
            "jname": param['jname'],  # 工作名称
            "jneed_age": param['jneed_age'],  # 年龄要求 25表示25岁以上 -25 表示25岁以下
            "jneed_edu": param['jneed_edu'],  # 教育要求
            "jneed_year": param['jneed_year'],  # 工作经验
            "jneed_other": param['jneed_other'],  # 其他所有的要求
            "hash_code": ""
        }
        if Work:
            return Response({
                "error": "The work has existed"
            })
        else:
            Job['hash_code'] = hash_code
            Job = Job_Serializer(Job)
            models.Job.objects.create(**Job.data)
            return Response(Job.data)
