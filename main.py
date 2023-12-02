import streamlit as st
import keyboard
import os
import psutil
import TapexTokenizer
import pandas as pd


# Создаем форму
form = st.form(key="my_form")
# Добавляем строку выбора файла
uploaded_file = form.file_uploader("Выберите файл csv", type=["csv"])
# Добавляем кнопку считывания файла
submit_button = form.form_submit_button(label="Считать файл")

# Добавляем текстовую строку запроса
my_query = form.text_input("Запрос в Tapex", "Рассчитать среднее значение по столбцу")
# Добавляем кнопку отправки запроса в Tapex 
submit_button2 = form.form_submit_button(label="Отправить запрос в Tapex")

# Добавляем кнопку выхода из приложения
exit_app = form.form_submit_button ("Выход")

# Если форма отправлена и файл загружен, то выводим содержимое файла
if submit_button and uploaded_file is not None:
    # Читаем файл как датафрейм
    my_table = pd.read_csv(uploaded_file, encoding='utf-8', sep=';')
    # Преобразуем тип данных
    my_table = my_table.astype(str)
    # Выводим датафрейм
    st.write(my_table)
    st.session_state.my_table = my_table
    

if submit_button2:
    title = TapexTokenizer.tapex_tokenizer(st.session_state.my_table, my_query)
    st.write(f"Ответ TapexTokenizer: {title}")

# Если нажата кнопка выхода, то закрываем вкладку браузера и завершаем процесс Python
if exit_app:
    # Закрываем вкладку браузера streamlit
    keyboard.press_and_release ('ctrl+w')
    # Завершаем процесс Python streamlit
    pid = os.getpid ()
    p = psutil.Process (pid)
    p.terminate ()