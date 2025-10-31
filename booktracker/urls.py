from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # lista książek
    path('add/', views.add_book, name='add_book'),  # dod. książki
    path('add_review/<int:book_id>/', views.add_review, name='add_review'),
    path('reviews/', views.book_reviews, name='book_reviews'),  # str z recenzjami

]
