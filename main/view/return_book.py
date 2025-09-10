from django.shortcuts import render,redirect
from django.utils import timezone

from main.models import Issue,Book
from accounts.models import User

def return_book(request):
    if request.method == 'GET':
        Issues=Issue.objects.filter(return_date__isnull=True)
        return render(request,'return_book/admin.html',{'issues':Issues})
    if request.method == 'POST':
        issueid=request.POST.get('issueid')
        issue=Issue.objects.get(id=issueid)
        issue.return_date=timezone.now()
        issue.save()
        book=issue.book
        book.available_copies+=1
        book.save()
        return redirect('return_book')
        