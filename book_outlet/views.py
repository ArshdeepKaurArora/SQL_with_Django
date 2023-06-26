from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Max, Min

from .models import Book

# Create your views here.

def index(request):
    """returns the homepage with the collection of all books"""
    books = Book.objects.all().order_by("-title")
    total_books = books.count()
    average_rank = books.aggregate(Avg("ranking"))
    return render(request,"book_outlet/index.html",{
        'books': books,
        "total_books": total_books,
        'average_rank': average_rank,
    })

def book_detail(request,slug):
    """Return the details of book"""
    book = get_object_or_404(Book, slug=slug)
    return render(request,"book_outlet/book_detail.html",{
        'book': book,
    })