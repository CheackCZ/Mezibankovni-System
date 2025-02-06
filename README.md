# Mezibankovní systém

## Obsah
- [Mezibankovní systém](#mezibankovní-systém)
  - [Obsah](#obsah)
  - [Úvod](#úvod)
  - [Architektura](#architektura)
  - [Funkcionalita](#funkcionalita)
  - [Struktura projektu](#struktura-projektu)
  - [Instalace](#instalace)
    - [Stažení projektu](#stažení-projektu)
  - [Spuštění aplikace](#spuštění-aplikace)
  - [Deployment a odevzdání](#deployment-a-odevzdání)
  - [Zdroje](#zdroje)
    - [Autor](#autor)


## Úvod
Projekt implementuje **P2P mezibankovní systém**, kde každý **uzel** v síti **představuje banku**. Každý uzel umožňuje *vytváření účtů*, *vkládání* a *výběr peněz* a *komunikaci s ostatními bankami* v síti prostřednictvím **TCP/IP protokolu**. Jedná se o **síťový protokol**, který **umožňuje decentralizovanou výměnu dat mezi bankami**.

Projekt zahrnuje asynchronní serverovou architekturu, správu bankovních účtů v databázi a komunikaci prostřednictvím textových příkazů v UTF-8.


## Architektura
- ```app.py``` – Hlavní **spouštěcí soubor**, inicializuje Node.
- ```node.py``` – Implementace uzlu (Node), který **naslouchá příkazům a spravuje klientská spojení**.
- ```command_controller.py``` – **Zpracovává příkazy** (BC, AC, AD, AW atd.).
- ```bank_controller.py``` – Spravuje **bankovní operace**.
- ```account_controller.py``` – **Spravuje jednotlivé účty**.
- ```config.py``` – Načítání konfigurace z ```.env```.
- ```logger.py``` – Správa **logování**.
- ```connection.py``` – Připojení k databázi pomocí ```SQLAlchemy```.


## Funkcionalita
- Bankovní protokol implementuje následující bankovní operace:
  - ```BC``` (Bank Code) – Vrací **IP adresu banky**.
  - ```AC``` (Account Create) – Vytvoří **nový bankovní účet**.
  - ```AD``` (Account Deposit) – **Vklad** na účet.
  - ```AW``` (Account Withdrawal) – **Výběr** peněz z účtu.
  - ```AB``` (Account Balance) – Získání **zůstatku** na účtu.
  - ```AR``` (Account Remove) – **Smazání účtu**, pokud je zůstatek 0.
  - ```BA``` (Bank Amount) – **Celková částka** v bance.
  - ```BN``` (Bank Number of Clients) – **Počet účtů** v bance.


## Struktura projektu
```
.
├── /db                    # Soubory související s databází
│   ├── setup.sql             # SQL skript pro vytvoření databáze
│   ├── connection.py         # Správa připojení k databázi
│
├── /logs                  # Logovací soubory
│   └── debug.log             # Soubor s logy
│
├── /src                   # Zdrojový kód
|   ├── /commands             # Implementace jednotlivých příkazů
|   ├── /controllers          # Řízení bankovní logiky
|   ├── /models               # Datové modely pro SQLAlchemy
|   ├── /p2p                  # P2P komunikační modul
│   ├── config.py             # Načítání konfigurace
│   └── logger.py             # Logování
│
├── app.py                    # Spuštění serveru
├── README.md                 # Dokumentace
├── .env                      # Konfigurace
├── .env.example              # Struktura jak by měl vypadat .env soubor
└── requirements.txt          # Seznam závislostí
```

## Instalace
### Stažení projektu
1. Projekt lze stáhnout buď jako .zip archiv, nebo pomocí GitHub repozitáře.
   - Stažení jako ZIP
     - Stáhni soubor ```Mezibankovni-System.zip``` a rozbal jej.
     - Přejdi do složky projektu.
 
   - Naklonování repozitáře
        ```
        git clone https://github.com/CheackCZ/Mezibankovni-System.git
        cd Mezibankovni-System
        ```

2. Instalace závislostí
    ```
    pip install -r requirements.txt
    ```

3. Konfigurace ```.env``` souboru
    ```
    # Konfigurace databáze
    DB_HOST=
    DB_USER=
    DB_PASSWORD=
    DB_NAME=
    DB_PORT=

    # Konfigurace socketu
    HOST=
    PORT=

    # Konfigurace formátování zpráv
    FORMAT=

    # Konfigurace levelu logování
    LOG_LEVEL=

    # Konfigurace timeoutu
    TIMEOUT=30
    ```

4. Importujte databázi do MySQL pomocí setup.sql:
    ```
    mysql -u [uživatel] -p [název_databáze] < db/setup.sql
    ```

## Spuštění aplikace
1. Spusťte aplikaci (v hlavní složce):
    ```
    python app.py
    ```

2. Připojte se na ```app.py``` s použitím konfiguračních dat socketu z ```.env``` souboru.

## Deployment a odevzdání
- Projekt je odevzdán jako .zip archiv obsahující zdrojový kód, testy a dokumentaci. Zajištěna kompatibilita se školním PC (Windows/Linux).
- Lze stáhnout přes GitHub repozitář pro lepší přístupnost.

## Zdroje
[Logging v Pythonu – logování v Pythonu](https://www.geeksforgeeks.org/logging-in-python/)<br>
[SQLAlchemy úvod a instalace – Práce s ORM v Pythonu](https://www.itnetwork.cz/python/sqlalchemy/sqlalchemy-uvod-a-instalace)<br>
[ChatGPT: Deklarativní modely v SQLAlchemy – Vytváření tabulek pomocí ORM](https://chatgpt.com/c/6798c30b-756c-800b-b2a8-fdd371fdf18a)<br>
[Base table v SQLAlchemy](https://docs.sqlalchemy.org/en/14/orm/declarative_tables.html)<br>
[Node for P2P in Python](https://blog.devgenius.io/implementing-peer-to-peer-data-exchange-in-python-8e69513489af)<br>
[Listen() method parameters in Python](https://stackoverflow.com/questions/48244322/listen-method-parameters-in-python)<br>
[Binding and Listening in Python](https://www.geeksforgeeks.org/python-binding-and-listening-with-sockets/)<br>
[Rozdíl mezi Process.start() a Process.run()](https://stackoverflow.com/questions/55084433/difference-between-process-run-and-process-start)<br>
[Co jsou signály a jak s nimi pracovat v pythonu?](https://www.askpython.com/python-modules/python-signal)<br>
[Python: frame parameter of signal handler](https://stackoverflow.com/questions/18704862/python-frame-parameter-of-signal-handler)<br>
[ChatGPT: Generování pydoc dokumantace](https://chatgpt.com/c/67a51035-43bc-800b-9951-048a23a61ec5)<br>
...

### Autor
**Ondřej Faltin**
*Student, SPŠE Ječná, třída C4A*
✉️ Email: ondra.faltin@gmail.com / faltin@spsejecna.cz