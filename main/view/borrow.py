from django.shortcuts import render,redirect

from main.models import issues,Book

def borrow(request):
    if request.method == 'GET':
        books = Book.objects.all()
        return render(request, 'borrow/admin.html', {'books': books})
    if request.method == 'POST':
        book=request.POST.get('book')
        user=request.user
        issues.object.create(book=book,user=user)
        return redirect('borrow')