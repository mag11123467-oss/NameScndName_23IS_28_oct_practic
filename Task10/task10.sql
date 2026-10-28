CREATE TABLE public.computers (
    name TEXT PRIMARY KEY,
    category TEXT NOT NULL,
    ram_gb INT NOT NULL CHECK (ram_gb > 0),
    storage_gb INT NOT NULL CHECK (storage_gb > 0),
    quantity INT NOT NULL CHECK (quantity >= 0)
);

INSERT INTO public.computers (name, category, ram_gb, storage_gb, quantity)
VALUES
    ('Учебный-1', 'ПК', 8, 256, 12),
    ('Учебный-2', 'ПК', 16, 512, 8),
    ('Мобильный-1', 'Ноутбук', 8, 512, 5),
    ('Мобильный-2', 'Ноутбук', 16, 1024, 3),
    ('Сервер-1', 'Сервер', 32, 2048, 1);