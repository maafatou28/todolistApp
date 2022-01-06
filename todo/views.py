from django import forms
from django.shortcuts import redirect, render, get_object_or_404
from . forms import FormTask
from .models import Task
# Create your views here.
def index(request ):
    form =FormTask(request.POST or None )
    if form.is_valid():
        form.save() 

    list = Task.objects.all()

    context = {
        'form' : form,
        'taches':list,
    }
    return render(request, 'index.html', context) 


def update(request, pk):
    obj = get_object_or_404 (Task, id=pk)
    form = FormTask(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form })  


def delete(request, pk):
    obj = get_object_or_404(Task, id=pk)
    obj.delete()
    return redirect('/')    