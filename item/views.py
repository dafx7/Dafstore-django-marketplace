from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Item, Category, ItemImage
from .forms import NewItemForm, EditItemForm


# Create your views here.
def items(request):
    query = request.GET.get('query', '')
    categories = Category.objects.all()
    category_id = request.GET.get('category', 0)
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category=category_id)

    if query:
        items = items.filter(Q(name__contains=query) |
                             Q(description__contains=query))

    context = {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    }
    return render(request, 'item/items.html', context)


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    images = item.images.all
    context = {
        'item': item,
        'images': images,
        'related_items': Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3],
    }
    return render(request, 'item/details.html', context)


@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        uploaded_images = request.FILES.getlist('images')

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            for i in uploaded_images:
                ItemImage(item=item, images=i).save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    context = {
        'form': form,
        'title': 'New item',
    }

    return render(request, 'item/form.html', context)


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        uploaded_images = request.FILES.getlist('images')
        if form.is_valid():
            item = form.save()
            ItemImage.objects.all().filter(item=item).delete()
            for i in uploaded_images:
                ItemImage(item=item, images=i).save()
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    context = {
        'form': form,
        'title': 'Edit item',
    }

    return render(request, 'item/form.html', context)


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')
