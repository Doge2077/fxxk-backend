def workerModel(worker):
    return ({
        "id":worker.fileid,
        "name":worker.worker_name,
        "sex":worker.sex,
        "age":worker.age,
        "education":worker.edu_level,
        "college":worker.edu_school
    })