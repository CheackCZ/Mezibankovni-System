-- Vytvoření databáze
create database interbanking_db;

use interbanking_db;

-- Vytvoření admin uživatele pro správu databáze
create user 'admin'@'localhost' identified by 'admin';

-- Vyhrazení všech práv administrátorovi
grant all privileges on Service.* to 'admin'@'localhost';
flush privileges;


-- Vytvoření tabulky account
create table account (
    account_number int primary key auto_increment=10000,
        check (account_number >= 10000 and <= 99999),
    balance float not null,
        check (balance >= 0)
);

-- Vložení dat do tabulky account
insert into account (balance) values (1000);
insert into account (balance) values (2000);
insert into account (balance) values (3000);