import tkinter as tk
from tkinter import ttk
import psycopg

def очистить_таблицу():
    for строка in таблица.get_children():
        таблица.delete(строка)

def показать_данные():
    with psycopg.connect(
        dbname='board_games_task9', user='postgres', password='Admin', host='localhost', port=5432
    ) as соединение:
        with соединение.cursor() as курсор:
            курсор.execute('SELECT name, genre, players, duration, min_age FROM public.board_games ORDER BY duration ASC, name ASC')
            данные = курсор.fetchall()

    очистить_таблицу()
    for строка in данные:
        таблица.insert('', tk.END, values=строка)

окно = tk.Tk()
окно.title('Настольные игры — Task 9')
окно.geometry('800x450')

ttk.Label(окно, text='Каталог: Настольные игры', font=('Arial', 14)).pack(pady=10)

фрейм_кнопок = ttk.Frame(окно)
фрейм_кнопок.pack(pady=5)
ttk.Button(фрейм_кнопок, text='Показать', command=показать_данные).pack(side=tk.LEFT, padx=10)
ttk.Button(фрейм_кнопок, text='Очистить таблицу', command=очистить_таблицу).pack(side=tk.LEFT, padx=10)

фрейм_таблицы = ttk.Frame(окно)
фрейм_таблицы.pack(padx=15, pady=10, fill=tk.X, expand=False)

# Таблица с height=3
таблица = ttk.Treeview(фрейм_таблицы, columns=('name', 'genre', 'players', 'duration', 'min_age'), show='headings', height=3)

# Заголовки
таблица.heading('name', text='Игра'); таблица.heading('genre', text='Жанр'); таблица.heading('players', text='Игроков'); таблица.heading('duration', text='Минут'); таблица.heading('min_age', text='Возраст, от');

# Ширина
таблица.column('name', width=150, anchor='w'); таблица.column('genre', width=150, anchor='w'); таблица.column('players', width=90, anchor='center'); таблица.column('duration', width=90, anchor='center'); таблица.column('min_age', width=100, anchor='center');

скролл = ttk.Scrollbar(фрейм_таблицы, orient='vertical', command=таблица.yview)
таблица.configure(yscrollcommand=скролл.set)

таблица.grid(row=0, column=0, sticky='nsew')
скролл.grid(row=0, column=1, sticky='ns')

окно.mainloop()
