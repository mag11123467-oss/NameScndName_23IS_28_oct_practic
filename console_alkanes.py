import psycopg

минимум = 7

with psycopg.connect(
    dbname="organic_chemistry",
    user="postgres",
    password="Admin",
    host="localhost",
    port=5432,
    connect_timeout=5
) as соединение:
    with соединение.cursor() as курсор:
        курсор.execute("""
            SELECT name, formula, carbon_count
            FROM public.alkanes
            WHERE carbon_count >= %s
            ORDER BY carbon_count ASC
        """, (минимум,))
        алканы = курсор.fetchall()

for алкан in алканы:
    название = алкан[0]
    формула = алкан[1]
    число_атомов = алкан[2]
    print(название, формула, число_атомов)