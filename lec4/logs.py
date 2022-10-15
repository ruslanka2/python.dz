from datetime import datetime as dt
from gui import dict_log




def get_log(res, op):
    dtime = dt.now()
    with open('log.json', 'a', encoding='utf-8') as file:
        file.write('{}; операция: {}; результат: {}\n'
                     .format(dtime, op, res))