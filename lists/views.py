from django.http import HttpResponse
from django.shortcuts import render, redirect
from lists.models import Item


# Create your views here.

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    print(request.POST['item_text'])
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')
