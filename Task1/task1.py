import tkinter as tk
from tkinter import ttk
import psycopg

def очистить_таблицу():
    for строка in таблица.get_children():
        таблица.delete(строка)

def показать_данные():
    with psycopg.connect(
        dbname='alkanes_task1', user='postgres', password='Admin', host='localhost', port=5432
    ) as соединение:
        with соединение.cursor() as курсор:
            курсор.execute('SELECT name, formula, carbon_count, hydrogen_count, molar_mass FROM public.alkanes ORDER BY carbon_count ASC')
            данные = курсор.fetchall()

    очистить_таблицу()
    for строка in данные:
        таблица.insert('', tk.END, values=строка)

окно = tk.Tk()
окно.title('Алканы — Task 1')
окно.geometry('800x450')

ttk.Label(окно, text='Каталог: Алканы', font=('Arial', 14)).pack(pady=10)

фрейм_кнопок = ttk.Frame(окно)
фрейм_кнопок.pack(pady=5)
ttk.Button(фрейм_кнопок, text='Показать', command=показать_данные).pack(side=tk.LEFT, padx=10)
ttk.Button(фрейм_кнопок, text='Очистить таблицу', command=очистить_таблицу).pack(side=tk.LEFT, padx=10)

фрейм_таблицы = ttk.Frame(окно)
фрейм_таблицы.pack(padx=15, pady=10, fill=tk.X, expand=False)

# Таблица с height=3
таблица = ttk.Treeview(фрейм_таблицы, columns=('name', 'formula', 'carbon_count', 'hydrogen_count', 'molar_mass'), show='headings', height=3)

# Заголовки
таблица.heading('name', text='Название'); таблица.heading('formula', text='Формула'); таблица.heading('carbon_count', text='Атомов C'); таблица.heading('hydrogen_count', text='Атомов H'); таблица.heading('molar_mass', text='Масса, г/моль');

# Ширина
таблица.column('name', width=150, anchor='w'); таблица.column('formula', width=100, anchor='center'); таблица.column('carbon_count', width=90, anchor='center'); таблица.column('hydrogen_count', width=90, anchor='center'); таблица.column('molar_mass', width=120, anchor='center');

скролл = ttk.Scrollbar(фрейм_таблицы, orient='vertical', command=таблица.yview)
таблица.configure(yscrollcommand=скролл.set)

таблица.grid(row=0, column=0, sticky='nsew')
скролл.grid(row=0, column=1, sticky='ns')

окно.mainloop()
