from django.shortcuts import render
from django.http import HttpResponse
#from forms import SearchForm
import subprocess
#from .models import Greeting
import datetime as dt
import importlib
#Imports the function that calculates odds from Cool-Beans_Project.
from .main import trumpGuess
from .main import guess2


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def search(request):
  print("In search")
  #form = SearchForm
  if request.method == 'POST':
    info = request.POST['search']
    #What is currently the get_tweets function can be changed to whatever function outputs a number.
    output = guess2(info)
    return render(request, 'index.html', {
        'info': info,
        'output': output,
    })
  return render(request, 'index.html', {
    'form': form,
  })

def Donald(request):
  print("In search")
  if request.method == 'POST':
    #What is currently the get_tweets function can be changed to whatever function outputs a number.
    output2 = trumpGuess()
    return render(request, 'index.html', {
        'output2': output2,
    })
  return render(request, 'index.html', {
    'form': form,
  })


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


