from datetime import datetime
from math import floor


def validate_year(min_year: int = 1900, max_year: int = 3000):
    """
    Para validar o ano, usamos uma verificação simples para ver se o valor digitado é maior do que o minimo passado no parâmetro e se ele é maior
    do que o máximo passado no parâmetro
    """

    invalidYear = True
    while invalidYear:
        try:
            print('Por favor, digite o ano no formato YYYY (Ex: 1950)')
            year = int(input('Ano do nascimento : ') or 0)
            if year < min_year or year > max_year:
                raise (ValueError)
            invalidYear = False
            return year
        except ValueError:
            print(f"Por favor, selecione um valor menor do que {max_year} para o ano de nascimento") if year > max_year else \
                print(
                    f'Por favor, selecione um valor maior do que {min_year} para o ano de nascimento')
            invalidYear = True


def validate_month(month_order: list):
    invalidMonth = True
    while invalidMonth:
        try:
            print('Por favor, digite um valor no intervalo de 1(Janeiro) a 12(Dezembro)')
            month = int(input('Mes do nascimento : ') or 0)
            if month not in month_order:
                raise (ValueError)
            invalidMonth = False
            return month
        except ValueError:
            invalidMonth = True


def validate_day(month_max: list, month: int):
    invalidDay = True
    while invalidDay:
        try:
            print(
                f'Por favor, digite um valor no intervalo de 1 a {month_max[month]}')
            day = int(input('Dia do nascimento : ') or 0)
            if day <= 0 or day > month_max[month]:
                raise (ValueError)
            invalidDay = False
            return day
        except ValueError:
            invalidDay = True


def get_age():
    today = datetime.today()
    month_order = list(range(1, 13))
    month_max = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = validate_year()
    month = validate_month(month_order)
    day = validate_day(month_max, month-1)
    birth = datetime(year, month, day)
    age = floor(((today - birth).days)/365)
    print(f'O usuario possui {age} anos')


get_age()