from django.urls import path
from . import views
from .view.books import book_list, add_book, edit_book
from .view.home import home
from .view.members import member_list, add_member, edit_member



urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('add-book/', add_book, name='add_book'),
    path('edit-book/<int:book_id>/', edit_book, name='edit_book'),
    path('members/', member_list, name='members'),
    path('add-member/', add_member, name='add_member'),
    path('edit-member/<int:user_id>/', edit_member, name='edit_member'),
    path('borrow/', views.borrow_book, name='borrow'),
    path('borrow-records/', views.borrow_records, name='borrow_records'),
    path('returns/', views.returns, name='returns'),
    
   
]
