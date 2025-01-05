from django.shortcuts import render

from django.http import HttpResponse

from .forms import BookForm 

from .models import Book 

# Create your views here.
def home(request):
    context={}
    return render(request,"myApp/home.html",context)


def book_data(request):
  if request.method =='POST':
    form = BookForm(request.POST)
    if form.is_valid():
        name= form.cleaned_data['bk_name']
        number = form.cleaned_data['bk_number']
        book1 = Book.objects.create(bk_name = name, 
                  bk_number = number                  )
        
        book1.save()


  form = BookForm()
  return render (request,'myApp/book.html', {'form':form})

    