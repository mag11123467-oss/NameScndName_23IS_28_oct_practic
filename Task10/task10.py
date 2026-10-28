import tkinter as tk
from tkinter import ttk
import psycopg

def очистить_таблицу():
    for строка in таблица.get_children():
        таблица.delete(строка)

def показать_данные():
    with psycopg.connect(
        dbname='computers_task10', user='postgres', password='Admin', host='localhost', port=5432
    ) as соединение:
        with соединение.cursor() as курсор:
            курсор.execute('SELECT name, category, ram_gb, storage_gb, quantity FROM public.computers ORDER BY storage_gb ASC, name ASC')
            данные = курсор.fetchall()

    очистить_таблицу()
    for строка in данные:
        таблица.insert('', tk.END, values=строка)

окно = tk.Tk()
окно.title('Компьютерное оборудование — Task 10')
окно.geometry('800x450')

ttk.Label(окно, text='Каталог: Компьютерное оборудование', font=('Arial', 14)).pack(pady=10)

фрейм_кнопок = ttk.Frame(окно)
фрейм_кнопок.pack(pady=5)
ttk.Button(фрейм_кнопок, text='Показать', command=показать_данные).pack(side=tk.LEFT, padx=10)
ttk.Button(фрейм_кнопок, text='Очистить таблицу', command=очистить_таблицу).pack(side=tk.LEFT, padx=10)

фрейм_таблицы = ttk.Frame(окно)
фрейм_таблицы.pack(padx=15, pady=10, fill=tk.X, expand=False)

# Таблица с height=3
таблица = ttk.Treeview(фрейм_таблицы, columns=('name', 'category', 'ram_gb', 'storage_gb', 'quantity'), show='headings', height=3)

# Заголовки
таблица.heading('name', text='Модель'); таблица.heading('category', text='Тип'); таблица.heading('ram_gb', text='ОЗУ, ГБ'); таблица.heading('storage_gb', text='Накопитель, ГБ'); таблица.heading('quantity', text='Количество');

# Ширина
таблица.column('name', width=150, anchor='w'); таблица.column('category', width=120, anchor='w'); таблица.column('ram_gb', width=90, anchor='center'); таблица.column('storage_gb', width=130, anchor='center'); таблица.column('quantity', width=110, anchor='center');

скролл = ttk.Scrollbar(фрейм_таблицы, orient='vertical', command=таблица.yview)
таблица.configure(yscrollcommand=скролл.set)

таблица.grid(row=0, column=0, sticky='nsew')
скролл.grid(row=0, column=1, sticky='ns')

окно.mainloop()
