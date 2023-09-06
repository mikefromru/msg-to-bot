from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Message
from . serializers import MessageSerializer

class MessageView(APIView):

    #serializer_class = MessageSerializer

    def get(self, request):
        queryset = Message.objects.all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.error, status=400)

