from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Category, Item

def home(request):
    categories = Category.objects.all()
    items = Item.objects.all()
    return render(request, 'index.html', {'categories': categories, 'items': items})

def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        messages.success(request, f'Категорія "{category.name}"видалена')
        return redirect('blog:home')
    return redirect('blog:home')

def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    items = Item.objects.filter(category=category)
    return render(request, 'blog/category.html', {'category': category, 'items': items})

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'item_detail.html', {'item': item})

def create_item(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        new_category = request.POST.get('new_category')

        if new_category:
            category, created = Category.objects.get_or_create(name=new_category)
        elif category_id:
            try:
                category = Category.objects.get(id=int(category_id))
            except (Category.DoesNotExist, ValueError):
                messages.error(request, 'Невірний вибір')
                return render(request, 'create_item.html', {'categories': categories})
        else:
            messages.error(request, 'Оберіть категорію!')
            return render(request, 'create_item.html', {'categories': categories})

        try:
            price = float(price)
        except ValueError:
            messages.error(request, 'Ціна має бути числом!')
            return render(request, 'create_item.html', {'categories': categories})

        item = Item(title=title, description=description, price=price, category=category)
        item.save()
        messages.success(request, 'Товар створений!')
        return redirect('blog:home')

    return render(request, 'create_item.html', {'categories': categories})

def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.delete()
        messages.success(request, f'Товар "{item.title}" видалений!')
        return redirect('blog:home')
    return redirect('blog:home')
