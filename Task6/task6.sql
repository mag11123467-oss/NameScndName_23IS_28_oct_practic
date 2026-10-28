CREATE TABLE public.books (
    title TEXT PRIMARY KEY,
    author TEXT NOT NULL,
    publication_year INT NOT NULL CHECK (publication_year > 0),
    pages INT NOT NULL CHECK (pages > 0),
    copies INT NOT NULL CHECK (copies >= 0)
);

INSERT INTO public.books (title, author, publication_year, pages, copies)
VALUES
    ('Путь к звёздам', 'Анна Мирова', 2018, 180, 3),
    ('Лесные истории', 'Иван Ветров', 2020, 240, 5),
    ('Мир роботов', 'Ольга Север', 2021, 320, 2),
    ('Тайна острова', 'Павел Лисов', 2022, 280, 4),
    ('Город будущего', 'Мария Луч', 2024, 400, 1);