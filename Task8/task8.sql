CREATE TABLE public.sports (
    name TEXT PRIMARY KEY,
    sport TEXT NOT NULL,
    participants INT NOT NULL CHECK (participants > 0),
    sessions INT NOT NULL CHECK (sessions > 0),
    fee INT NOT NULL CHECK (fee > 0)
);

INSERT INTO public.sports (name, sport, participants, sessions, fee)
VALUES
    ('Старт', 'Плавание', 12, 2, 2500),
    ('Волна', 'Плавание', 16, 3, 3500),
    ('Темп', 'Бег', 10, 3, 1800),
    ('Пас', 'Футбол', 20, 2, 2200),
    ('Ритм', 'Гимнастика', 14, 4, 4000);