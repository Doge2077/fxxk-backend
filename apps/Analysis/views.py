import base64

from rest_framework.response import Response
from rest_framework.views import APIView

from Analysis.tools import *


class loadInfo(APIView):
    def post(self, request):
        param = request.data["data"]
        fileType = checkFileType(param)
        fileData = base64.b64decode(FileData(param))
        addFile(fileData, fileType)
        return Response({
            "type": fileType
        })
