from datetime import date
from datetime import datetime

def date_para_str(data) -> str:
    return datetime.strftime(data, '%d/%m/%Y')

def str_para_date(data) -> date:
    return datetime.strptime(data, '%d/%m/%Y').date()

def formata_float_str(valor) -> str:
    return f'R$ {valor:,.2f}'


