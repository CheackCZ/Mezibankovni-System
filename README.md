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
  - [Testování](#testování)
  - [Deployment a odevzdání](#deployment-a-odevzdání)
  - [Zdroje](#zdroje)
    - [Autor](#autor)


## Úvod
Projekt implementuje **P2P mezibankovní systém**, kde každý **uzel** v síti **představuje banku**. Jednotlivé uzly spolu komunikují prostřednictvím **bankovního protokolu**, který umožňuje *vytváření účtů*, *vkládání* a *výběr peněz* a *komunikaci s ostatními bankami* v síti prostřednictvím **TCP/IP protokolu** díky kterému je možná decentralizovaná **výměna dat mezi bankami**.


## Architektura
- ```app.py``` – Hlavní **spouštěcí soubor**, inicializuje Node.

- ```node.py``` – Implementace uzlu (Node), který **naslouchá příkazům a spravuje klientská spojení**.
- ```proxy.py``` – **Přesměrovává požadavky mezi bankami** při použití proxy příkazů (AD, AW, AB).

- ```command_controller.py``` – **Zpracovává příkazy** (BC, AC, AD, AW atd.).
- ```bank_controller.py``` – Spravuje **bankovní operace**.
- ```account_controller.py``` – **Spravuje jednotlivé účty**.

- ```config.py``` – Načítání konfigurace z ```.env```.

- ```logger.py``` – Správa **logování**.

- ```connection.py``` – Připojení k databázi pomocí ```SQLAlchemy```.


## Funkcionalita
- Bankovní protokol implementuje následující bankovní operace:
  - ```BC``` (Bank Code) – Vrací **IP adresu banky**.
  - ```BA``` (Bank Amount) – **Celková částka** v bance.
  - ```BN``` (Bank Number of Clients) – **Počet účtů** v bance.
  - ```AC``` (Account Create) – Vytvoří **nový bankovní účet**.
  - ```AD``` (Account Deposit) – **Vklad** na účet.
  - ```AW``` (Account Withdrawal) – **Výběr** peněz z účtu.
  - ```AB``` (Account Balance) – Získání **zůstatku** na účtu.
  - ```AR``` (Account Remove) – **Smazání účtu**, pokud je zůstatek 0.
  
**Proxy Funkcionalita**
- Příkazy ```AD```, ```AW``` a ```AB``` fungují jako proxy. Přijmou-li jinou IP adresu než svojí banky, **přesměrují příkaz na daný uzel**. 
- Umožňuje komunikaci mezi jednotlivými bankami (uzly) v P2P síti.


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
│   │    ├── ab.py                # Příkaz pro získání zůstatku účtu
│   │    ├── ac.py                # Příkaz pro vytvoření účtu
│   │    ├── ad.py                # Příkaz pro vklad na účet
│   │    ├── ar.py                # Příkaz pro odstranění účtu
│   │    ├── aw.py                # Příkaz pro výběr z účtu
│   │    ├── ba.py                # Příkaz pro získání celkové částky v bance
│   │    ├── bc.py                # Příkaz pro získání kódu banky (IP)
│   │    └── bn.py                # Příkaz pro počet účtů v bance
│   │ 
│   ├── /controllers          # Řízení bankovní logiky
│   │   ├── account_controller.py  # Správa účtů
│   │   ├── bank_controller.py     # Správa banky
│   │   └── command_controller.py  # Správa příkazů
│   │ 
│   ├── /models               # Datové modely pro SQLAlchemy
│   │   ├── account.py          # Model bankovního účtu
│   │   └── base.py             # Deklarativní základ pro SQLAlchemy
│   
│   ├── /p2p                  # P2P komunikační modul
│   │   ├── node.py             # Implementace P2P uzlu
│   │   └── proxy.py            # Proxy vrstva pro komunikaci mezi bankami
│
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
    - Pokud se Vám nebude dařit závislosti stáhnout, zkuste je stáhnout sami (bez využití souboru requirements.txt):
    ```
    pip install python-dotenv sqlalchemy mysql-connector-python
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
    TIMEOUT=

    # Konfigurace timeoutu pro vyhedávání aktivních portů proxy
    PROXY_TIMEOUT=
    ```

4. Importujte databázi do MySQL pomocí ```setup.sql```:
    ```
    mysql -u [uživatel] -p [název_databáze] < db/setup.sql
    ```
    - nebo spusťte v MySQL serveru:
    ```
    -- Vytvoření databáze
    create database interbanking_db;

    use interbanking_db;

    -- Vytvoření tabulky account
    create table account (
        account_number int primary key auto_increment,
        balance float not null,
            check (balance >= 0)
    ) auto_increment = 10000;
    ```

## Spuštění aplikace
1. Spusťte aplikaci (v hlavní složce):
    ```
    python app.py
    ```

2. Připojte se na ```app.py``` s použitím konfiguračních dat socketu z ```.env``` souboru, konkrétně ```HOST``` a ```PORT```, přes například PuTTy.

## Testování
- **Otestována databázová integrace** a **logování**.
- **Testování** se spolužáky navzájem:
  - **Funkčnosti programu** a **odchytávání chyb**.
  - **Funkčnosti proxy** příkazů mezi bankami.

Spolužáci se kterými jsem aplikaci testoval: *Saša Komínek (C4a)* a *Tomáš Kléger (C4a)* 

## Deployment a odevzdání
- Projekt je odevzdán jako .zip archiv obsahující zdrojový kód, testy a dokumentaci. Zajištěna kompatibilita se školním PC (Windows).
- Lze stáhnout přes **GitHub repozitář** pro lepší přístupnost: [link na github](https://github.com/CheackCZ/Mezibankovni-System).

- Vyžadovaná nejnižší verze *Python*u* 3.7*

## Zdroje
**python-dotenv**<br>
[Oficiální dokumentace dotenv knihovny](https://pypi.org/project/python-dotenv/)<br>

**python logging**<br>
[Logging v Pythonu – logování v Pythonu](https://www.geeksforgeeks.org/logging-in-python/)<br>

**python sqlalchemy**<br>
[SQLAlchemy úvod a instalace – Práce s ORM v Pythonu](https://www.itnetwork.cz/python/sqlalchemy/sqlalchemy-uvod-a-instalace)<br>
[Base table v SQLAlchemy](https://docs.sqlalchemy.org/en/14/orm/declarative_tables.html)<br>
[Engine v SQLAlchemy](https://docs.sqlalchemy.org/en/20/core/connections.html)<br>
[Session a Sessionmaker v pythonu](https://docs.sqlalchemy.org/en/20/orm/session_basics.html#using-a-sessionmaker)<br>

**python socket**<br>
[Node for P2P in Python](https://blog.devgenius.io/implementing-peer-to-peer-data-exchange-in-python-8e69513489af)<br>
[Rozdíl mezi Process.start() a Process.run()](https://stackoverflow.com/questions/55084433/difference-between-process-run-and-process-start)<br>

**python signal**<br>
[Co jsou signály a jak s nimi pracovat v pythonu?](https://www.askpython.com/python-modules/python-signal)<br>
[Python: frame parameter of signal handler](https://stackoverflow.com/questions/18704862/python-frame-parameter-of-signal-handler)<br>

**cariage return python**<br>
[Carriage return in python](https://supersourcing.com/blog/what-is-r-in-python-what-is-its-purpose/)<br>

**ChatGPT**<br>
[ChatGPT: MySQL Auto_INCREMENT od vyšší úrovně](https://chatgpt.com/c/6798c30b-756c-800b-b2a8-fdd371fdf18a)<br>
[ChatGPT: Generování pydoc dokumantace](https://chatgpt.com/c/67a51035-43bc-800b-9951-048a23a61ec5)<br>

**Kód z předchozích projektů**<br>
_Paralelní programování: JečnáBot_
- **Inspirace navržení síťového protokolu** (```node.py```) pomocí ```server.py``` a ```session.py``` tříd a jejich metod v tomto projektu.
- Použití metody ```handle_client()``` a ```_process_message()``` pro práci s připojeným nodem, v ```node.py/handle_client()```. 
  
_RDBMS: Car-Service_
- Použití stejné struktury: **model + controller** pro tabulky v databázi a práci s nimi. 
- Použití stejné metody **připojující se k databázi** pro kontrolu připojení, v ```config.py/_validate_db_connection()```. 
- Použití metod pro **validaci portu a hodnot z ```.env``` souboru**, v ```config.py```. 

**Použití kódu ze cvičení 16.*.**
...

### Autor
**Ondřej Faltin**<br>
*Student, SPŠE Ječná, třída C4A*<br>
✉️ Email: ondra.faltin@gmail.com / faltin@spsejecna.cz
