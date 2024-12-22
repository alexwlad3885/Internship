# Документация проекта для анализа и визуализации данных об акциях
***
## Общий обзор
* Этот проект предназначен для загрузки исторических данных об акциях и их визуализации.
* Он использует библиотеку yfinance для получения данных и matplotlib для создания графиков.
* Пользователи могут выбирать различные тикеры и временные периоды для анализа, а также просматривать движение цен и скользящие средние на графике.
* Задания нацелены на улучшение пользовательского опыта и расширение аналитических возможностей проекта, предоставляя глубокие и настраиваемые инструменты для анализа данных об акциях.
***
## Структура и модули проекта
1. data_download.py:
    - Отвечает за загрузку данных об акциях.
    - Содержит функции для извлечения данных об акциях из интернета и расчёта скользящего среднего.
2. main.py:
    - Является точкой входа в программу.
    - Запрашивает у пользователя тикер акции и временной период, загружает данные, обрабатывает их и выводит результаты в виде графика.
3. data_plotting.py:
    - Отвечает за визуализацию данных.
    - Содержит функции для создания и сохранения графиков цен закрытия и скользящих средних.
***
## Описание функций
1. data_download.py:
    - fetch_stock_data(ticker, period):
          получает исторические данные об акциях для указанного тикера и временного периода.
          возвращает DataFrame с данными.
    - add_moving_average(data, window_size):
          добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.
    - calculate_and_display_average_price(data):
          функция вычисляет среднее арифметическое по колоннке 'Close' DataFrame за период.
          выводит среднюю цену закрытия акций за заданный период.
2. main.py:
    - main():
          основная функция, управляющая процессом загрузки, обработки данных и их визуализации.
          запрашивает у пользователя ввод данных.
          вызывает функции загрузки и обработки данных.
          передаёт результаты на визуализацию.
3. data_plotting.py:
    - create_and_save_plot(data, ticker, period, filename):
          создаёт график, отображающий цены закрытия и скользящие средние.
          предоставляет возможность сохранения графика в файл.
          параметр filename опционален; если он не указан, имя файла генерируется автоматически.
***
## Пошаговое использование
1. Запустите main.py.
2. Введите интересующий вас тикер акции (например, 'AAPL' для Apple Inc).
3. Введите желаемый временной период для анализа (например, '1mo' для данных за один месяц).
4. Программа обработает введённые данные, загрузит соответствующие данные об акциях, рассчитает скользящее среднее и отобразит график
***
<!--описание коммитов-->
## Описание коммитов
| Название | Описание                                                        |
|-------------|-------------------------------------------------------------------------------|
| first commit| Базовый проект и добавление функции calculate_and_display_average_price(data) |
