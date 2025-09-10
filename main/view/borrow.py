from django.shortcuts import render,redirect

from main.models import Issue,Book
from accounts.models import User

def borrow(request):
    if request.method == 'GET':
        books = Book.objects.filter(available_copies__gt=0)
        members = User.objects.all()
        return render(request, 'borrow/admin.html', {'books': books ,'members': members})
    if request.method == 'POST':
        bookid=request.POST.get('book')
        user=request.user
        book=Book.objects.get(id=bookid)
        book.available_copies-=1
        book.save()
        Issue.objects.create(book=book,user=user)
        return redirect('borrow_records')