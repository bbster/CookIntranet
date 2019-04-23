CREATE USER admin WITH PASSWORD 'dlwlehd12';
ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE admin SET TIMEZONE TO 'Asia/Seoul';

ALTER ROLE admin WITH SUPERUSER;

CREATE DATABASE cookintranet;
