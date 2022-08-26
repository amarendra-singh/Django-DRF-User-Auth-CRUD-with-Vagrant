from rest_framework.views import APIView
from rest_framework.response import Response

class Hello(APIView):
    def get(self, request, format = None):
        apiview = ['Use HTTP methods as function (GET, POST, PATCH, PUT, DELETE)']
        return Response({'message':'hello', 'apiview':apiview})