CREATE TABLE public.board_games (
    name TEXT PRIMARY KEY,
    genre TEXT NOT NULL,
    players INT NOT NULL CHECK (players > 0),
    duration INT NOT NULL CHECK (duration > 0),
    min_age INT NOT NULL CHECK (min_age > 0)
);

INSERT INTO public.board_games (name, genre, players, duration, min_age)
VALUES
    ('Остров', 'Стратегия', 4, 60, 10),
    ('Маршрут', 'Приключения', 3, 45, 8),
    ('Слова', 'Викторина', 6, 30, 12),
    ('Башня', 'Ловкость', 2, 15, 6),
    ('Космос', 'Стратегия', 5, 90, 14);