# Cook-Helper 

### Opis projektu:<br/>
Pomysł polega na stworzeniu botu do jednego z messenger'ów, w naszym projekcie to jest "Telegram Messenger" https://telegram.org/, który na podstawie zdjęcia dania podanego przez użytkownika proponuje wideo tutorial przygotowania takiego dania.

link do podłączenia bot'a: http://t.me/help_me_to_cook_bot 

![Cook_Helper](https://github.com/VladPodlesnyi/Cook-Helper/blob/09442c9ac8f26a4e49d8fcf1407595729c5952fb/Cook_Helper.png)

### Architektura
* Custom Vision<br/>
Na podstawie dataset'u o większości ponad 101 000 zdjęć został wytrenerowany model, dzięki któremu i wyznaczamy jakie danie jest na zdęciu.
* Azure Blob Storage<br/>
Używając poniższy serwis przechowujemy zdjęcia, które ładują użytkownicy, w przyszłości możemy używać ich, jako dodatkowe elementy datasetu.
* Azure Storage Account<br/>
Powyższy serwis używamy dla stworzenia tablicy z linków przepisów dań i linków z tutorial'em do przygotowania (linki dostajemy parsing'em)
* Azure Web App


### Funkcjonalność:
Aplikacja działa w następujący sposób: użytkownik przesyła lub robi zdjęcie za pomocą bota "Cook-Helper", który działa na stronie azure webapp. To zdjęcie jest zapisywane w serwisie blob_storadge, a następnie wysyłane wraz z funkcją przewidywania dań do naszego wyszkolonego modelu custom_vision, skąd zwracany jest wynik - nazwa dania. Według którego poszukujemy w tabeli storadge_account linku do filmiku na YouTube z przepisem, w końcu bot wysyła wideo do naszego użytkownika w odpowiedzi na początkowe zdjęcie.


### Stos technologiczny:
* Telegramm API
* Azure SDK For Python


### Skład zespołu:
* Kharashun Ilya https://github.com/Mr-Cronk
* Khameta Maksim https://github.com/khametamaksim
* Podlesnyi Vladyslav https://github.com/VladPodlesnyi
* Selivoniets Aliaksiei https://github.com/alselivonets
