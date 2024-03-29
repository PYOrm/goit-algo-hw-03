# Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату, 
# залишаючи тільки цифри та символ '+' на початку. 
# Функція приймає один аргумент - рядок з телефонним номером у будь-якому форматі та перетворює його на стандартний формат, 
# залишаючи тільки цифри та символ '+'. Якщо номер не містить міжнародного коду, функція автоматично додає код '+38' (для України). 
# Це гарантує, що всі номери будуть придатними для відправлення SMS.

# Вимоги до завдання:
# Параметр функції phone_number - це рядок з телефонним номером у різноманітних форматах.
# Функція видаляє всі символи, крім цифр та символу '+'.
# Якщо міжнародний код відсутній, функція додає код '+38'. Це враховує випадки, коли номер починається з '380' (додається лише '+') 
# та коли номер починається без коду (додається '+38').
# Функція повертає нормалізований телефонний номер у вигляді рядка.

import re

def normalize_phone(phone_number: str) -> str:

    pattern = re.compile(r'\+*[^\d]+')
    normal_number = re.sub(pattern, '', phone_number)
    if normal_number[:2] == "38":
        normal_number = "+" + normal_number
    else:
        normal_number = "+38" + normal_number
    return normal_number
