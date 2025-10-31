from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm, ReviewForm
from .models import Book, Review
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.shortcuts import redirect


def home(request):
    return render(request, 'home.html')

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

#rejestracja uzytkownika
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print("Formularz zawiera błędy:")
            print(form.errors)
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


#autentykacja uzytkownikow

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# wylogowywanie uzytkownika
def logout_view(request):
    logout(request)
    return redirect('home')  # or 'login'