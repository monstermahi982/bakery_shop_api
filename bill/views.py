from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import Bill
from .serializers import BillSerializer
from rest_framework.decorators import api_view, renderer_classes, authentication_classes
from rest_framework import status
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

@csrf_exempt
@api_view(('GET','POST'))
@authentication_classes([TokenAuthentication])
def bills(request):
    if request.method == 'GET':
        snippets = Bill.objects.all()
        serializer = BillSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse("hello monster")


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def bill(request, id):
    try:
        product = Bill.objects.filter(user_id=int(id))
    except Bill.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BillSerializer(product, many=True)
        return Response(serializer.data)