# Instrukcja uruchomienia aplikacji BOOKLET w Pycharm

# Opis aplikacji Booklet

Aplikacja **Booklet** pozwala na zarządzanie swoimi książkami w trzech kategoriach: przeczytane, w trakcie czytania oraz książki, które chcemy przeczytać. Główne funkcjonalności aplikacji obejmują:

- **Lista książek**: Można dodać książki do swojej listy, klikając zakładkę „Dodaj książkę”.
- **Recenzje**: Dla książek przeczytanych oraz tych w trakcie czytania, użytkownik ma możliwość dodania recenzji, które są dostępne w zakładce „Recenzje”.

Aplikacja została zaprojektowana na podstawie moich personalnych preferencji dotyczących książek. Interfejs został stworzony w **Canvie**, aby zapewnić estetyczny i przyjazny dla użytkownika wygląd.

# Wymagania
Aby uruchomić aplikację lokalnie, musisz mieć zainstalowane następujące oprogramowanie:

- Python (w wersji 3.7 lub wyższej)
- Django (w wersji 5.2 lub wyższej)
- SQLite (baza danych używana w tej aplikacji, domyślnie dostępna w Pythonie)
# Instrukcja uruchomienia aplikacji

Aby uruchomić aplikację, postępuj zgodnie z poniższymi krokami:

## 1. Klonowanie repozytorium

Sklonuj repozytorium na swój komputer za pomocą poniższego polecenia:

git clone https://github.com/magdaplecak/Aplikacja-Booklet.git

## 2. Przejście do folderu z aplikacją

Przejdź do folderu z aplikacją:

cd Aplikacja-Booklet

## 3. Utworzenie wirtualnego środowiska

Stwórz wirtualne środowisko Pythona, które będzie zawierać wszystkie wymagane zależności:

python -m venv .venv

lub 

python3 -m venv .venv **na MacOS**


## 4. Aktywacja wirtualnego środowiska
Aby aktywować wirtualne środowisko, użyj odpowiedniego polecenia w zależności od systemu operacyjnego:

**Na systemie Linux/macOS:**

source .venv/bin/activate


**Na systemie Windows:**

.venv\Scripts\activate

## 5. Instalacja zależności
Zainstaluj wszystkie wymagane pakiety z pliku requirements.txt:

pip install -r requirements.txt


## 6. Uruchomienie aplikacji
Aby uruchomić serwer aplikacji, użyj poniższego polecenia:

python manage.py runserver

## 7. Dostęp do aplikacji
Aplikacja będzie dostępna pod adresem:

http://127.0.0.1:8000/
