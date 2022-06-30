from re import L
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from forum.models import Room
from .serializers import RoomSerializer, MessageSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def get_rooms(request):

    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = RoomSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detail_room(request, pk):
    try:
        room = Room.objects.get(id=pk)
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    


    if request.method == 'GET':
        serializer = RoomSerializer(room)
        return Response(serializer.data)

    if request.method == 'PUT':
        
        if room.host != request.user:
            return Response('No esta autorizado a modificar salas que no son las suyas',status=status.HTTP_401_UNAUTHORIZED)

        data=JSONParser().parse(request)
        serializer = RoomSerializer(room,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':

        if room.host != request.user:
            return Response('No esta autorizado a eliminar salas que no son las suyas',status=status.HTTP_401_UNAUTHORIZED)

        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_messages(request, pk):
    room = Room.objects.get(id=pk)
    messages = room.message_set.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)