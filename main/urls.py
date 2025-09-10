from django.urls import path
from .view.books import book_list, add_book, edit_book
from .view.home import home
from .view.members import member_list, add_member, edit_member
from .view.borrow import borrow 
from .view.borrow_records import borrow_record
from .view.return_book import return_book




urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('add-book/', add_book, name='add_book'),
    path('edit-book/<int:book_id>/', edit_book, name='edit_book'),
    path('members/', member_list, name='members'),
    path('add-member/', add_member, name='add_member'),
    path('edit-member/<int:user_id>/', edit_member, name='edit_member'),
    path('borrow/',borrow,name='borrow'),
    path('borrow-records/',borrow_record,name='borrow_records'),
    path('returns/',borrow,name='returns'),
    path('return-records/',return_book,name='return_book'),
    
 
    
   
]
