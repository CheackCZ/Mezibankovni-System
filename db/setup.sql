-- Vytvoření databáze
create database interbanking_db;

use interbanking_db;

-- Vytvoření admin uživatele pro správu databáze
-- create user 'admin'@'localhost' identified by 'admin_password';

-- Vyhrazení všech práv administrátorovi
-- grant all privileges on interbanking_db.* to 'admin'@'localhost';
-- flush privileges;

-- Vytvoření tabulky account
create table account (
    account_number int primary key auto_increment,
    balance float not null,
        check (balance >= 0)
) auto_increment = 10000;

-- Výpis všeho z tabulky account pro otestování dat v databázi
-- select * from account;