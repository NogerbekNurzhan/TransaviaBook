from django.urls import path
from book.views import (
    BookListView,
    BookFilterView,
)


app_name = 'book'


urlpatterns = [
    path(
        'book/',
        BookListView.as_view(),
        name='book_list'
    ),
    path(
        'book/filter/',
        BookFilterView.as_view(),
        name='book_filter'
    ),
]
