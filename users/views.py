from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view, renderer_classes,authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny

# user logic code
@csrf_exempt
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
@api_view(['GET', 'PUT', 'DELETE'])
def user(request, id):
    try:
        product = User.objects.get(id=id)
        print(product)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @authentication_classes([TokenAuthentication])
# @permission_classes([AllowAny])
@csrf_exempt
@api_view(['POST', 'GET'])
def users(request):
    if request.method == 'GET':
        snippets = User.objects.filter(is_superuser=False)
        print(snippets)
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# owner logic code
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
@csrf_exempt
@api_view(['POST', 'GET'])
def owners(request):
    if request.method == 'GET':
        snippets = User.objects.filter(is_superuser=True)
        print(snippets)
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)

@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def owner(request, id):
    try:
        product = User.objects.get(id=id)
        print(product)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
