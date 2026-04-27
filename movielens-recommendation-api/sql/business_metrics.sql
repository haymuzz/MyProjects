-- Дополнительная схема БД для проекта: MovieLens Recommendation API

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY
);

CREATE TABLE items (
    item_id INTEGER PRIMARY KEY,
    title TEXT,
    category TEXT
);

CREATE TABLE interactions (
    user_id INTEGER,
    item_id INTEGER,
    rating REAL,
    event_ts TIMESTAMP,
    PRIMARY KEY (user_id, item_id)
);
