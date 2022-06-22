from django import urls
from django.shortcuts import redirect, render
from .models import Message, Room
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login_page(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'El usuario no existe')
        
        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect("home")        
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    context={'page':page}
    return render(request, 'forum/login_register.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, 'Ha ocurrido un error durante el registro')

    return render(request, 'forum/login_register.html', {'form': form})

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'forum/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')
    context = {'room': room, 'room_messages': room_messages}

    if request.method == "POST":
        
        Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get("new-msg")
        )
        return redirect('room', pk=room.id)

    return render(request, 'forum/room.html', context)

@login_required(login_url='login')
def create_room(request):
    form = RoomForm()

    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():

            room = form.save(commit=False)
            room.host = request.user
            room.save()
            return redirect("home")

    context = {'form': form}
    return render(request, 'forum/room_form.html', context)

@login_required(login_url='login')
def update_room(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('No tiene permitido entrar acá!!')

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid:
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'forum/room_form.html', context)

@login_required(login_url='login')
def delete_room(request,pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('No tiene permitido entrar acá!!')

    if request.method == "POST":
        room.delete()
        return redirect('home')

    return render(request, 'forum/delete_room.html', {'obj':room})

def delete_message(request,pk):
    message = Message.objects.get(id=pk)
    id_room = message.room.id
    if message.was_posted_recently():
        message.delete()
    else:
        messages.error(request, 'Solo se pueden eliminar mensajes creados hace un minuto')
    return redirect('room' ,id_room)