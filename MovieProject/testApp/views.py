from django.shortcuts import render

from testApp import forms
from testApp.models import Movie


# Create your views here.

def addmovie_view(request):
    form=forms.MovieForm()
    if request.method=='POST':
        form=forms.MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Movie data inserted into database successfully")
        return index_view(request)
    return render(request,'testapp/addmovie.html',{'form':form})

def index_view(request):
    return render(request,'testApp/index.html')


def listmovies_view(request):
    movies_list=Movie.objects.all()
    return render(request,'testApp/listmovies.html',{'movies_list':movies_list})
