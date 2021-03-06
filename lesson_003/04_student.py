# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
count_months = 10
count = count_months
money_from_parents = 0

while count > 0:
    money_from_parents += round(expenses - educational_grant, 2)
    expenses *= 1.03
    count -= 1

print('На', count_months, 'месяцев нужно попросить у родителей', money_from_parents, 'руб.')
