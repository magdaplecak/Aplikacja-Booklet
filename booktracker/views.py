from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm, ReviewForm
from .models import Book, Review

# Widok listy książek
def book_list(request):
    books = Book.objects.all()  # Pobierz wszystkie książki
    return render(request, 'books/book_list.html', {'books': books})


# # Widok szczegółów książki z recenzjami
# def book_detail(request, book_id):
#     book = get_object_or_404(Book, id=book_id)  # Pobierz książkę po ID
#     reviews = book.reviews.all()  # Pobierz wszystkie recenzje dla tej książki
#     return render(request, 'books/book_detail.html', {'book': book, 'reviews': reviews})



# Widok dodawania książki
def add_book(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()  # Zapisz książkę
            return redirect('book_list')  # Po zapisaniu książki, przekierowanie do listy książek
    else:
        book_form = BookForm()

    return render(request, 'books/add_book.html', {'book_form': book_form})

# widok dodawania recenzji
def add_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return redirect('book_list')
    else:
        form = ReviewForm()
    return render(request, 'books/add_review.html', {'form': form, 'book': book})


# widok, który pokazuje wszystkie książki z ich recenzjami
def book_reviews(request):

    books = Book.objects.all()
    return render(request, 'books/book_reviews.html', {'books': books})