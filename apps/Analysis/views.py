from rest_framework.response import Response
from rest_framework.views import APIView


class analysisFiles(APIView):
    def post(self, request):
        param = request.data
        return Response({"param" : param})
