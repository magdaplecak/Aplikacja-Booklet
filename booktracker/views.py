from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm, ReviewForm
from .models import Book, Review

# widok listy książek
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})





# widok dodawania książki
def add_book(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect('book_list')
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


# widok który pokazuje wszystkie książki z ich recenzjami
def book_reviews(request):

    books = Book.objects.all()
    return render(request, 'books/book_reviews.html', {'books': books})