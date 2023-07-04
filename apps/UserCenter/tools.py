import hashlib
import parser

import re

from bson import regex
from django.core.cache import cache

from UserCenter import models
from UserCenter.settings import *

from datetime import datetime, timedelta
import random

tools_person = {
    "fileid": "",
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

tools_anaperson = {
    "id": 0,
    "skills": "",
    "jobHunt": "",
    "self": "",
    "award": ""
}


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


def hash_user(str):
    Hash_tool = hashlib.sha256()
    Hash_tool.update(str.encode('utf-8'))
    return Hash_tool.hexdigest()


def hash_token(Person):
    hash_code = ""
    hash_code += str(str(Person["worker_name"]) \
                     + str(Person["sex"]) \
                     + str(Person["age"]) \
                     + str(Person["phone_number"]) \
                     + str(Person["e_mail"]) \
                     + str(Person["statue"]))
    return hash_user(hash_code)


def hash_work(Work):
    hash_code = ""
    hash_code += str(Work["jname"]) \
                 + str(str(Work["jneed_age"])) \
                 + str(Work["jneed_edu"]) \
                 + str(Work["jneed_other"]) \
                 + str(str(Work["jneed_year"]))
    return hash_user(hash_code)


def check_has(hash_code):
    return models.Worker.objects.filter(hash_code=hash_code).first()


def check_work(hash_code):
    return models.Job.objects.filter(hash_code=hash_code).first()


def check_registered(hash_code):
    return models.User.objects.filter(hash_code=hash_code).first()


def confirmUser(token):
    uid = cache.get(token)
    if uid:
        return uid
    else:
        User = check_registered(token)
        if User:
            val = User.uid
            key = User.hash_code
            cache.set(key, val)
            return val
        else:
            return -1


def generate_random_date(start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year + 1, 1, 1) - timedelta(days=1)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date


def calculate_age(birthdate):
    try:
        birthdate = parser.parse(birthdate)
    except:
        birthdate = generate_random_date(1990, 2000)
    current_date = datetime.now()
    age = current_date.year - birthdate.year
    # 比较月份和日期来调整年龄
    if (current_date.month, current_date.day) < (birthdate.month, birthdate.day):
        age -= 1

    return age
