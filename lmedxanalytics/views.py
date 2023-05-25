from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

@api_view(['GET'])
def hello_world(request):
    return render(request, 'lmedxanalytics/index.html')

@api_view(['GET'])
def hello_world2(request):
    return Response({'msg' : 'success'}, status=200)