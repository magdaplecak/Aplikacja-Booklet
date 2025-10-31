# Instrukcja uruchomienia projektu BOOKLET z pliku ZIP w PyCharm

# Opis aplikacji Booklet

Aplikacja **Booklet** pozwala na zarządzanie swoimi książkami w trzech kategoriach: przeczytane, w trakcie czytania oraz książki, które chcemy przeczytać. Główne funkcjonalności aplikacji obejmują:

- **Lista książek**: Można dodać książki do swojej listy, klikając zakładkę „Dodaj książkę”.
- **Recenzje**: Dla książek przeczytanych oraz tych w trakcie czytania, użytkownik ma możliwość dodania recenzji, które są dostępne w zakładce „Recenzje”.

Aplikacja została zaprojektowana na podstawie moich personalnych preferencji dotyczących książek. Interfejs został stworzony w **Canvie**, aby zapewnić estetyczny i przyjazny dla użytkownika wygląd.

## 0. Przed uruchomieniem


Proszę pobrać plik ZIP z e-mail na komputer. Następnie proszę postępować zgodnie z poniższymi krokami:

## 1. Pobranie pliku ZIP
Proszę pobrać plik ZIP z repozytorium na komputer.

## 2. Rozpakowanie pliku ZIP
Po pobraniu pliku ZIP, proszę o rozpakowanie zawartości.

## 3. Otworzenie projektu w PyCharm
- Proszę otworzyć PyCharm.
- Następnie należy wybrać opcję „Open” (Otwórz) i wskazać folder, w którym został rozpakowany plik ZIP z projektem.

## 4. Utworzenie wirtualnego środowiska
Proszę otworzyć terminal w PyCharm i przejść do katalogu z projektem: cd praca_podyplomowa
Następnie proszę utworzyć wirtualne środowisko:

python -m venv .venv


## 5. Aktywacja wirtualnego środowiska
- Na systemie **Windows** proszę aktywować środowisko za pomocą polecenia:

.venv\Scripts\activate


## 6. Instalacja zależności
Po aktywacji środowiska należy zainstalować wymagane zależności:

pip install -r requirements.txt


## 7. Migracje bazy danych
Proszę uruchomić migracje bazy danych, aby utworzyć odpowiednie tabele:

python manage.py migrate


## 8. Uruchomienie aplikacji
Na tym etapie można uruchomić aplikację lokalnie za pomocą komendy:

python manage.py runserver

## 9. Dostęp do aplikacji
Aplikacja będzie dostępna pod adresem:

http://127.0.0.1:8000/
