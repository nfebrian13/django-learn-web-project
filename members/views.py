from builtins import print

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Members


def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname=x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('index'))


def index4(request):
    mymembers = Members.objects.all().values()
    output = ""
    for x in mymembers:
        output += x["firstname"]
    return HttpResponse(output)


def index3(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


def index2(request):
    return HttpResponse("Hello world!")


def hello(request):
    template = loader.get_template('hello.html')
    return HttpResponse(template.render({}, request))


def hello_input(request):
    full_name = request.POST['first']
    template = loader.get_template('hello_world.html')
    context = {
        'full_name': full_name,
    }
    return HttpResponse(template.render(context, request))
