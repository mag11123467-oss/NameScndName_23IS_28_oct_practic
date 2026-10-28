CREATE TABLE public.stationery (
    name TEXT PRIMARY KEY,
    category TEXT NOT NULL,
    price INT NOT NULL CHECK (price > 0),
    quantity INT NOT NULL CHECK (quantity >= 0),
    reorder_level INT NOT NULL CHECK (reorder_level >= 0)
);

INSERT INTO public.stationery (name, category, price, quantity, reorder_level)
VALUES
    ('Тетрадь', 'Бумага', 60, 25, 10),
    ('Блокнот', 'Бумага', 180, 8, 10),
    ('Ручка', 'Письмо', 40, 50, 20),
    ('Маркер', 'Письмо', 120, 5, 10),
    ('Папка', 'Хранение', 150, 12, 5);