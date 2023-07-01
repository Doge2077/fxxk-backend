from rest_framework.response import Response
from rest_framework.views import APIView

from Analysis.tools import workerModel
from UserCenter.models import Have, Worker
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