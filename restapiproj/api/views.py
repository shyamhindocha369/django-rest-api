from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from .models import *
@api_view(['GET'])
def endpoints(request):
    data = {
        'Viewall': '/api/viewall/',
        'Viewa Only One': '/api/view/<int:pk>/',
        'Post data': '/api/putdata/',
        'Delete': '/api/delete/<int:id>/',
        'Update': '/api/update/<int:id>/',
        'search': '/api/search/',
    }
    return Response(data)

@api_view(['GET'])
def list_fooddata(request):
    data = fooddata.objects.all()
    serializer = FoodDataSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_fooddata(request):
    serializer = FoodDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_fooddata(request, pk):
    try:
        instance = fooddata.objects.get(pk=pk)
    except fooddata.DoesNotExist:
        return Response({"error": "FoodData not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = SingleFoodDataSerializer(instance)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_fooddata(request, id):  
    try:
        instance = fooddata.objects.get(id=id)
    except fooddata.DoesNotExist:
        return Response({"error": "FoodData not found"}, status=status.HTTP_404_NOT_FOUND)

    instance.delete()
    return Response({"message": "FoodData deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT', 'PATCH'])
def update_fooddata(request, id):
    try:
        instance = fooddata.objects.get(id=id)
    except fooddata.DoesNotExist:
        return Response({"error": "FoodData not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = FoodDataUpdateSerializer(instance, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def search_fooddata(request):
    query = request.query_params.get('query', '')
    
    if not query:
        return Response({"error": "Please provide a search query"}, status=status.HTTP_400_BAD_REQUEST)

    
    results = fooddata.objects.filter(
        
        area_abbreviation_1__icontains=query
    )

    serializer = FoodDataSerializer(results, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
