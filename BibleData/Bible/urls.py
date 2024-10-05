from django.urls import path

from Bible.views import BookCreateView, BookListView, BookHomeView, BookUpdateView

urlpatterns = [
    path('', BookHomeView.as_view(), name='book_home'),
    path('create/', BookCreateView.as_view(), name='create'),
    path('list/', BookListView.as_view(), name='book_list'),
    path('<str:pk>/update/', BookUpdateView.as_view(), name='book_update'),
]
