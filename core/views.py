from django.shortcuts import render, redirect
from item.models import Category, Item

from .forms import SignupForm, LoginForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid:
            form.save()
            return redirect('/')
    else:
        form = SignupForm()

    context = {
        'form': form
    }
    return render(request, 'core/signup.html', context)


def index(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category', 0)
    items = Item.objects.filter(is_sold=False)
    
    context = {
        'categories': categories, 
        'category_id': category_id,       
        'items': items,
    }
    return render(request, 'core/index.html', context)


def contact(request):
    return render(request, 'core/contacts.html')
