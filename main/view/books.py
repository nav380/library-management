from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from main.models import Book
from django.utils.dateparse import parse_date
from main.serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/admin.html', {'books': books})

@api_view(['GET'])
def api_book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

def add_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST.get('title'),
            author=request.POST.get('author'),
            isbn=request.POST.get('isbn'),
            publication_date=parse_date(request.POST.get('publication_date')),
            pages=request.POST.get('pages'),
            language=request.POST.get('language'),
            publisher=request.POST.get('publisher'),
            serial_number=request.POST.get('serial_number'),
            numberofcopies=request.POST.get('numberofcopies'),
            available_copies=request.POST.get('available_copies')
        )
        return redirect('books')
    books = Book.objects.all()
    return render(request, 'books/admin.html',{'books': books})

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.isbn = request.POST.get('isbn')
        book.publication_date = parse_date(request.POST.get('publication_date'))
        book.pages = request.POST.get('pages')
        book.language = request.POST.get('language')
        book.publisher = request.POST.get('publisher')
        book.serial_number = request.POST.get('serial_number')
        book.numberofcopies = request.POST.get('numberofcopies')
        book.available_copies = request.POST.get('available_copies')
        book.save()
        return redirect('books')
    books = Book.objects.all()
    return render(request, 'books/admin.html', {'books': books , 'book': book})
