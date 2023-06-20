import base64

from rest_framework.response import Response
from rest_framework.views import APIView

from Analysis.tools import *
from Login.views import confirmUser


class loadInfo(APIView):
    def post(self, request):
        hash_code = request.data["token"]
        uid = confirmUser(hash_code)
        if uid == -1:
            return Response({
                "error": "user not allowed"
            })
        else:
            param = request.data["baseByte"]
            fileType = checkFileType(param)
            fileData = base64.b64decode(FileData(param))
            addFile(fileData, fileType)
            return Response({
                "success": "add a worker file"
            })
