from rest_framework.response import Response
from rest_framework.views import APIView

from Analysis.tools import workerModel, jobModel
from UserCenter.models import Have, Worker, Job
from UserCenter.tools import confirmUser


class loadAllInfo(APIView):
    def post(self, request):
        param = request.data
        token = param["token"]
        page = param["page"]
        userid = confirmUser(token)
        if userid == -1:
            return Response({
                "error": "user token not existed"
            })

        records_have = Have.objects.filter(uid=userid)
        workers = []
        for have in records_have:
            wid = have.wid
            worker = Worker.objects.filter(wid=wid).first()
            param = workerModel(worker)
            workers.append(param)

        per_page = 10  # 每页显示的元素数量
        page_number = page  # 假设当前页码为1
        start_index = (page_number - 1) * per_page  # 计算切片开始的索引
        end_index = start_index + per_page  # 计算切片结束的索引
        sliced_workers = workers[start_index:end_index]  # 对workers数组进行切片操作

        return Response({
            "success": sliced_workers
        })

class loadOneJob(APIView):
    def post(self, request):
        param = request.data
        token = param["token"]
        id = param["id"]
        userid = confirmUser(token)
        if userid == -1:
            return Response({
                "error": "user token not existed"
            })

        record_job = Job.objects.filter(jid=id)
        job = jobModel(record_job)
        if job:
            return Response(job)
        else:
            return Response({
                "error": "job not found"
            })

class loadAllJob(APIView):
    def post(self, request):
        param = request.data
        token = param["token"]
        userid = confirmUser(token)
        if userid == -1:
            return Response({
                "error": "user token not existed"
            })
        record_jobs = Job.objects.all()
        jobs = []
        for job in record_jobs:
            jobs.append({
                "id": job.jid,
                "job_name": job.jname
            })

        if len(jobs) != 0:
            return Response({
                "content": jobs
            })
        else:
            return Response({
                "error": "no job exist"
            })


class loadNameInfo(APIView):
    def post(self, request):
        param = request.data
        token = param["token"]
        key = param["key"]
        userid = confirmUser(token)
        if userid == -1:
            return Response({
                "error": "user token not existed"
            })

        record_workers = Worker.objects.filter(worker_name__contains=key)
        workers = []
        for worker in record_workers:
            workers.append(workerModel(worker))

        if len(workers) > 0:
            return Response({
                "content": workers
            })
        else:
            return Response({
                "error": "worker not existed"
            })