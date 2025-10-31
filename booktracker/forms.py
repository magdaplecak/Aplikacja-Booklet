from django import forms
from .models import Book, Review

# forma dodawania książki
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'status']  # Pola formularza
        labels = {
            'title': 'Tytuł',
            'author': 'Autor',
            'description': 'Opis',
            'status': 'Status',
        }

# forma dodawania recenzji
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rating']  # pola formularza
        labels = {
            'review_text': 'Treść recenzji',
            'rating': 'Ocena',
        }
        widgets = {
            'review_text': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Napisz swoją recenzję...'}),
            'rating': forms.Select(choices=[(i, str(i)) for i in range(1, 11)], attrs={
                'placeholder': 'Oceń od 1 do 10'
            })
        }
