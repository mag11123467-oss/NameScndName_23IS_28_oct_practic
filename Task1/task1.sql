CREATE TABLE public.alkanes (
    name TEXT PRIMARY KEY,
    formula TEXT NOT NULL,
    carbon_count INT NOT NULL CHECK (carbon_count > 0),
    hydrogen_count INT NOT NULL CHECK (hydrogen_count > 0),
    molar_mass INT NOT NULL CHECK (molar_mass > 0)
);

INSERT INTO public.alkanes (name, formula, carbon_count, hydrogen_count, molar_mass)
VALUES
    ('Метан', 'CH4', 1, 4, 16),
    ('Этан', 'C2H6', 2, 6, 30),
    ('Пропан', 'C3H8', 3, 8, 44),
    ('Бутан', 'C4H10', 4, 10, 58),
    ('Пентан', 'C5H12', 5, 12, 72);