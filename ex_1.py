# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

# Вимоги до завдання:
# Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
# Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, 
# результат має бути від'ємним.
# У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
# Для роботи з датами слід використовувати модуль datetime Python.

import datetime

def get_days_from_today(date:str) -> int:
    enter_date = datetime.datetime.strptime(date,"%Y-%m-%d").date()     # Try convert string to datetime and get date part 
    today = datetime.date.today()                                       # get current date
    return (today - enter_date).days                                    # return differance in days 


while True:                                                             # start unlimit cycle 
    get_date = input("Enter a date: ")                                  # get date from user
    try:                                                                # try call function until recive string with correct date format
        print(get_days_from_today(get_date))                            # call function get_days_from_today and print return result
        break                                                           # stop unlimit cycle
    except ValueError:                                           
        print ("Wrong date format. Try again")                          # print error and return to begin of cycle