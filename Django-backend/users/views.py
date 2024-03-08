from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import MyInfoUserSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ParseError    # 비밀번호 규칙 검증 (8자리 이상 등)

# Create your views here.
# api/v1/users [POST] → 유저 생성 API
class Users(APIView):
    def post(self, request):
        # password → 검증 필요, 해쉬화해서 저장 필요
        password = request.data.get('password')
        serializer = MyInfoUserSerializer(data=request.data)

        try:
            validate_password(password)
        except:
            raise ParseError('Invalid password')
        
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()

            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        else:
            return ParseError(serializer.errors)
        # the other → 비밀번호 외 다른 데이터들

# api/v1/users/myinfo [GET,Put] → 유저 프로필 업데이트
class MyInfo(APIView):
    # read
    def get(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user)
        return Response(serializer.data)
    
    # update
    def put(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        else:
            return ParseError(serializer.errors)