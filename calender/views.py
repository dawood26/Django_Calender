from django.shortcuts import render,get_object_or_404
from .models import Entry
from .forms import Entryform
from django.http import HttpResponseRedirect
from django.http import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse('it works hurray')
    entries=Entry.objects.all()
    context = { 'entries' : entries}
    return render(request,'calender/index.html',context)


def calender(request):
    #return HttpResponse('it works hurray')
    entries=Entry.objects.all()
    context = { 'entries' : entries}
    return render(request,'calender/calender.html',context)

def details(request,pk):
    entry = Entry.objects.get(pk=pk)
    context = {'entry': entry}
    return render(request, 'calender/details.html',context)

def add(request):

    if request.method == 'POST':

        form = Entryform(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']

            date = form.cleaned_data['date']

            description = form.cleaned_data['description']

            Entry.objects.create(name=name,date=date,description=description,).save()

            return HttpResponseRedirect('/')

    else:
        form = Entryform()

    return render(request,'calender/form.html',{'form':form})

def delete(request,pk):

    if request.method == 'DELETE':

        entry = get_object_or_404(Entry,pk=pk)
        entry.delete()

    return HttpResponseRedirect('/')
