DROP DATABASE IF EXISTS db_livinghome;
CREATE DATABASE db_livinghome;

\c db_livinghome;

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50),
    password VARCHAR(162)
);

CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(50),
    description TEXT,
    price INTEGER
);

CREATE TABLE IF NOT EXISTS images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_product INTEGER REFERENCES product(id),
    image_uri VARCHAR(25)
);

CREATE TABLE IF NOT EXISTS comment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_product INTEGER REFERENCES product(id),
    nama VARCHAR(50),
    comment TEXT
);

CREATE TABLE IF NOT EXISTS link (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_product INTEGER REFERENCES product(id),
    no_wa VARCHAR(13),
    web_link VARCHAR(25),
    fb_link VARCHAR(25),
    ig_link VARCHAR(25),
    web_click INTEGER,
    fb_click INTEGER,
    ig_click INTEGER,
    web_checkout INTEGER,
    fb_checkout INTEGER,
    ig_checkout INTEGER
);