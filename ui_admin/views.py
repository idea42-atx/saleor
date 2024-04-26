from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from saleor.product.models import Collection, Category


def collection_home(request):
    return render(
        request,
        "ui_admin/collection_home.html.jinja2",
    )


def collection_list(request):
    collections = Collection.objects.all()
    return render(
        request, "ui_admin/collection_listing.html.jinja2", {"collections": collections}
    )


def category_home(request):
    return render(
        request,
        "ui_admin/category_home.html.jinja2",
    )


def category_list(request):
    # get root categories
    categories = Category.objects.filter(parent=None)

    return render(
        request, "ui_admin/category_listing.html.jinja2", {"categories": categories}
    )
