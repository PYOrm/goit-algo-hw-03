# Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, 
# що випали випадковим чином і в певному діапазоні під час чергового тиражу. 
# Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.
# Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), 
# яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.
# Вона буде повертати випадковий набір чисел у межах заданих параметрів, 
# причому всі випадкові числа в наборі повинні бути унікальні.

# Вимоги до завдання:
# Параметри функції:
# min - мінімальне можливе число у наборі (не менше 1).
# max - максимальне можливе число у наборі (не більше 1000).
# quantity - кількість чисел, які потрібно вибрати (значення між min і max).
# Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
# Функція повертає список випадково вибраних, відсортованих чисел. 
# Числа в наборі не повинні повторюватися. Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.

import random

def get_numbers_ticket(min:int, max:int, quantity:int) -> list:
    if (min < 1) or (max > 1000) or \
        (max-min < quantity):                                   # return empty list if min, max not in range
        return []                                               # or can not generate {quantity} unic numbers in selected range
    
    generated_values_set = set()                                # declare empty set. set can store only unic values.

    while len(generated_values_set) < quantity:                 # add to set random numbers from order range, 
        generated_values_set.add(random.randint(min, max))      # till set accumulated {quantity} numbers 
    
    return sorted(list(generated_values_set))                   # return sorted list of numbers.





