from django.shortcuts import render,redirect

from main.models import issues,Book

def borrow_record(request):
    if request.method == 'GET':
        books = Book.objects.all()
        return render(request, 'borrow/recordadmin.html', {'books': books})
 