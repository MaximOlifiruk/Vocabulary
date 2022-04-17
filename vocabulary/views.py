from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Word
 
# получение данных из бд
def index(request):
    return render(request, "vocabulary/index.html")

def create(request):
    return render(request, "vocabulary/create.html")

def read(request):
    words = Word.objects.all()
    return render(request, "vocabulary/read.html", {"words": words} )

def create_word(request):
    if request.method == "POST":
        new_word = Word()
        new_word.word = request.POST.get("word")
        new_word.translation = request.POST.get("translation")
        new_word.save()
    return HttpResponseRedirect("/")

def edit(request, id):
    try:
        edit_word = Word.objects.get(id=id)
 
        if request.method == "POST":
            edit_word.word = request.POST.get("word")
            edit_word.translation = request.POST.get("translation")
            edit_word.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "vocabulary/edit.html", {"edit_word": edit_word})
    except Word.DoesNotExist:
        return HttpResponseNotFound("<h2>Edit_word not found</h2>")
     
# удаление данных из бд
def delete(request, id):
    try:
        delete_word = Word.objects.get(id=id)
        delete_word.delete()
        return HttpResponseRedirect("/")
    except Word.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")