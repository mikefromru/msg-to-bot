from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Message
from . serializers import MessageSerializer
import requests
from project import local_settings
from . send_msg_to_bot import send_message

class MessageView(APIView):

    def get(self, request):
        queryset = Message.objects.all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            msg = str(request.user) + ', я получил от тебя сообщение:' + '\n' + request.data['message']

            send_message(
                local_settings.CHAT_ID,
                local_settings.TOKEN,
                msg,
            )

            return Response(serializer.data, status=201)
        else:
            return Response(serializer.error, status=400)

