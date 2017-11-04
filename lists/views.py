import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from io import StringIO

from lists.models import Item, List


# Create your views here.

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    errors = request.GET.get('errors', None)

    if errors is not None:
        errors = json.loads(errors)

    return render(request, 'list.html', {
        'list': list_,
        'errors': errors
    })


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id))


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    item_text = request.POST.get('item_text', None)

    if item_text is None or len(item_text) == 0:
        errors = ['The item cannot be empty']
    else:
        errors = []
        Item.objects.create(text=request.POST['item_text'], list=list_)

    return redirect('/lists/%d/?errors=%s' % (list_.id, json.dumps(errors)))
