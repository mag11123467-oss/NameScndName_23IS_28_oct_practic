CREATE TABLE public.alkynes (
    name TEXT PRIMARY KEY,
    formula TEXT NOT NULL,
    carbon_count INT NOT NULL CHECK (carbon_count > 0),
    hydrogen_count INT NOT NULL CHECK (hydrogen_count > 0),
    molar_mass INT NOT NULL CHECK (molar_mass > 0)
);

INSERT INTO public.alkynes (name, formula, carbon_count, hydrogen_count, molar_mass)
VALUES
    ('Этин', 'C2H2', 2, 2, 26),
    ('Пропин', 'C3H4', 3, 4, 40),
    ('Бут-1-ин', 'C4H6', 4, 6, 54),
    ('Пент-1-ин', 'C5H8', 5, 8, 68),
    ('Гекс-1-ин', 'C6H10', 6, 10, 82);