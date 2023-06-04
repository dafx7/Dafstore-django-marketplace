from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Item
from .forms import NewItemForm


# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {
        'item': item,
        'related_items': Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3],
    }
    return render(request, 'item/details.html', context)


@login_required
def add(request):
    form = NewItemForm()
