CREATE TABLE public.alkadienes (
    name TEXT PRIMARY KEY,
    formula TEXT NOT NULL,
    carbon_count INT NOT NULL CHECK (carbon_count > 0),
    hydrogen_count INT NOT NULL CHECK (hydrogen_count > 0),
    molar_mass INT NOT NULL CHECK (molar_mass > 0)
);

INSERT INTO public.alkadienes (name, formula, carbon_count, hydrogen_count, molar_mass)
VALUES
    ('Пропадиен', 'C3H4', 3, 4, 40),
    ('Бута-1,3-диен', 'C4H6', 4, 6, 54),
    ('Пента-1,3-диен', 'C5H8', 5, 8, 68),
    ('Гекса-1,3-диен', 'C6H10', 6, 10, 82),
    ('Гепта-1,3-диен', 'C7H12', 7, 12, 96);