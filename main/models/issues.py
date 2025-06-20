from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from .books import Book  # Update the import path if needed

def get_due_date():
    return timezone.now().date() + timedelta(days=30)

class Issue(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    returned=models.BooleanField(default=False)
    due_date = models.DateField(default=get_due_date)
    return_date = models.DateField(null=True, blank=True)

    def is_overdue(self):
        if self.return_date:
            return self.return_date > self.due_date
        return self.due_date < timezone.now().date()

    def __str__(self):
        return f"{self.book.title} issued to {self.user.username}"
