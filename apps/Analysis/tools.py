def workerModel(worker):
    return ({
        "id":worker.fileid,
        "name":worker.worker_name,
        "sex":worker.sex,
        "age":worker.age,
        "education":worker.edu_level,
        "college":worker.edu_school
    })

def jobModel(job):
    return ({
        "jname": job.jname,  # 工作名称
        "jneed_age": job.jneed_age,  # 年龄要求 25表示25岁以上 -25 表示25岁以下
        "jneed_edu": job.jneed_edu,  # 教育要求
        "jneed_year": job.jneed_year,  # 工作经验
        "jneed_other": job.jneed_other,  # 其他所有的要求
    })