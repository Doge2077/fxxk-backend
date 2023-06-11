import hashlib
import re

from bson import regex
from UserCenter import models
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


def hash_user(str):
    Hash_tool = hashlib.sha256()
    Hash_tool.update(str.encode('utf-8'))
    return Hash_tool.hexdigest()


def hash_token(Person):
    hash_code = ""
    hash_code += Person["worker_name"] \
                 + Person["sex"] \
                 + Person["age"] \
                 + Person["phone_number"] \
                 + Person["e_mail"] \
                 + Person["statue"]
    return hash_user(hash_code)


def hash_work(Work):
    hash_code = ""
    hash_code += Work["jname"] \
                 + str(Work["jneed_age"]) \
                 + Work["jneed_edu"] \
                 + Work["jneed_other"] \
                 + str(Work["jneed_year"])
    return hash_user(hash_code)


def check_has(hash_code):
    return models.Worker.objects.filter(hash_code=hash_code).first()


def check_work(hash_code):
    return models.Job.objects.filter(hash_code=hash_code).first()


def check_registered(hash_code):
    return models.User.objects.filter(hash_code=hash_code).first()
