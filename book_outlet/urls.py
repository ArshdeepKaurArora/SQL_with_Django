from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name='homepage'),
    path("<slug:slug>",views.book_detail,name='book_detail')
]
