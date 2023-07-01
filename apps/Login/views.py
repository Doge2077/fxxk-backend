from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache

from UserCenter import models
from UserCenter.serializer import User_Serializer
from UserCenter.views import hash_user, check_registered


class registerUser(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        hash_code = hash_user(username + password)

        Person = {
            "hash_code": ""
        }

        # 检查是否注册过
        User = check_registered(hash_code)

        if User:
            return Response({
                "error": "registered"
            })
        else:
            Person["hash_code"] = hash_code
            User = User_Serializer(Person)
            models.User.objects.create(**User.data)
            uid = check_registered(hash_code).uid
            return Response({
                "token": hash_code,
                "success": "finished"
            })


class loginUser(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        hash_code = hash_user(username + password)
        # 检查是否注册过
        User = check_registered(hash_code)

        if User:
            val = User.uid
            key = User.hash_code
            # 存储到 redis
            cache.set(key, val)
            return Response({
                "token": key,
                "success": "login successfully"
            })
        else:
            return Response({
                "error": "not registered"
            })



