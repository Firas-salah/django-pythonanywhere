from urllib import response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from REST_API.models import Data
from REST_API.serializers import Data_serializer

@api_view(['GET', 'POST'])
def data_list(request, format=None):

#Lists all data objects in json format, and also adds new json objects to database

    if request.method == 'GET':
        data_obj = Data.objects.all()
        serializer = Data_serializer(data_obj, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        
        serializer = Data_serializer(data=request.data)
        
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def data_specific(request, pk, format=None):

# Retrieves, updates, or deletes any specifc data via its id

    try:
        data_obj = Data.objects.get(pk=pk)
    except Data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Data_serializer(data_obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        
        serializer = Data_serializer(data_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        data_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)