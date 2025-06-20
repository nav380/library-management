from django.urls import path
from . import views
from .view.books import book_list



urlpatterns = [
    path('', views.home, name='home'),
    path('books/', book_list, name='books'),
    path('members/', views.member_list, name='members'),
    path('borrow/', views.borrow_book, name='borrow'),
    path('borrow-records/', views.borrow_records, name='borrow_records'),
    path('returns/', views.returns, name='returns'),
    
   
]
