from operator import truediv
from urllib import response
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

class AppUsers(APIView):

    def get(self, request):
        url = "https://randomuser.me/api/?results=50"
        response = requests.get(url)
        response_body = response.json()
        users_data = response_body["results"]

        # Create a list to store user instances
        users_list = []

        # Loop through the user data and create Users instances
        for user_data in users_data:
            user_instance = Users(
                first_name=user_data["name"]["first"],
                last_name=user_data["name"]["last"],
                email="{first}.{last}@gmail.com".format(first=user_data["name"]["first"], last=user_data["name"]["last"])
            )
            users_list.append(user_instance)

        # Bulk create users to improve performance
        Users.objects.bulk_create(users_list)

        # Serialize the created users and return them in the response
        serialized_users = UserSerializer(users_list, many=True)
        
        return Response(serialized_users.data, status=status.HTTP_200_OK)

class BlogPosts(APIView):
    def get(self, request):
        url = "https://davidinmichael.pythonanywhere.com/blog/"
        response = requests.get(url)
        blogs = response.json()
        blog = blogs["results"]
        data = {
            "message": "You request is successfull",
            "blogs": blog,}
        return Response(data, status=status.HTTP_200_OK)
    