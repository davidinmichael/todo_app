from operator import truediv
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import *
from .models import *


class TodoListCreate(APIView):

    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Todo Created successfully",
                "todo": serializer.data,
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoUpdateDelete(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Todo Updated successfully",
                "todo": serializer.data,
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        todo.delete()
        message = {"message": "Todo deleted successfully"}
        return Response(message, status=status.HTTP_200_OK)

class RandomUsers(APIView):
    def get(self, request):
        url = "https://randomuser.me/api/?results=10"
        response = requests.get(url)
        users_results = response.json()
        users = users_results["results"]
        # users = users_results.get("results", [])
        emails = [result["email"] for result in users]
        new_domain = "@gmail.com"
        # first_names = [result['name']['first'] for result in users]
        results = [email.split("@")[0] + new_domain for email in emails]
        data = {
            "message": "You request is successfull",
            "emails": results,}
        return Response(data, status=status.HTTP_200_OK)
    