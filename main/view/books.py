from django.shortcuts import render,redirect

def home(request):
    try:
        if request.user.is_authenticated:
            if request.user.is_staff:
                return render(request, 'home/adminhome.html')
            elif request.user.is_customer:
                return render(request, 'home/home.html')
        else:
            return render(request, 'error.html', {'error': 'User is not authenticated'})
    except Exception as e:
        print(f"Error: {e}")
        
        return redirect('login')


# library/views.py
from django.shortcuts import render, redirect, get_object_or_404
from main.models import Book
from django.utils.dateparse import parse_date

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/admin.html', {'books': books})

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
    return render(request, 'library/add_book.html')

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
    return render(request, 'library/edit_book.html', {'book': book})
