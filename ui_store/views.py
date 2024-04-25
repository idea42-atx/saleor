from django.shortcuts import render
from django.views.decorators.http import require_http_methods


def search(request):
    return render(request, "ui_store/search.html.jinja2", {"todos": []})
