import hashlib
import parser
from math import ceil

from bson import regex
from django.core.cache import cache

from UserCenter import models
from UserCenter.settings import *

from datetime import datetime, timedelta
import random

from datetime import datetime
import re

tools_person = {
    "fileid": "",
    "worker_name": "",
    "sex": "男",
    "age": None,
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


def extract_dates(text):
    pattern = r"\b(\d{4})[年.-](\d{1,2})[月.-]?(\d{1,2})?[日号]?\b"
    dates = sorted(
        [
            f"{year}.{month.zfill(2)}.{day.zfill(2) if day else '01'}"
            for year, month, day in re.findall(pattern, text)
            if is_valid_date(year, month, day)
        ]
    )
    return dates


def is_valid_date(year, month, day):
    try:
        date_str = f"{year}-{month.zfill(2)}-{day.zfill(2) if day else '01'}"
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def calculate_year(dates):
    sum_diff = 0
    for i in range(0, len(dates) - 1, 2):
        date1 = datetime.strptime(dates[i], "%Y.%m.%d")
        date2 = datetime.strptime(dates[i + 1], "%Y.%m.%d")
        diff = (date2 - date1).days
        sum_diff += diff
    return ceil(sum_diff / 365)


def calculate_work_year(work_years):
    size = len(work_years)
    year = 0
    if size == 0:
        return random.randint(0, 10)
    if size % 2 == 0:
        year = calculate_year(work_years)
    else:
        year1 = calculate_year(work_years[1:])
        year2 = calculate_year(work_years[:-1])
        year = ceil((year1 + year2) / 2)
    # year = calculate_year(work_years)
    return year


def calculate_age(birthdate):
    try:
        birthdate = parser.parse(birthdate)
    except:
        age = re.findall(r'\d+', str(birthdate))
        if len(age) == 1:
            return age[0]
        else:
            birthdate = generate_random_date(1990, 2000)
    current_date = datetime.now()
    age = current_date.year - birthdate.year
    # 比较月份和日期来调整年龄
    if (current_date.month, current_date.day) < (birthdate.month, birthdate.day):
        age -= 1

    return age
