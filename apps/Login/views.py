from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache

from UserCenter.views import hash_user, check_registered


class loginUser(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        hash_code = hash_user(username + password)
        User = check_registered(hash_code)
        if User:
            val = User.uid
            key = User.hash_code
            cache.set(key, val)
            return Response({
                "success": "login successfully"
            })
        else:
            return Response({
                "error": "not registered"
            })

