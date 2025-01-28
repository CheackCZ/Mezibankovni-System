-- Vytvoření databáze
create database interbanking_db;

use interbanking_db;

-- Vytvoření admin uživatele pro správu databáze
-- create user 'admin'@'localhost' identified by 'admin';

-- Vyhrazení všech práv administrátorovi
grant all privileges on interbanking_db.* to 'admin'@'localhost';
flush privileges;


-- Vytvoření tabulky account
create table account (
    account_number int primary key auto_increment,
    balance float not null,
        check (balance >= 0)
) auto_increment = 10000;

select * from account;

-- Vložení dat do tabulky account
insert into account (balance) values (1000);
insert into account (balance) values (2000);
insert into account (balance) values (3000);