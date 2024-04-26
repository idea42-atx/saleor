from django.urls import path

from .views import collection_home, collection_list, category_home, category_list

urlpatterns = [
    path("collections/", collection_home, name="collection_home"),
    path("collection_list/", collection_list, name="collection_list"),
    path("categories/", category_home, name="category_home"),
    path("category_list/", category_list, name="category_list"),
]
