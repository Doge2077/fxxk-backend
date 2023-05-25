import re

from rest_framework.response import Response
from rest_framework.views import APIView

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


class loadUserInfo(APIView):
    def post(self, request):

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
        }

        anaPerson = {
            "id": 0,
            "skills": "",
            "jobHunt": "",
            "self": "",
            "award": "",
        }

        param = request.data
        for i in range(0, len(param)):
            str = param[i]["words"]
            if i == 0 :
                Person["worker_name"] = str
            else :
                flag = idx(str)
                res = str[flag:]
                no_match = True
                if check(str, Names) and len(res) <= 4 and len(str) <= 7 and not check(str, Edu_school):
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
                if check(str, Location) and not check(str, Award) and len(str) <= 13:
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
                                break
                    Person["edu_level"] = str
                    no_match = False
                if check(str, Statue):
                    Person["statue"] = str if flag == -1 else res
                    no_match = False
                if check(str, Skills) and not check(str, Award):
                    anaPerson["skills"] += str if flag == -1 else res
                    anaPerson["skills"] += "，" if anaPerson["skills"][-1] not in {':', '：'} else ""
                    no_match = False
                if check(str, JobHunt):
                    anaPerson["jobHunt"] = str if flag == -1 else res
                    no_match = False
                if check(str, Award) and not check(str, Skills):
                    anaPerson["award"] += str if flag == -1 else res
                    anaPerson["award"] += "，" if anaPerson["award"][-1] not in {':', '：'} else ""
                    no_match = False
                if no_match and len(str) >= 3 and check(str, {":", "："}) == False:
                    anaPerson["self"] += str
                    anaPerson["self"] += "，" if anaPerson["self"][-1] not in {':', '：'} else ""
        return Response(
            {
                "Person": Person,
                "anaPerson": anaPerson
            }
        )
