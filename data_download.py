import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    """
    функция вычисляет и выводит среднюю цену закрытия акций за заданный период
    :param data: DataFrame
    :return: average_price среднее значение колонки 'Close'
    """
    average_price = data["Close"].mean()
    return average_price


def notify_if_strong_functionals(data, threshold):
    """
    функция вычисляет максимальную цену актива за один день (истинный диапазон true range),
            усредняет полученные значения на заданном периоде (средний истинный диапазон average true range)
            сравнивает ATR с заданным порогом threshold
            если ATR превышает threshold, пользователь получает уведомление
    :param data: DataFrame
    :param threshold: заданное значение порога цены в процентах
    :return: ATR (средний истинный диапазон)
    """

    data_lict = []
    # Расчёт истинного диапазона (True Range, TR)
    rows_count = len(data) - 1
    prev = None
    for row in data.itertuples():
        min_func = row.Low      # минимальная цена актива за 1 день
        max_func = row.High     # максимальная цена актива за 1 день
        if prev is not None:    # цена закрытия предыдущего дня
            close_funk = getattr(prev, "Close")
        else:
            close_funk = max_func
        prev = row
        # разность между максимальной и минимальной ценами актива за 1 день
        tr_1 = max_func - min_func
        # разность между максимальной ценой актива за 1 день и ценой закрытия предыдущего
        tr_2 = max_func - close_funk
        # разность между ценой закрытия предыдущего и минимальной ценой актива за 1 день
        tr_3 = close_funk - min_func
        # выбираем наибольшее из трёх значений
        tr = max(tr_1, tr_2, tr_3)
        # сохраняем данные в списке
        data_lict.append(tr)

    # Усреднение полученных значений на заданном интервале (вычисление ATR)
    atr = sum(data_lict) / rows_count
    # Если ATR больше порга threshold, возвращается ATR
    if atr > float(threshold):
        return atr
