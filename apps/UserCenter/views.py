from rest_framework.response import Response
from rest_framework.views import APIView

from UserCenter.settings import userFormat, names


class loadUserInfo(APIView):
    def post(self, request):
        name = "姓名"
        param = request.data["words_result"]
        for item in range(0, len(param)):
            str = param[item]["words"]
            if item == 0:
                name = str
            else:
                for tags in userFormat:
                    for tag in tags:
                        if tag in str:
                            # 判断姓名
                            if tag in names:
                                flag = 0
                                for k in range(1, len(str)):
                                    if str[k] in {'：', ':'}:
                                        flag = k
                                        break
                                name = str[flag + 1:]


                            print(str)
        print(name)
        # print(param["words_result"], type(param["words_result"]))
        return Response({"info": "ok"})