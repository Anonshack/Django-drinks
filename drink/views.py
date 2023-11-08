from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .model import Drink
from .serializers import DrinkSerializers


@api_view(['GET', 'POST'])
def drink_list(request):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializers(drinks, many=True)
        return Response({"drinks": serializer.data})

    if request.method == 'POST':
        serializer = DrinkSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DrinkSerializers(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DrinkSerializers(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response({"res": "deleted"})
