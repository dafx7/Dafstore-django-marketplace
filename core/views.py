from django.shortcuts import render
from item.models import Category, Item


# Create your views here.
def index(request):
    context = {
        'categories': Category.objects.all(),        
        'items': Item.objects.filter(is_sold=False)[0:6],
    }
    return render(request, 'core/index.html', context)


def contact(request):
    return render(request, 'core/contacts.html')
