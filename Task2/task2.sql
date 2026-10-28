CREATE TABLE public.alkenes (
    name TEXT PRIMARY KEY,
    formula TEXT NOT NULL,
    carbon_count INT NOT NULL CHECK (carbon_count > 0),
    hydrogen_count INT NOT NULL CHECK (hydrogen_count > 0),
    molar_mass INT NOT NULL CHECK (molar_mass > 0)
);

INSERT INTO public.alkenes (name, formula, carbon_count, hydrogen_count, molar_mass)
VALUES
    ('Этен', 'C2H4', 2, 4, 28),
    ('Пропен', 'C3H6', 3, 6, 42),
    ('Бут-1-ен', 'C4H8', 4, 8, 56),
    ('Пент-1-ен', 'C5H10', 5, 10, 70),
    ('Гекс-1-ен', 'C6H12', 6, 12, 84);