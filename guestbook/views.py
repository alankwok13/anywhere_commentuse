from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from . import models
import datetime

# Create your views here.
def index(request):
    messages = models.Message.objects.all()
    return render(request, 'index.html', {'messages' : messages})

def save(request):
    username = request.POST.get("username")
    title = request.POST.get("title")
    content = request.POST.get("content")
    publish = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = models.Message(title=title, content=content, username=username, publish=publish)
    message.save()

    return HttpResponseRedirect('/guestbook/index/')
