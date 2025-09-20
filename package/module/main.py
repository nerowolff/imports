from salary import calculate_salary
from people import get_employees

import datetime


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    str_today=datetime.date.today()
    str_today=str(str_today)
    today_list=str_today.split('-')
    if today_list[1][0] == '0':
        print (type(today_list[1]))
        today_list[1]=today_list[1].replace('0','')
    print(f'Сегодня {today_list[2]}-е число, {today_list[1]}-ого месяца, {today_list[0]}-ого года')
