CREATE TABLE public.alcohols (
    name TEXT PRIMARY KEY,
    formula TEXT NOT NULL,
    carbon_count INT NOT NULL CHECK (carbon_count > 0),
    hydrogen_count INT NOT NULL CHECK (hydrogen_count > 0),
    molar_mass INT NOT NULL CHECK (molar_mass > 0)
);

INSERT INTO public.alcohols (name, formula, carbon_count, hydrogen_count, molar_mass)
VALUES
    ('Метанол', 'CH4O', 1, 4, 32),
    ('Этанол', 'C2H6O', 2, 6, 46),
    ('Пропан-1-ол', 'C3H8O', 3, 8, 60),
    ('Бутан-1-ол', 'C4H10O', 4, 10, 74),
    ('Пентан-1-ол', 'C5H12O', 5, 12, 88);