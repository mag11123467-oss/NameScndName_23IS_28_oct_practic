import tkinter as tk
from tkinter import ttk
import psycopg

def очистить_таблицу():
    for строка in таблица.get_children():
        таблица.delete(строка)

def показать_данные():
    with psycopg.connect(
        dbname='books_task6', user='postgres', password='Admin', host='localhost', port=5432
    ) as соединение:
        with соединение.cursor() as курсор:
            курсор.execute('SELECT title, author, publication_year, pages, copies FROM public.books ORDER BY publication_year ASC, title ASC')
            данные = курсор.fetchall()

    очистить_таблицу()
    for строка in данные:
        таблица.insert('', tk.END, values=строка)

окно = tk.Tk()
окно.title('Библиотека — Task 6')
окно.geometry('800x450')

ttk.Label(окно, text='Каталог: Библиотека', font=('Arial', 14)).pack(pady=10)

фрейм_кнопок = ttk.Frame(окно)
фрейм_кнопок.pack(pady=5)
ttk.Button(фрейм_кнопок, text='Показать', command=показать_данные).pack(side=tk.LEFT, padx=10)
ttk.Button(фрейм_кнопок, text='Очистить таблицу', command=очистить_таблицу).pack(side=tk.LEFT, padx=10)

фрейм_таблицы = ttk.Frame(окно)
фрейм_таблицы.pack(padx=15, pady=10, fill=tk.X, expand=False)

# Таблица с height=3
таблица = ttk.Treeview(фрейм_таблицы, columns=('title', 'author', 'publication_year', 'pages', 'copies'), show='headings', height=3)

# Заголовки
таблица.heading('title', text='Название'); таблица.heading('author', text='Автор'); таблица.heading('publication_year', text='Год'); таблица.heading('pages', text='Страниц'); таблица.heading('copies', text='Экземпляров');

# Ширина
таблица.column('title', width=150, anchor='w'); таблица.column('author', width=150, anchor='w'); таблица.column('publication_year', width=80, anchor='center'); таблица.column('pages', width=90, anchor='center'); таблица.column('copies', width=100, anchor='center');

скролл = ttk.Scrollbar(фрейм_таблицы, orient='vertical', command=таблица.yview)
таблица.configure(yscrollcommand=скролл.set)

таблица.grid(row=0, column=0, sticky='nsew')
скролл.grid(row=0, column=1, sticky='ns')

окно.mainloop()
