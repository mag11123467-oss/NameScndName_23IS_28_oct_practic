import tkinter as tk
from tkinter import ttk
import psycopg

def очистить_таблицу():
    for строка in таблица.get_children():
        таблица.delete(строка)

def показать_данные():
    with psycopg.connect(
        dbname='stationery_task7', user='postgres', password='Admin', host='localhost', port=5432
    ) as соединение:
        with соединение.cursor() as курсор:
            курсор.execute('SELECT name, category, price, quantity, reorder_level FROM public.stationery ORDER BY price ASC, name ASC')
            данные = курсор.fetchall()

    очистить_таблицу()
    for строка in данные:
        таблица.insert('', tk.END, values=строка)

окно = tk.Tk()
окно.title('Магазин канцтоваров — Task 7')
окно.geometry('800x450')

ttk.Label(окно, text='Каталог: Магазин канцтоваров', font=('Arial', 14)).pack(pady=10)

фрейм_кнопок = ttk.Frame(окно)
фрейм_кнопок.pack(pady=5)
ttk.Button(фрейм_кнопок, text='Показать', command=показать_данные).pack(side=tk.LEFT, padx=10)
ttk.Button(фрейм_кнопок, text='Очистить таблицу', command=очистить_таблицу).pack(side=tk.LEFT, padx=10)

фрейм_таблицы = ttk.Frame(окно)
фрейм_таблицы.pack(padx=15, pady=10, fill=tk.X, expand=False)

# Таблица с height=3
таблица = ttk.Treeview(фрейм_таблицы, columns=('name', 'category', 'price', 'quantity', 'reorder_level'), show='headings', height=3)

# Заголовки
таблица.heading('name', text='Товар'); таблица.heading('category', text='Категория'); таблица.heading('price', text='Цена, руб.'); таблица.heading('quantity', text='Остаток'); таблица.heading('reorder_level', text='Порог заказа');

# Ширина
таблица.column('name', width=150, anchor='w'); таблица.column('category', width=120, anchor='w'); таблица.column('price', width=100, anchor='center'); таблица.column('quantity', width=90, anchor='center'); таблица.column('reorder_level', width=120, anchor='center');

скролл = ttk.Scrollbar(фрейм_таблицы, orient='vertical', command=таблица.yview)
таблица.configure(yscrollcommand=скролл.set)

таблица.grid(row=0, column=0, sticky='nsew')
скролл.grid(row=0, column=1, sticky='ns')

окно.mainloop()
