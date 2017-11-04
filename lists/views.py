import json

from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from io import StringIO

from lists.models import Item, List


# Create your views here.

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = request.GET.get('error', '')

    if request.method == 'POST':
        item = Item(text=request.POST['item_text'], list=list_)

        try:
            item.full_clean()
            item.save()
        except ValidationError:
            error = 'The item cannot be empty'

        return redirect('/lists/%d/?error=%s' % (list_.id, error))

    return render(request, 'list.html', {
        'list': list_,
        'error': error
    })


def new_list(request):
    list_ = List.objects.create()
    item = Item(text=request.POST.get('item_text', None), list=list_)
    error = ''

    try:
        item.full_clean()
        item.save()
    except ValidationError:
        error = 'The item cannot be empty'
        return render(request, 'home.html', {"error": error})

    return redirect('/lists/%d/?error=%s' % (list_.id, error))
