from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Page

def index(request):
    pages = Page.objects.all()
    return render(request, 'wiki/index.html', {'pages': pages})

def page(request, title):
    page = get_object_or_404(Page, title=title)
    return render(request, 'wiki/page.html', {'page': page})

def edit_page(request, title):
    page = get_object_or_404(Page, title=title)
    return render(request, 'wiki/edit_page.html', {'page': page})

def save_page(request, title):
    page = get_object_or_404(Page, title=title)
    if request.method == 'POST':
        content = request.POST.get('content', '')
        page.content = content
        page.save()
        return redirect('page', title=title)
    return redirect('edit_page', title=title)
