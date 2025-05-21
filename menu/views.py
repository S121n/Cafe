from django.shortcuts import render
from .models import Category


def menu_view(request):
    categories = Category.objects.prefetch_related('items').all()
    return render(request, 'menu.html', {'category': categories})
