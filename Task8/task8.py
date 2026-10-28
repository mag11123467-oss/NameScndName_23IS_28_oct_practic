import tkinter as tk
from tkinter import ttk
import psycopg

def очистить_таблицу():
    for строка in таблица.get_children():
        таблица.delete(строка)

def показать_данные():
    with psycopg.connect(
        dbname='sports_task8', user='postgres', password='Admin', host='localhost', port=5432
    ) as соединение:
        with соединение.cursor() as курсор:
            курсор.execute('SELECT name, sport, participants, sessions, fee FROM public.sports ORDER BY fee ASC, name ASC')
            данные = курсор.fetchall()

    очистить_таблицу()
    for строка in данные:
        таблица.insert('', tk.END, values=строка)

окно = tk.Tk()
окно.title('Спортивные секции — Task 8')
окно.geometry('800x450')

ttk.Label(окно, text='Каталог: Спортивные секции', font=('Arial', 14)).pack(pady=10)

фрейм_кнопок = ttk.Frame(окно)
фрейм_кнопок.pack(pady=5)
ttk.Button(фрейм_кнопок, text='Показать', command=показать_данные).pack(side=tk.LEFT, padx=10)
ttk.Button(фрейм_кнопок, text='Очистить таблицу', command=очистить_таблицу).pack(side=tk.LEFT, padx=10)

фрейм_таблицы = ttk.Frame(окно)
фрейм_таблицы.pack(padx=15, pady=10, fill=tk.X, expand=False)

# Таблица с height=3
таблица = ttk.Treeview(фрейм_таблицы, columns=('name', 'sport', 'participants', 'sessions', 'fee'), show='headings', height=3)

# Заголовки
таблица.heading('name', text='Секция'); таблица.heading('sport', text='Вид спорта'); таблица.heading('participants', text='Участников'); таблица.heading('sessions', text='Занятий/нед.'); таблица.heading('fee', text='Цена/мес., руб.');

# Ширина
таблица.column('name', width=120, anchor='w'); таблица.column('sport', width=150, anchor='w'); таблица.column('participants', width=120, anchor='center'); таблица.column('sessions', width=120, anchor='center'); таблица.column('fee', width=130, anchor='center');

скролл = ttk.Scrollbar(фрейм_таблицы, orient='vertical', command=таблица.yview)
таблица.configure(yscrollcommand=скролл.set)

таблица.grid(row=0, column=0, sticky='nsew')
скролл.grid(row=0, column=1, sticky='ns')

окно.mainloop()
